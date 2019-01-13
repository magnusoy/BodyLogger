from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import DailyForm, WeeklyForm
import os


def updateDailyTable(user, data):
    fname = f'users/{user}/{user}_daily.csv'
    dirname = f'users/{user}'
    if os.path.isfile(fname):
        with open(fname, 'a', encoding='utf-8') as f:
            f.write(f'{data["date"]},{data["weight"]}\n')
    else:	
        os.mkdir(dirname)
        with open(fname, 'w', encoding='utf-8') as f:
            f.write('date,weight\n')
            f.write(f'{data["date"]},{data["weight"]}\n')

def updateWeeklyTable(user, data):
    fname = f'users/{user}/{user}_weekly.csv'
    dirname = f'users/{user}'
    if os.path.isfile(fname):
        with open(fname, 'a', encoding='utf-8') as f:
            f.write(f'{data["date"]},{data["weight"]},{data["shoulders"]},{data["chest"]},{data["arms"]},{data["forearms"]},{data["waist"]},{data["hips"]},{data["legs"]},{data["calfs"]}\n')
    else:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write('date,weight,shoulders,chest,arms,forearms,waist,hips,legs,calfs\n')
            f.write(f'{data["date"]},{data["weight"]},{data["shoulders"]},{data["chest"]},{data["arms"]},{data["forearms"]},{data["waist"]},{data["hips"]},{data["legs"]},{data["calfs"]}\n')
    
def dailyUpdate(request):
    if request.method == 'GET':
        form = DailyForm()
    else:
        form = DailyForm(request.POST)
        if form.is_valid():
            user = request.user.username
            updateDailyTable(user, form.cleaned_data)
            return redirect('success')
    return render(request, "daily.html", {'form': form})


def successView(request):
    return HttpResponse('Success, table updated!')


def weeklyUpdate(request):
    if request.method == 'GET':
        form = WeeklyForm()
    else:
        form = WeeklyForm(request.POST)
        if form.is_valid():
            user = request.user.username
            updateWeeklyTable(user, form.cleaned_data)
            return redirect('success')
    return render(request, "weekly.html", {'form': form})

