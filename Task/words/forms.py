from django import forms

from .models import Word


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ("file",)

    def clean_file(self):
        file = self.cleaned_data["file"]
        if not file:
            raise forms.ValidationError("No file provided.")
        return file
