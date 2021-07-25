from django.shortcuts import render, redirect
from django.http import HttpResponse
import joblib

def home(request):
    if request.method == 'POST':

        catmodel = joblib.load('predfile.sav')
        predlist = []

        predlist.append(request.POST.get('pm1'))
        predlist.append(request.POST.get('pm2'))
        predlist.append(request.POST.get('NO'))
        predlist.append(request.POST.get('NO2'))
        predlist.append(request.POST.get('NOx'))
        predlist.append(request.POST.get('NH3'))
        predlist.append(request.POST.get('CO'))
        predlist.append(request.POST.get('SO2'))
        predlist.append(request.POST.get('O3'))
        predlist.append(request.POST.get('Benzene'))
        predlist.append(request.POST.get('Toluene'))
        predlist.append(request.POST.get('Xylene'))
        
        prediction = catmodel.predict([predlist])
        print('prediction', prediction)

        if prediction  >=0 and prediction  <=50:
            str="""Levels of Concern : Good\n\n\
                    Values of Index : 0 to 50\n\n\
                    Description of Air Quality :
                    Air quality is Good, and air pollution poses little or no risk."""
            res = str
            print(str)

        if prediction  >=51 and prediction  <=100:
            str="""Levels of Concern : Satisfactory\n\n\
                    Values of Index : 51 to 100\n\n\
                    Description of Air Quality :
                    May cause minor breathing discomfort to sensitive people."""
            res = str
            print(str)

        if prediction  >=101 and prediction  <=200:
            str="""Levels of Concern : Moderately polluted\n\n\
                    Values of Index : 101 to 200\n\n\
                    Description of Air Quality :
                    May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults."""
            res = str
            print(str)

        if prediction >201 and prediction <=300:
            str="""Levels of Concern : Poor\n\n\
                    Values of Index : 201 to 300\n\n\
                    Description of Air Quality :
                    May cause breathing discomfort to people on prolonged exposure, and discomfort to people with heart disease."""
            res = str
            print(str)
        
        if prediction  >=301 and prediction <=400:
            str="""Levels of Concern : Very poor\n\n\
                    Values of Index : 301 to 400\n\n\
                    Description of Air Quality :
                    May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases."""
            res = str
            print(str)

        if prediction  >=401:
            str="""Levels of Concern : Severe \n\n\
                    Values of Index : 401 and higher\n\n\
                    Description of Air Quality :
                    May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease. The health impacts may be experienced even during light physical activity."""
            res = str
            print(str)

        return render(request, 'home.html',{'res':res})
    else:
        return render(request, 'home.html',{'res':''})