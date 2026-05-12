from django import forms
from . import models



class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.EventRegistration
        fields = "__all__"
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': 'Enter your age'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Create a password'
            }),
        }


    
    def clean(self):
        data = self.cleaned_data

        if len(data.get('full_name')) <= 5:
            raise forms.ValidationError("Full name must be at least 5 character")

        if not data.get('email').endswith("@gmail.com"):
            raise forms.ValidationError("Email must end with @gmail.com")
        
        if data.get('age') < 18 or data.get('age') < 0:
            raise forms.ValidationError("Age must be 18 and above")
        
        if len(data.get('password')) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")


        return super().clean()