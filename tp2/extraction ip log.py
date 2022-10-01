# -*- coding: utf-8 -*-

#lecture du fichier de log
#Extraction des IP
#Geolocalisation des IP
#Classification des IP

import pygeoip

from OTXv2 import OTXv2
import argparse
import get_malicious
import hashlib

import json

#Récupérer la liste de toute les ip (on stocke une seule fois chaque ip)
listIp = []
ips = []
file = open("logs.test.txt", 'r')
line = file.readline()
while line:
    ip = line.split(' ', 1)[0]
    if(ip not in listIp):
        listIp += [ip]
        obj = {}
        obj["ip"] = ip
        ips += [obj]
    line = file.readline()
file.close()

#Géolocaliser les ip
#geoip = pygeoip.GeoIP("GeoLiteCity.dat", pygeoip.MEMORY_CACHE)
gi = pygeoip.GeoIP('GeoLiteCity.dat', pygeoip.MEMORY_CACHE)
API_KEY = '7930f37d7c2aa67ba24aa55174ba487632b5baa2a587b22ac61603b7e581b111'
OTX_SERVER = 'https://otx.alienvault.com/'
otx = OTXv2(API_KEY, server=OTX_SERVER)
for obj in ips:
    ip = obj['ip']
    #print(gi.record_by_addr(obj['ip'])['longitude'])
    info = gi.record_by_addr(obj['ip'])
    if(info != None): #Certaines ip n'ont pas de correspondance dans la bdd
        obj['latitude'] = info['latitude']
        obj['longitude'] = info['longitude']
        ### Malocious (on le récupère que si on récupère aussi les coordonnées)
        #alerts = get_malicious.ip(otx, obj['ip'])
        #if len(alerts) > 0:
        #    obj['malicious'] = True
        #else:
        #    obj['malicious'] = False

#print(ips)

### stocker les résultats ###
j = json.dumps(ips)
print(j)

file = open("save.json", 'w')
file.write("data = '" + j +"';")
file.close()