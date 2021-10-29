from django import forms

from app.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'



class RecipeFormReadOnly(forms.ModelForm):

    title = forms.CharField(disabled=True)
    image_url = forms.URLField(disabled=True)
    description = forms.CharField(disabled=True)
    ingredients = forms.CharField(disabled=True)
    time = forms.IntegerField(disabled=True)
                                  # widget=forms.Textarea(
                                  #     attrs={'class': 'form-control rounded-2'}
                                  # ))
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')

