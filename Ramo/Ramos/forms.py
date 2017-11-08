from django import forms
from .models import Ramo, Flor

class FlorForm(forms.ModelForm):

        class Meta:
            model = Flor
            fields = ('nombre', 'caracteristica','color','precio')

class RamoForm(forms.ModelForm):

    class Meta:
        model = Ramo
        fields = ('nombre', 'flores')
    def __init__ (self, *args, **kwargs):
        super(RamoForm, self).__init__(*args, **kwargs)
        self.fields["flores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["flores"].queryset = Flor.objects.all()
