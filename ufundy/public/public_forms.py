#!/usr/bin/env python
#

from wtforms import Form, TextField, TextAreaField, IntegerField, FileField, SelectField, BooleanField, validators


class ContactuFundyForm(Form):
    name = TextField(u'Your Name', validators=[validators.required()])
    city = TextField(u'City', validators=[validators.required()])
    email = TextField(u'Email', validators=[validators.required()])
    message = TextAreaField(u'Message')


class WaitingListForm(Form):
    email = TextField(u'Your Name', validators=[validators.required()])
    company = TextField(u'City', validators=[validators.required()])
    founder = TextField(u'Email', validators=[validators.required()])

    def validate_company(form, field):
        founder = form.founder.data
        if founder and not field.data:
            raise validators.ValidationError('If you are Founder, blah blah blah')
