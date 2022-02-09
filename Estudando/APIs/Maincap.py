from urllib import request
from Acessocep import Acessocep
import requests


cep = 63400000
obj_cep = Acessocep(cep)
print(obj_cep)


r = requests.get("https://viacep.com.br/ws/01001000/json/")
print(r)
