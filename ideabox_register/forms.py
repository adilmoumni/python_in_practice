from django import forms
from .models import Employee


class EmployeeFrom(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('__all__')
        lables = {
            'fullname': 'Full -Name',
            'emp_code': 'EMP Code',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeFrom, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
