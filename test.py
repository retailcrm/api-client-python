import os
import sys
import inspect
import json

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path: sys.path.insert(0, cmd_folder)

cmd_subfolder = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "subfolder")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

from retailcrm import Client

url = 'https://crm_name.retailcrm.ru'
key = 'api_key'

crm = Client(url, key)

result = crm.deliveryServicesList()

print json.dumps(result)
