import requests
while True:
    shahar=input('Shaharingiz nomini kiriting: ')

    url=f'http://api.weatherapi.com/v1/current.json?key=91c4fb4f07eb40b5b3a125700220403&q={shahar}&aqi=yes'

    obhavo=requests.get(url).json()

    try:
        a=obhavo['location']['country']
        b=obhavo['location']['region']
        c=obhavo['location']['name']
        d=obhavo['current']['last_updated']
        e=obhavo['current']['temp_c']
        f=obhavo['current']['condition']['text']
        g=obhavo['current']['wind_kph']
        i=obhavo['current']['pressure_mb']
        j=obhavo['current']['humidity']
        k=obhavo['current']['cloud']
        s=(f'Davlat-{a},\n Viloyat -{b}\nShahar - {c}\nOhirgi yangilanish -{d}\nTemperatura (C)-{e}\nHavo-{f}\nShamol tezligi(km/soat)-{g}\nBosim(mega pascal) -{i}\nNamlik-{j}\nBulut -{k} %')
    except:
        KeyError: print("shahar nomini to'g'ri kiriting \nMasalan(xiva=khiva,xonqa=khonqa)")