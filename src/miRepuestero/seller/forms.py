from django import forms
from .models import Publication

class CreatePublicationForm(forms.ModelForm):

    class Meta:
        model = Publication
        fields = ['name', 
                'part_number',
                'price',
                'aka',
                'works_for',
                'description',
                'image',
                'image2',
                'image3',
                'image4',
                'image5']          

    
    def __init__(self, *args, **kwargs):
        super(CreatePublicationForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs\
            .update({                
                'class': 'materialize-textarea'
            })