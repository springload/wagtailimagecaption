from django import forms
from django.utils.translation import ugettext as _


class CaptionForm(forms.Form):
    caption = forms.CharField(label=_("Image caption"), max_length=255)
