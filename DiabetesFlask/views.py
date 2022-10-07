from os import path
from django.shortcuts import render
from django.http import JsonResponse
from pymongo import MongoClient
import numpy as np
from markupsafe import escape
import pickle
from pathlib import Path
import pandas as pd


# Create your views here.

cluster = MongoClient("mongodb://freecosmosmongo:96H8EIaveSasdyY5IIvuvml0cYXZaM9DuO536yJYLvXfUxSypKfOPigVuBPyusllTfiXPjD2FSAqIDHIF9qdfg==@freecosmosmongo.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@freecosmosmongo@")
db = cluster["firstDB"]
collection = db["c2"]

path = Path('./model_Diabetes')
with path.open(mode='rb') as f:
    mp = pickle.load(f)


def home(request):
    return render(request, 'heartDisease/home.html')


def predict(request):

    data1 = int(request.POST.get('a'))
    data2 = int(request.POST.get('b'))
    data3 = int(request.POST.get('c'))
    data4 = int(request.POST.get('d'))

    data5 = int(request.POST.get('e'))
    data6 = float(request.POST.get('f'))
    data7 = float(request.POST.get('g'))
    data8 = int(request.POST.get('h'))


    # Data1 = int(request.POST.get('a'))
    # if Data1 == 0:
    #     Data1 = "No"
    # elif Data1 == 1:
    #     Data1 = "Yes"

    # Data2 = int(request.POST.get('b'))
    # if Data2 == 0:
    #     Data2 = "No"
    # elif Data2 == 1:
    #     Data2 = "Yes"

    # Data3 = int(request.POST.get('c'))
    # if Data3 == 0:
    #     Data3 = "No"
    # elif Data3 == 1:
    #     Data3 = "Yes"

    # Data4 = int(request.POST.get('d'))
    # if Data4 == 0:
    #     Data4 = "No"
    # elif Data4 == 1:
    #     Data4 = "Yes"

    # Data5 = int(request.POST.get('e'))
    # if Data5 == 0:
    #     Data5 = "No"
    # elif Data5 == 1:
    #     Data5 = "Yes"

    # Data6 = int(request.POST.get('f'))

    # Data7 = int(request.POST.get('g'))
    # if Data7 == 0:
    #     Data7 = "No"
    # elif Data7 == 1:
    #     Data7 = "Yes"

    # Data8 = int(request.POST.get('h'))
    # if Data8 == 0:
    #     Data8 = "No Diabetes"
    # elif Data8 == 1:
    #     Data8 = "Pre-Diabetes"
    # elif Data8 == 2:
    #     Data8 = "Diabetes"

    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8]])
    pred = mp.predict(arr)
    # pred2 = model.predict(arr)

    # model = pd.read_pickle('./model_pickle.pickle')
    # return render(request, 'heartDisease/after.html', {'data': pred})

    # result = model.predict([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16]])


    if pred == 0:
        finalData = "Diabetes Negative"
    else:
        finalData = "Diabetes Positive"

    myList = [
        {"question a": data1, "question b": data2, "question c": data3, "question d": data4, "question e": data5, "question f": data6, "question g": data7, "question h": data8, "result": finalData}
    ]

    collection.insert_many(myList)

    # return render(request, 'heartDisease/after.html', {'pred': pred})
    # return render(request, 'heartDisease/after.html', {'pred': result})
    # classification = result[0]
    # return JsonResponse({'result': classification})
    # return JsonResponse({result})

    context = {'pred': pred}
    return render(request, 'heartDisease/after.html', context)
    # return render(request, 'heartDisease/after.html', pred)

# def signup(request):
#     return HttpResponse(request, "heartDisease/signup.html")


# def signin(request):
#     return HttpResponse(request, "heartDisease/signin.html")


# def signout(request):
#     pass
