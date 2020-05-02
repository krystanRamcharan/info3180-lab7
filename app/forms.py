from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import DataRequired, Length

class UploadForm(FlaskForm):
  photo = FileField('Photo',validators= 
                  [ FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
  
  description=TextAreaField('description) [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
  
  submit = SubmitField('Submit')
  
  
