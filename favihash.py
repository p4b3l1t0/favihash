#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Autor:   Pablo Salinas
# Linkedin: https://www.linkedin.com/in/00011001/
# Nota:     Usarlo bajo responsabilidad
# Licencia:  MIT License (http://www.opensource.org/licenses/mit-license.php)
# Version : 1.0

from importlib.resources import path
import mmh3
import requests
import codecs

def banner():
    print(
"""
  ___                _  _                   _     
 / __)              (_)| |                 | |    
| |__   ____  _   _  _ | | _    ____   ___ | | _  
|  __) / _  || | | || || || \  / _  | /___)| || \ 
| |   ( ( | | \ V / | || | | |( ( | ||___ || | | |
|_|    \_||_|  \_/  |_||_| |_| \_||_|(___/ |_| |_|
                    </coded by Pablo Salinas>                     
""")
    
banner()

domain = input("please insert the domain or IP: \n")

def readDomain():
    try:
        url = 'https://{}/favicon.ico'.format(domain)
        response = requests.get(url)
        favicon = codecs.encode(response.content,"base64")
        hash = mmh3.hash(favicon)
        print("This is the shodan URL to search more assets: https://beta.shodan.io/search?query=http.favicon.hash%3A{}\n".format(hash))
        print(url)
    except Exception:
        print("Favicon hash endpoint not found")
readDomain()
