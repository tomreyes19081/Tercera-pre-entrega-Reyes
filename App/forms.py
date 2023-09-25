from django import forms

class sedanform(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    fechacompra = forms.DateField()

class coupeform(forms.Form):
    marca2 = forms.CharField()
    modelo2 = forms.CharField()
    fechacompra2 = forms.DateField()
class suvform(forms.Form):
    marca3 = forms.CharField()
    modelo3 = forms.CharField()
    fechacompra3 = forms.DateField()