''' This code uses opennotify api to display number of persons present in iss at present and their name,the current location(latitude,longitude) of iss and time at which it
will pass over my current location
'''
import requests
import  json
from requests import get
from datetime import datetime

#open-notify respons
res=get("http://api.open-notify.org/astros.json")
#print(res.status_code)

#stores json 
result=res.json()
#converting json to strings
print('total number of persons in space at present:',result['number'])
print('They are:')
for i in range (result['number']):
    print('craft name:',result['people'][i]['craft'])
    print('name:',result['people'][i]['name'],'\n')

#current position of iss
res3=get('http://api.open-notify.org/iss-now.json')
result3=res3.json()
print('curent time:',datetime.fromtimestamp(result3['timestamp']))
print('iss_position_latitude:',result3['iss_position']['latitude'])
print('iss_position_longitude:',result3['iss_position']['longitude'])
print('http://www.google.com/maps/place/',result3['iss_position']['latitude'],',',result3['iss_position']['longitude'])
print('\n')

#pass time over current location
p={'lat':22.6670,'lon':88.3796} #location of my place
res2=get("http://api.open-notify.org/iss-pass.json",params=p)
result2=res2.json()
print('info about given coordinates')
print('altitude of place:',result2['request']['altitude'])
print('latitude of place:',result2['request']['latitude'])
print('longitude of place:',result2['request']['longitude'])
print('passes over',result2['request']['passes'],'times in a day')
print('The times are:')
rtime=result2['response']
for rt in rtime:
    print(datetime.fromtimestamp(rt['risetime']))
