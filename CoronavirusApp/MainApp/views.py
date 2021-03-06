from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import requests


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/aboutPage.html')


def Summary(request):
    url = 'https://api.covid19api.com/summary'
    res = requests.get(url).json()

    getGlobalSum = {
        'newConf': res["Global"]["NewConfirmed"],
        'totConf': res["Global"]["TotalConfirmed"],
        'newDeaths': res["Global"]["NewDeaths"],
        'totDeaths': res["Global"]["TotalDeaths"],
        'newRec': res["Global"]["NewRecovered"],
        'totRec': res["Global"]["TotalRecovered"]
    }



    allCountry = []
    i = 0

    for value in res["Countries"]:
        getListOfCountries = {
            'country': res["Countries"][i]["Country"],
            'date': res["Countries"][i]["Date"],
            'newCases': res["Countries"][i]["NewConfirmed"],
            'Cases': res["Countries"][i]["TotalConfirmed"],
            'newD': res["Countries"][i]["NewDeaths"],
            'Deaths': res["Countries"][i]["TotalDeaths"],
            'newR': res["Countries"][i]["NewRecovered"],
            'Recovers': res["Countries"][i]["TotalRecovered"]
        }

        allCountry.append(getListOfCountries)
        i += 1






    context = {'infoGlob': getGlobalSum,'infoCoun':allCountry }
    return render(request, 'main/index.html', context)


