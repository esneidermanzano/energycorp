import datetime
import random
from energytransfers.models import Counter, History

data = {
    "name": 0,
    "address": 0,
    "identification": 0,
    "payMonth":1,
    "rangeBilling": 1,
    "days":0,
    "deadDatePay": 1,
    "stratum": 1,
    "counter":1,
    "currentRecord":1,
    "pastRecord":1,
    "difference":0,
    "basicTake": 1,
    "remainder": 1,
    "interest": 1,
    "totalBasic": 1,
    "totalRemainder":1,
    "subsidy": 1,
    "totalBasicSubsidy": 1,
    "total": 1,
    "contract":0,
    "reference": 1,
    "intakes": 1

}
def generateHistory():
    contadores = Counter.objects.filter(is_active=True).values('codeCounter', 'value')
    for counter in contadores:
        history = History.objects.filter(
            counter=counter['codeCounter']).order_by('-codeHistory').values('current')[:1]
        print(history)

    print(contadores)

def generateInvoice(query):
    data['name'] = query['client']['user']['name']
    data['address'] = query['counter']['addressCounter']
    data['identification'] = query['client']['user']['id_user']

    finalRecordDate = query['counter']['historys'][0]['registryHistory']
    frdate = datetime.datetime.strptime(finalRecordDate,'%Y-%m-%d')
    payMonth = frdate + datetime.timedelta(days=10)

    data['payMonth'] = payMonth.strftime("%B-%Y")
    data['rangeBilling'] =frdate.replace(day=1).strftime('%b-%d') +" a " + frdate.strftime('%b-%d')
    data['days'] = frdate.strftime('%d')
    data['deadDatePay'] = payMonth.strftime("%b-%d-%Y")
    data['stratum'] = query['counter']['stratum']
    data['counter'] = query['counter']['codeCounter']
    data['currentRecord'] = query['counter']['historys'][0]['consumption']
    data['pastRecord'] = query['counter']['historys'][1]['consumption']
    data['difference'] = data['currentRecord'] - data['pastRecord']
    
    basic = 173
    if data['difference'] > basic:
        data['basicTake'] = basic
        data['remainder'] = data['difference'] - basic
    else:
        data['basicTake'] = data['difference']
        data['remainder'] = 0
    
    unitaryValue = 598
    data['interest'] = query['client']['interes_mora']
    data['totalBasic'] = data['basicTake']*unitaryValue
    data['totalRemainder'] = data['remainder']*unitaryValue

    subsidyValue = 0

    if data['stratum'] == 1:
        subsidyValue = 0.6
    elif data['stratum'] == 2:
        subsidyValue = 0.5
    elif data['stratum'] == 3:
        subsidyValue = 0.15
    else:
        subsidyValue = 0
    
    data['subsidy'] = -data['totalBasic']*subsidyValue
    data['totalBasicSubsidy'] = data['totalBasic'] + data['subsidy']

    data['total'] = data['totalBasicSubsidy'] + data['totalRemainder']
    data['contract'] = query['contractNumber']

    now = datetime.datetime.now()
    code = str(now).replace(':', '').replace('.', '').replace('-','').split()
    reference = code[0] + "("+ code[1]+")"+ str(random.randint(1111111,9999999))

    data['reference'] = reference

    intakes = []

    for history in query['counter']['historys']:
        month = datetime.datetime.strptime(history['registryHistory'],'%Y-%m-%d')
        month = month.strftime('%B')
        reading = history['consumption']
        intakes.append([{"month":month}, {"reading": reading}])
    data['intakes'] = intakes

    generateHistory()
    return data
