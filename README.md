# Flask Amazon Web Services (AWS) Dashboard 

## Description 
Motivation behind this project was to learn about AWS VPCs and security groups and experiment with their Python SDK, boto3. 
This is an Amazon AWS Dashboard to validate VPC and security group configuration written in Python using Flask and Bootstrap 
on the front end and Boto3 using EC2 API on the back end.  

## Installation Setup: 
#### Environment tested on:
* MAC OS X 10.13.3 (High Sierra) 
* Python 3.7.1 

#### Requirements: 
* AWS account (free tier)
* Create an IAM user that has access keys (best practice) 
* Configure environment variable for CSFR form validation
  * Run export SECRET_KEY = "enter secret key here"
* Static folder contains:
  * css\bootstrap.min.css 
  * css/main.css

#### Setup virtual environment:
* virtualenv --python=python3.7 .
*	source ./bin/activate
*	pip install -r requirements.txt

# Usage 
## Run locally 
* Run python flask-aws-dashboard-heroku.py 
* Open browser to http://127.0.0.1:5000/
* 3 buttons (for each flask route, two GET and one POST) do just as their names describe. Login to your AWS dashboard to compare output. 
	* show vpc
	* show security groups
	* create vpc - create a new vpc 

## Deploy Heroku 
* Create an account on Heroku
* Config vars 
  * AWS_ACCESS_KEY_ID
  * AWS_SECRET_ACCESS_KEY
  * AWS_EC2_REGION
  * SECRET_KEY

### Setup environment:
  * heroku login
  * heroku create
  * git init 
  * git commit -am "enter descriptive message here"
  * git push heroku master		

# License
GNU General Public License v3.0
