from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class New_vpc_form(FlaskForm):
    subnet_to_create = StringField('New Subnet (required)',
                                   validators=[InputRequired(), Length(min=9, max=18)])
    submit = SubmitField('Create new VPC')
