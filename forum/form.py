from django.forms import ModelForm
from .models import project

class project_form(ModelForm):
    class Meta:
        model= project
        fields='__all__'
