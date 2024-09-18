from django import forms
from .models import User, Student, Instructor, Department

class UserSignupForm(forms.ModelForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)
    
    class Meta:
        model = User
        fields = ['email', 'user_type']


class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['otherNames', 'surname', 'level', 'matricNumber', 'dateOfBirth', 'gender', 'studentPhoneNumber']


class InstructorSignupForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'department', 'phoneNumber']