from django.shortcuts import render
from django.http import HttpResponse

import os
import joblib

model1 = joblib.load(os.path.dirname(__file__)+ "\\myModel.pk1")
model2 = joblib.load(os.path.dirname(__file__)+ "\\mySVCModel.pk1")

# Create your views here.
def index(request):
    return render(request,'../templates/index.html')

def checkSpam(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>" + request.method)
    if{request.method == "POST"}:
        finalAns = None
        
        algo = request.POST.get("algo")
        rawData = request.POST.get("rawdata")

        if(algo == "Algo-1"):
            finalAns = model1.predict([rawData])[0]
            param = {"answer" : finalAns}
        elif(algo == "Algo-2"):
            finalAns = model2.predict([rawData])[0]
            param = {"answer" : finalAns}
        return render(request,'../templates/output.html', param)
    else:
        return render(request,'../templates/index.html')

