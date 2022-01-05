import requests
import json
import shutil
import os
pip=requests.get('https://ipinfo.io/ip').text
d=json.loads(requests.get('https://ipinfo.io/'+pip).text)
s=d['city']
s=s.replace(" ","")
f=open("f","w") 
f.write(d['city'])
f.close()
t=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+s+'&APPID=1d546279fd1cf542d882b5a1de752f36&units=metric').text
v=json.loads(t)
f=open("t","w")
f.write(str((v['main']['temp']))[:-1])
f.close()
s=v['weather'][0]['icon']+'.png'
home=os.path.expanduser('~/')
s=home+'.iconos/'+s
shutil.copyfile(s,home+'/.cache/weather.png')


