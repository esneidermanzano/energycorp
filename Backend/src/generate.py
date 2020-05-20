import json
import random
import math
import geopy.distance
import datetime

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
            "interes_mora": 0
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
    [3.4613754609402134, -76.50162220001222],
    [3.463560148219834, -76.49715900421144],
    [3.468572058805507, -76.50488376617432],
    [3.4810374646865485, -76.49346828460695],
    [3.488105405079248, -76.49904727935792],
    [3.4357371374880414, -76.5101408958435],
    [3.437086540149677, -76.504282951355],
    [3.4278120357529867, -76.4970088005066],
    [3.4380932361303143, -76.49919748306276],
    [3.4223072642741497, -76.50091409683229]
]

countdir = [
    'Carrera 5 # 14-4',
    'Carrera 5 con calle 56',
    'Carrera 2 # 45',
    'Calle 66A #43',
    'Calle 71 #42',
    'Carrera 24 #4B',
    'Carrera 24C #10',
    'Carrera 28B #9',
    'Carrera 25 #33-17',
    'Carrera 29A #12-89'
]

transformador = [9, 9, 9, 10, 10, 6, 6, 5, 6, 5]
stratos = [1,3,2,6,4, 4, 3,3,5,4]
counters = []

for i in range (1, 11):
    counter = {
        "model": "energytransfers.counter",
        "pk": i,
        "fields": {
            "latitudeCounter": str(countercoors[i-1][0]),
            "lengthCounter": str(countercoors[i-1][1]),
            "value": random.randint(1000, 2000),
            "is_active": True,
            "addressCounter": countdir[i-1],
            "stratum": stratos[i-1],
            "clientCounter": i,
            "transformatorCounter": transformador[i-1]
        }
    }
    counters.append(counter)

basejson.extend(counters)

histories = []
rand1 = [0.17, 0.15, 0.24, 0.18, 0.26]
rand2 = [0.20, 0.15, 0.24, 0.19, 0.22]
fechas = ['2019-12-31', '2020-01-31', '2020-02-29', '2020-03-31', '2020-04-30']
pesos = []
for i in range (1, len(counters) + 1):
    totalcurrent = 0
    if i%2==0:
        random.shuffle(rand1)
        pesos = rand1
    else:
        random.shuffle(rand2)
        pesos = rand2

    for j in range (1, 6):
        consumption = math.floor(pesos[j-1]*counters[i-1]['fields']['value'])
        totalcurrent = totalcurrent + consumption
        current  = totalcurrent 
        history = {
            "model": "energytransfers.history",
            "pk": (i-1)*5 + j,
            "fields": {
                "current": current,
                "consumption": consumption,
                "registryHistory": fechas[j-1],
                "counter": i
            }
        }
        histories.append(history)

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

for i in range (1, len(counters)+1):
    contract = {
        "model": "contract.contract",
        "pk": 20200514 + i,
        "fields": {
            "client": i,
            "counter": i
        }
    }
    contracts.append(contract)

basejson.extend(contracts)

invoices = []

for i in range (1, len(counters) + 1):
    pastRecord = 0
    anterior=0
    intakes =[]
    for j in range (1,6):
        date = datetime.datetime.strptime(fechas[j-1],'%Y-%m-%d')
        deadDate = date + datetime.timedelta(days=10)
        deadDate.strftime("%Y-%m-%d")
        deadDate=str(deadDate).split(" ")[0]
        current = histories[(i-1)*5 + j - 1]['fields']['current']
        pastRecord=anterior
        consumo = histories[(i-1)*5 + j - 1]['fields']['consumption']
        basic = 173
        basicTake = 0  
        remainder=0
        if consumo > basic:
            basicTake = basic
            remainder = consumo - basic
        else:
            basicTake = consumo

        intakes.insert(0,str(date.month)+"-"+str(consumo))
        intk = ','.join(intakes)
        
        subsidyValue = 0
        stratum = stratos[i-1]
        if stratum == 1:
            subsidyValue = 0.6
        elif stratum == 2:
            subsidyValue = 0.5
        elif stratum == 3:
            subsidyValue = 0.15
        else:
            subsidyValue = 0
        
        totalBasicSubsidy = (1-subsidyValue)*basicTake

        total = (totalBasicSubsidy + remainder)*589

        invoice = {
            "model": "contract.Invoice",
            "pk": 2000+(i-1)*5 + j,
            "fields": {
                "billingDate": fechas[j-1],
                "deadDatePay": deadDate,
                "consumptiondaysInvoice": str(date.day),
                "counter": i,
                "address": countdir[i-1],
                "stratum": stratum,
                "currentRecord": current,
                "pastRecord": pastRecord,
                "basicTake": basicTake,
                "remainder": remainder,
                "unitaryValue": 589,
                "interestMora": 0,
                "totalMora": 0.0,
                "overdue": 0.0,
                "intakes": intk,
                "referencecodeInvoice": "202004301759"+str(random.randint(111,999))+"26153" + str(random.randint(1111111,9999999)),
                "total": total,
                "stateInvoice": True,
                "contract": 20200514 + i
            }
        }
        invoices.append(invoice)
        anterior=current

    #now = datetime.now()
    #code = str(now).replace(':', '').replace('.', '').replace('-','').split()
    #reference = code[0] + "("+ code[1]+")"+ str(random.randint(1111111,9999999))

    
basejson.extend(invoices)

payments = []

for i in range (1,len(invoices)+1):
    date = datetime.datetime.strptime(invoices[i-1]['fields']['billingDate'],'%Y-%m-%d')
    datePayment = date + datetime.timedelta(days=random.randint(1,9))
    datePayment.strftime("%Y-%m-%d")
    datePayment=str(datePayment).split(" ")[0]
    pay = {
        "model": "payments.payment",
        "pk": 40050+i,
        "fields": {
            "valuePayment": invoices[i-1]['fields']['total'],
            "datePayment": datePayment,
            "facturaPayment": 2000+i
        }
    }
    payments.append(pay)


basejson.extend(payments)


jsonData=json.dumps(basejson, ensure_ascii=False)



print(jsonData)

#========================== FIN generate clientes ================================
