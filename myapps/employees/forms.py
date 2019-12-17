from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Remove ':' default label suffix when rendering individual form fields
        # see corresponding form in 'update.html'
        kwargs.setdefault('label_suffix', '*')
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'class': 'form-control'})
            # field.widget.attrs.update({'placeholder': field.label})

    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'full_name': 'Full Name',
            'emp_code': 'Emp. Code',
            'mobile_number': 'Mobile Number',
            'position': 'Position',
        }
