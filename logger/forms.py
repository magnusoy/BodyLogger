from django import forms
import datetime

class DailyForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today)
    weight = forms.FloatField(required=True)

class WeeklyForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today)
    weight = forms.FloatField(required=True)
    shoulders = forms.FloatField(required=True)
    chest = forms.FloatField(required=True)
    arms = forms.FloatField(required=True)
    forearms = forms.FloatField(required=True)
    waist = forms.FloatField(required=True)
    hips = forms.FloatField(required=True)
    legs = forms.FloatField(required=True)
    calfs = forms.FloatField(required=True)
