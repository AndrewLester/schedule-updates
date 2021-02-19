from app.utils import IntervalField
from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.fields.core import DateTimeField, FormField, IntegerField
from wtforms.validators import Length, Required, Regexp


class ScheduledJob(FlaskForm):
    id = StringField()
    scheduled_for = DateTimeField()
    scheduled_in = IntervalField()


class UpdateForm(FlaskForm):
    id = IntegerField(validators=[Required()])
    realm_type = StringField('Update course type', validators=[Required(), Regexp('(courses|groups|schools|districts|sections)')])
    realm_id = StringField('Update course ID', validators=[Required()])
    body = StringField('Update body', validators=[Required()])
    attachments = StringField(default='')

    job = FormField(ScheduledJob, label='Post time')
