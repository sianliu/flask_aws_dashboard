#! /usr/bin/env python

"""

Github: Python Flask Bootstrap Boto3 AWS Validation Dashboard

Amazon AWS Dashboard to validate VPC and security group configuration created using Boto3, EC2 API, Python, and Flask.     

https://flask-aws-dashboard-heroku.herokuapp.com/
"""
__author__ = "Jonathan Liu"
__author_email__ = "mr@sianliu.com"
__license__ = "GNU GPLv3"


from flask import Flask, render_template, url_for, request, redirect, flash
from forms import New_vpc_form
from botocore.exceptions import ClientError
import boto3
import os

app = Flask(__name__)
# Required for form validation using CSFR
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

'''
Renders the Home page
'''


@app.route('/')
def index():
    return render_template('index.html')


'''
The show_vpc_info route displays a list of your configured of Amazon Virtual Private Clouds (VPC)
vpc_info holds the list of VPCs to render
boto3.resource is a resource representing Amazon Elastic Compute Cloud (EC2)
boto3.client is a low-level client representing Amazon Elastic Compute Cloud (EC2)
The method client.describe_vpcs(**kwargs) describes one or more of your VPCs
'''


@app.route('/vpc', methods=['GET'])
def show_vpc_info():
    vpc_info = []
    ec2 = boto3.resource('ec2', os.environ.get('AWS_EC2_REGION'))
    client = boto3.client('ec2', os.environ.get('AWS_EC2_REGION'))
    # returns dictionary containing vpcs
    temp_vpc_info = client.describe_vpcs()
    # parse json file and add information to vpc_info list
    if temp_vpc_info:
        for each_vpc in temp_vpc_info['Vpcs']:
            vpc_info.append(each_vpc)
    return render_template("vpc.html", vpc_info=vpc_info, title='VPC Info')


'''
The show_security_group_info route displays a list of your Amazon Security Groups (Note: VPCS and security groups have a 1:1 relationship)
sg_info holds the list of security groups to render
boto3.resource is a resource representing Amazon Elastic Compute Cloud (EC2)
boto3.client is a low-level client representing Amazon Elastic Compute Cloud (EC2)
The method client.describe_security_groups(**kwargs) describes one or more of your security groups
'''


@app.route('/securitygroup', methods=['GET'])
def show_security_group_info():
    sg_info = []
    ec2 = boto3.resource('ec2', os.environ.get('AWS_EC2_REGION'))
    client = boto3.client('ec2', os.environ.get('AWS_EC2_REGION'))
    # returns dictionary containing security groups
    sg_info = client.describe_security_groups()
    # parse json file and add information to sg_info list
    sg_info = sg_info['SecurityGroups']
    return render_template("securitygroup.html", sg_info=sg_info, title='Security Group Info')


'''
The create_new_vpc route creates a new VPC
boto3.client is a low-level client representing Amazon Elastic Compute Cloud (EC2)
New_vpc_form() is a custom class that uses WTForms, a flexible forms validation and rendering library for Python web development
client.create_vpc(**kwargs) creates a VPC with the specified IPv4 CIDR block
'''


@app.route('/createvpc', methods=['GET', 'POST'])
def create_new_vpc():
    client = boto3.client('ec2', os.environ.get('AWS_EC2_REGION'))
    form = New_vpc_form()
    CidrBlock = form.subnet_to_create.data
    if CidrBlock:
        try:
            new_vpc = client.create_vpc(CidrBlock=CidrBlock)
            flash(u'The VPC was created', 'error')
            return redirect(url_for('create_new_vpc'))
        except ClientError as e:
            if e.response['Error']['Code'] == 'VpcLimitExceeded' or 'TypeError':
                flash('Maximum VPCs reached. Ask Jonathan to delete one.')
            else:
                raise e
    return render_template('createvpc.html', form=form)


if __name__ == '__main__':
    app.run()
