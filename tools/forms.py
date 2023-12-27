from .models import Pdf
from django.forms import ModelForm

class UploadPdfForm(ModelForm):
    class Meta:
        model = Pdf
        fields = ('category','pdf')