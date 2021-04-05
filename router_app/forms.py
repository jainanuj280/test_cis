from django import forms
from router_app.models import RouterDetails

class RouterDetailsForm(forms.ModelForm):
    class Meta:
        model = RouterDetails
        fields = "__all__"