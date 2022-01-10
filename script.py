import requests
import json
import shutil
import os
home=os.path.expanduser('~/')
pip=requests.get('https://ipinfo.io/ip').text
d=json.loads(requests.get('https://ipinfo.io/'+pip).text)
s=d['city']
s=s.replace(" ","")
f=open(home+".conky/f","w") 
f.write(d['city'])
f.close()
t=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+s+'&APPID=1d546279fd1cf542d882b5a1de752f36&units=metric').text
v=json.loads(t)
f=open(home+".conky/t","w")
f.write(str((v['main']['temp']))[:-1])
f.close()
s=v['weather'][0]['icon']+'.png'
s=home+'.iconos/'+s
shutil.copyfile(s,home+'/.cache/weather.png')

