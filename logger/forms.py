from django import forms
import datetime

class DailyForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today)
    weight = forms.IntegerField(required=True)

class WeeklyForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today)
    weight = forms.IntegerField(required=True)
    shoulders = forms.IntegerField(required=True)
    chest = forms.IntegerField(required=True)
    arms = forms.IntegerField(required=True)
    forearms = forms.IntegerField(required=True)
    waist = forms.IntegerField(required=True)
    hips = forms.IntegerField(required=True)
    legs = forms.IntegerField(required=True)
    calfs = forms.IntegerField(required=True)
