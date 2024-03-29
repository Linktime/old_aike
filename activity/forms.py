# -*- coding:utf-8 -*-

from django import forms
from activity.models import Activity
from tools.forms import LtModelForm


class ActivityCreateForm(LtModelForm):
# class ActivityCreateForm(forms.ModelForm):
#     price = forms.IntegerField(widget=forms.TextInput(attrs={"class":"col-md-4"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"hide"}))
    price = forms.CharField(widget=forms.TextInput(attrs={"class":"hide"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"hide"}))
    date = forms.DateField(widget=forms.DateInput(attrs={"class":"hide"}))
    introduction = forms.CharField(widget=forms.Textarea(attrs={"class":"hide"}))
    abstract = forms.CharField(widget=forms.Textarea(attrs={"rows":"4"}))
    class Meta:
        model = Activity
        fields = ("name","address","introduction","date","place","price","abstract")

    #TODO
    # default creater use login user