from django import forms
from .models import CNNImage


class MemeUploadForm(forms.ModelForm):
    class Meta:
        model = CNNImage
        fields = ['image', 'name', "submitted_as_meme"]


class SearchMemeForm(forms.Form):
    search = forms.CharField()

    def __init__(self, *args, request_data=None, **kwargs):
        super().__init__(*args, **kwargs)
        # To help pagination work with filtered object lists the initial field is set with the query value
        self.fields['search'].initial = request_data.GET.get('search')
