import json
import random
import math
import geopy.distance
from datetime import datetime

from geopy.geocoders import Nominatim
from django.contrib.auth.hashers import make_password

basejson = []
#========================== generate clientes ================================
a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
trans = str.maketrans(a,b)
names= [
    "Cristóbal Cero Buedo",
    "Cecilia Urquijo Barma",
    "Teófilo Egusquiza Madariaga",
    "Pancracio Ispuzua Chave",
    "Celeste Ganzo Vicente",
    "Luis Valino Vango",
    "Florencia Cucho Ahedo",
    "Mariano Mogrovejo Gante",
    "Angélica Ter Tosantos",
    "Antonio Incera Fontoria",
    "Lupita Soret Garmendia",
    "Sayana Villarruel Saga",
    "Laila Herriaga Herreria",
    "Leví Encinas Durana",
    "Wendy Brena Suane",
    "Celia Malmonje Buyeres",
    "Reinaldo Maja Matuta",
    "Telesforo Rico Colombres",
    "Leonela Suane Ayuso",
    "Mariela Brasa Collazos",
    "Patricia Sesmilo Aranda",
    "Maribel Urizar Castañiza",
    "Aleyda Valverde Villena",
    "Erinelva Revuelta Ribero",
    "Nayade Artadi Urquijo",
    "Adam Idigoras Faes",
    "Máximo Corrales Balaunde",
    "Isaí Hita Carrera",
    "Juan Forcelledo Bodes",
    "Nicole Rioz Millares",
    "Yasnin Cedron Grandas",
    "Yosniel Estancion Cospedal",
    "América Rayon Sereno",
    "Adelaida Carces Surco",
    "Danila Torienzo Piñeiros",
    "Jordana Charlo Jara",
    "Felisa Senabres Brochero",
    "Pamela Briñas Telego",
    "Jeronimo Villarragut Bullido",
    "Salomé Lejobeitia Courel",
    "Marlon Avalos Marentos",
    "Amanda Marote Mortal",
    "Mariela Pablo Palma",
    "Marina Hernaez Iñarra",
    "Leonela Azcoitia Poladura",
    "Wenceslao Verga Maria",
    "Nieves Estua Galdia",
    "Faustino Candolias Jalon",
    "Argelia Cifontes Lasarte",
    "Aaron Davila Landeta",
    "Willy Jubitero Ayarza",
    "Sabine Taran Inguanzo",
    "Bradley Bispo Valdecañas",
    "Natali Chumacero Folgar",
    "Lasset Santotis Bernabeytia",
    "Jacinto Tablares Pico",
    "Aique Monterrey Ordoñez",
    "Carmela Catalan Roman",
    "Eugenio Arindez Cruz",
    "Adrián Villajane Porlier",
    "Sabrina Argandoña Agudo",
    "Crispín Corneja Argos",
    "Joel Espantoso Duran",
    "Gilda Alcivia Rubio",
    "Jade Vidaurre Negro",
    "Ricardo Briceño Marcha",
    "Naylu Amilburu Angeriz",
    "Yadira Villamediana Toro",
    "Sabrina Mancobo Barcaiztegui",
    "David Nurueña Pizaño",
    "Silvia Cardeiro Olavarria"
]

barrios =[
    'Aguablanca',
    'Belen',
    'Calipso',
    'Calima',
    'Eduardo Santos',
    'El vergel',
    'Sindical',
    'Manuela Beltran',
    'Potrero Grande',
    'Llano verde',
    'Mojica',
    'Marroquin',
    'El Retiro',
    'El vallado',
    'El bronx',  
    'Los Robles'  
]

ncalle = [
    'Calle',
    'Carrera',
    'Transversal',
    'Diagonal',
    'Avenida',
]

nncalle = ['A', 'B', 'C', 'D', 'E']
mails = ['gmail', 'yahoo', 'hotmail']
users = []
clients= []

for i in range (1,11):
    name = names[i]
    fname = name.split()[0].translate(trans)
    user ={
        "model": "users.CustomUser",
        "pk": i,
        "fields": {
            "id_user": str(random.randint(111111111,1144999999)),
            "name": name,
            "email": fname + "@"+random.choice(mails)+".com",
            "password": make_password(fname + str(len(fname))),
            "phone": str(random.randint(3000000,4999999)),
            "address": random.choice(ncalle) +" "+ str(random.randint(1,99)) + random.choice(nncalle) + " # " + str(random.randint(1,99)) + " - " + str(random.randint(10,200)),
            "neighborhood": random.choice(barrios),
            "stratus": random.randint(2,6),
            "is_active": True,
            "is_staff": False,
            "is_superuser": False    
        }
    }
    client ={
        "model": "users.Client",
        "pk": i,
        "fields": {
            "user": i,
            "type_client": 1,
            "interes_mora": 0,
            "cycle": "1",
            "financial_state": "libre",
            "billing": "no se",
        }
    }    
    users.append(user)
    clients.append(client)

#============================== trabajadores =======================

workers = [
{
  "model": "users.CustomUser",
  "pk": 11,
  "fields": {
    "id_user": "1144189914",
    "name": "Esneider Manzano",
    "email": "esneider@gmail.com",
    "password": "pbkdf2_sha256$180000$W4DSmgbKj7dK$s6p1mSZZ7bhhcbaKuQxpXLN8QP03eGULkW9/Rd+819w=",
    "phone": "4455971",
    "address": "cra28 C # 54-123",
    "neighborhood": "sindical",
    "stratus": 2,
    "is_active": True,
    "is_staff": True,
    "is_superuser": False    
  }
},
{
  "model": "users.CustomUser",
  "pk": 12,
  "fields": {
    "id_user": "1144189915",
    "name": "Luis de Huevosalva",
    "email": "luis@gmail.com",
    "password": "pbkdf2_sha256$180000$W4DSmgbKj7dK$s6p1mSZZ7bhhcbaKuQxpXLN8QP03eGULkW9/Rd+819w=",
    "phone": "4455972",
    "address": "cra28 C # 54-124",
    "neighborhood": "sindical",
    "stratus": 2,
    "is_active": True,
    "is_staff": True,
    "is_superuser": False
  }
},
{
    "model": "users.CustomUser",
    "pk": 13,
    "fields": {
        "id_user": "1144189910",
        "name": "Taborda",
        "email": "taborda@gmail.com",
        "password": "pbkdf2_sha256$180000$W4DSmgbKj7dK$s6p1mSZZ7bhhcbaKuQxpXLN8QP03eGULkW9/Rd+819w=",
        "phone": "4455970",
        "address": "cra28 C # 54-127",
        "neighborhood": "sindical",
        "stratus": 2,
        "is_active": True,
        "is_staff": True,
        "is_superuser": False
    }
  },
{
    "model": "users.Worker",
    "pk": 1,
    "fields": {
        "user": 11,
        "user_type": 1
    }
},
{
    "model": "users.Worker",
    "pk": 2,
    "fields": {
        "user": 12,
        "user_type": 2
    }
},
{
    "model": "users.Worker",
    "pk": 3,
    "fields": {
        "user": 13,
        "user_type": 3
    }
}
]
users.extend(workers)
users.extend(clients)

basejson.extend(users)
#============================== energytrasfer ======================
subcoor = [
    [3.372908, -76.532479], 
    [3.428119, -76.479726],
    [3.425783, -76.508505],
    [3.456173, -76.532861],
    [3.467536, -76.495797]
]
substations = []
for i in range (1,len(subcoor)+1):
    substation = {
        "model": "energytransfers.substation",
        "pk": i,
        "fields": {
            "latitudeSubstation": str(subcoor[i-1][0]),
            "lengthSubstation": str(subcoor[i-1][1]),
            "is_active": True
        }
    }
    substations.append(substation)
    
basejson.extend(substations)

transcoor = [
    [3.395716, -76.548220], 
    [3.380439, -76.544490],
    [3.426220, -76.480782],
    [3.418405, -76.471679],
    [3.427807, -76.500480],
    [3.433637, -76.504623],
    [3.448340, -76.538648],
    [3.448628, -76.523636],
    [3.465657, -76.500669],
    [3.484713, -76.497644]
]
ransformators = []
number = 1
for i in range (1,len(transcoor)+1):
    transformator = {
        "model": "energytransfers.transformator",
        "pk": i,
        "fields": {
            "latitudeTransformator": str(transcoor[i-1][0]),
            "lengthTransformator": str(transcoor[i-1][1]),
            "is_active": True,
            "substationTransformator": math.ceil(i/2)
        }
    }
    ransformators.append(transformator)

basejson.extend(ransformators)

countercoors = [
    #transf 1
    [3.429708, -76.501172],
    [3.429556, -76.504896],
    [3.428764, -76.506723],
    [3.430769, -76.508757],
    [3.437480, -76.508385],

    #transf2
    [3.470128, -76.490096],
    [3.462938, -76.504564],
    [3.459106, -76.487694],
    [3.475513, -76.501320],
    [3.471357, -76.498292]
]

countdir = [
    'Cra. 28c #50-2 a 50-178',
    'Tv. 33g #28e-2 a 28e-64',
    'Dg. 28d #29-2 a 29-96',
    'Tv. 28a #27a-89 a 27a-1',
    'Cl. 33f #23-12 a 23-64',

    'Cl. 64a #2d-39 a 2d-1',
    'Cl. 46 #4b-8 a 4b-28',
    'Cra. 7f #64-65 a 64-1',
    'Cra. 1B #5450',
    'Cra. 1d 2 #56-94'
]
counters = []

for i in range (1, 11):
    number = 1
    if i > 5:
        number = 2
    counter = {
        "model": "energytransfers.counter",
        "pk": i,
        "fields": {
            "latitudeCounter": str(countercoors[i-1][0]),
            "lengthCounter": str(countercoors[i-1][1]),
            "value": random.randint(100, 500),
            "is_active": True,
            "addressCounter": countdir[i-1],
            "clientCounter": i,
            "transformatorCounter": number
        }
    }
    counters.append(counter)

basejson.extend(counters)


histories = []

for i in range (1, len(counters) + 1):
    history1 = {
        "model": "energytransfers.history",
        "pk": i*2 - 1,
        "fields": {
            "consumption": random.randint(10,50),
            "counter": i,
            "registryHistory": "2020-04-30"
        }
    }
    history2 = {
        "model": "energytransfers.history",
        "pk": i*2,
        "fields": {
            "consumption": random.randint(10,50),
            "counter": i,
            "registryHistory": "2020-05-13"
        }
    }
    
    histories.append(history1)
    histories.append(history2)

basejson.extend(histories)
"""
geolocator = Nominatim(user_agent="geogenerator")
for i in range (len(countercoors)):
    location = geolocator.reverse(countercoors[i])
    print(location.address)
"""
"""
coors3 = (3.471357, -76.498292)
for i in range (len(transcoor)):
    print (geopy.distance.vincenty(tuple(transcoor[i]), coors3).km)
"""

#================================ INVOICES ========================

contracts = []

for i in range (1, len(counters+1)):
    contract = {
        "model": "contract.contract",
        "pk": i,
        "fields": {
            "client": i,
            "counter": i
        }
    }

invoices = []

for i in range (1, len(counters) + 1):
    invoice1 = {
        "model": "contract.Invoice",
        "pk": i*2 - 1,
        "fields": {
            "consumptiondaysInvoice": 30,
            "paymentdeadlineInvoice": "2020-05-05",
            "billingdateInvoice": "2020-04-30",
            "stateInvoice": True,
            "referencecodeInvoice": "20200430(175915326153)" + str(random.randint(1111111,9999999)),
            "total": 130000,
            "client": i,
            "history": i*2 - 1
        }
    }
    now = datetime.now()
    code = str(now).replace(':', '').replace('.', '').replace('-','').split()
    reference = code[0] + "("+ code[1]+")"+ str(random.randint(1111111,9999999))

    invoice2 = {
        "model": "contract.Invoice",
        "pk": i*2,
        "fields": {
            "consumptiondaysInvoice": 13,
            "paymentdeadlineInvoice": "2020-05-15",
            "billingdateInvoice": "2020-05-13",
            "stateInvoice": False,
            "referencecodeInvoice": reference,
            "total": 70000,
            "client": i,
            "history": i*2
        }
    }
    
    invoices.append(invoice1)
    invoices.append(invoice2)
    
basejson.extend(invoices)

payments = []

for i in range (1,11):
    pay = {
        "model": "payments.payment",
        "pk": i,
        "fields": {
            "valuePayment": 130000,
            "datePayment": "2020-05-01T01:53:37.426Z",
            "facturaPayment": i*2 - 1
        }
    }
    payments.append(pay)


basejson.extend(payments)


jsonData=json.dumps(basejson, ensure_ascii=False)



print(jsonData)

#========================== FIN generate clientes ================================
