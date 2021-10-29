from django import forms

from animal.models import Animal



class AnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Animal
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }

