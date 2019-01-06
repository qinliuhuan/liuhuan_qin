from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, HiddenField, TextAreaField, DateTimeField, FileField
from flask_wtf.file import FileField, FileAllowed

class BaseForm(Form):
    id = HiddenField('id')


class BulletinForm(BaseForm):
    # id = HiddenField('id')
    dt = DateTimeField('publish time', format='%Y-%m-%d %H:%M:%S')
    title = StringField("Title")
    content = TextAreaField('Detail')
    valid = BooleanField('Effective or not')
    source = StringField('source')
    author = StringField('author')
    image = FileField('upload image', validators=[FileAllowed('jpg', 'png'), 'Images onely!'])
