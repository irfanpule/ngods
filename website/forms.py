from django import forms
from pyexcel_ods import get_data, save_data

from website.utils import path_file_save

class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'accept': ".ods"}), label='Unggah berkas')

    def ods_save_to_storage(self, session_key):
        ods_file = self.cleaned_data['file']
        save_data(path_file_save(session_key), get_data(ods_file))
