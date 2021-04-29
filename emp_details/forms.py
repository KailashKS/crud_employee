from django import forms
from .models import Employee


class DateInput(forms.DateInput):
    input_type = 'date'


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('__all__')

        genderChoices = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others')
        )

        dept_choices = (
            ('Junior Programmer', 'Junior Programmer'),
            ('Senior Programmer', 'Senior Programmer'),
            ('Human Resources', 'Human Resources'),
            ('Technical Assistant', 'Technical Assistant')
        )

        eval_check = (
            ('1', 'Passed Psych Evaluation 1'),
            ('2', 'Passed Psych Evaluation 2'),
            ('3', 'Passed Physical Evaluation')
        )
        # labels = {
        #     'img': 'Upload Image ',
        #     'name': 'Enter Employee Name ',
        #     'dob': 'Enter Date of Birth ',
        #     'gender': 'Select your gender ',
        #     'eval': 'Mental and Physical Evaluation ',
        #     'salary': 'Enter Salary (in Rupees) ',
        #     'dept': 'Select Department ',
        #     'remarks': "Employer's Remarks "
        # }

        widgets = {
            'dob': forms.DateInput(format=('%d/%m/%Y'),
                                   attrs={'placeholder': 'Enter date of birth: ', 'type': 'date', 'required': True}),
            'eval': forms.CheckboxSelectMultiple(choices=eval_check, attrs={'class': "custom-list"}),
            'dept': forms.Select(choices=dept_choices),
            'gender': forms.RadioSelect(choices=genderChoices, attrs={'class': "custom-list"}),
            'remarks': forms.Textarea(attrs={'style': 'height: 50px;width:150px;', 'required': True})
        }
