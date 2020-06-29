from django import forms
from .models import Albums


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = [
            'albumcover',
            'title',
            'artist',
            'release_date',
            
        ]