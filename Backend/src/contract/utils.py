import datetime
import random
from .models import Contract, Invoice
from .serializers import ContractSerializer
from energytransfers.models import Counter, History
import json

def generateHistoryAndInvoices():
    contratos = Contract.objects.all()
   
    histories = []
    invoices = []
    for contrato in contratos:
        
        currentRegistry = contrato.counter.value
        lastRegistry = History.objects.filter(
            counter=contrato.counter).order_by('-codeHistory').values('current')[:1][0]['current']
        consumo = currentRegistry-lastRegistry

        lastInvoice = Invoice.objects.filter(
            contract=contrato).order_by('-codeInvoice').values(
                'overdue', 'intakes', 'deadDatePay', 'total', 'stateInvoice'
                )[:1][0]
        
        histories.append(History(
                current=currentRegistry,
                consumption=consumo,
                counter=contrato.counter
            )
        )
        
        billingDate = datetime.datetime.now()

        deadDate = billingDate + datetime.timedelta(days=10)
        deadDatePay = deadDate.strftime("%Y-%m-%d")
        counter = contrato.counter.codeCounter
        address = contrato.counter.addressCounter
        stratum = contrato.counter.stratum

        basicTake = 0
        remainder = 0
        unitaryValue = 589
        interestMora = 0
        totalMora = 0
        overdue = 0

        #================ necessary to total calcule ===============
        basic = 173
        if consumo > basic:
            basicTake = basic
            remainder = consumo - basic
        else:
            basicTake = consumo

        totalBasic = basicTake*unitaryValue
        totalRemainder = remainder*unitaryValue
        subsidyValue = 0
        if stratum == 1:
            subsidyValue = 0.6
        elif stratum == 2:
            subsidyValue = 0.5
        elif stratum == 3:
            subsidyValue = 0.15
        else:
            subsidyValue = 0
        
        totalBasicSubsidy = (1-subsidyValue)*totalBasic

        #=============== ESTA MOROSO ============
        if contrato.client.interes_mora != 0:
            interestMora = contrato.client.interes_mora
            totalMora = lastInvoice['total']*interestMora

        #================ Factura pendiente =========
        if not lastInvoice['stateInvoice']:
            overdue = lastInvoice['total']

        total = totalBasicSubsidy + totalRemainder + totalMora +overdue
        #================ necessary to total calcule ===============       

        intakes = lastInvoice['intakes'].split(",")
        combo = billingDate.month
        combo = str(combo) + "-" + str(consumo)

        if len(intakes) > 5:    
            del intakes[-1]
                            
        intakes.insert(0, combo)
        intakes = ','.join(intakes)

        code = str(billingDate).replace(':', '').replace('.', '').replace('-','').replace(' ', str(random.randint(1,9)))
        referencecodeInvoice = code + str(random.randint(1111111,9999999))

        invoices.append(Invoice(
                    billingDate=billingDate,
                    deadDatePay=deadDatePay,
                    counter=counter,
                    address=address,
                    stratum=stratum,
                    currentRecord=currentRegistry,
                    pastRecord=lastRegistry,
                    basicTake=basicTake,
                    remainder=remainder,
                    unitaryValue=unitaryValue,
                    interestMora=interestMora,
                    totalMora=totalMora,
                    overdue=overdue,
                    intakes=intakes,
                    referencecodeInvoice=referencecodeInvoice,
                    total=total,
                    contract=contrato
                )
            )

    History.objects.bulk_create(histories)
    Invoice.objects.bulk_create(invoices)



def getInvoiceData(query):
    data = {
        "name": "",
        "id_user": "",
        "payMonth": "",
        "rangeBilling": "",
        "days":"",
        "cutoffDate":"",
        "deadDatePay": "",
        "counter":0,
        "address": "",
        "stratum": 0,
        "currentRecord":0,
        "pastRecord":0,
        "difference":0,
        "basicTake": 0,
        "remainder": 0,
        "unitaryValue":0,
        "interestMora": 0,
        "totalMora": 0,
        "overdue": 0,
        "totalBasic": 0,
        "totalRemainder":0,
        "subsidy": 0,
        "totalBasicSubsidy": 0,
        "total": 0,
        "contract":"",
        "referencecodeInvoice": "",
        "intakesMonth": [],
        "intakesConsu": []

    }
    meses = [
        "Ene", "Feb", "Mar", 
        "Abr", "May", "Jun", 
        "Jul", "Ago", "Sep", 
        "Oct", "Nov", "Dic"
    ]
    meses2 = [
        "Enero", "Febrero", "Marzo", 
        "Abril", "Mayo", "Junio", 
        "Julio", "Agosto", "Septiembre", 
        "Octubre", "Noviembre", "Diciembre"
    ]

    data['name'] = query['client']['user']['name']
    data['id_user'] = query['client']['user']['id_user']
    
    frdate = query['invoice']['billingDate']
    frdate = datetime.datetime.strptime(frdate,'%Y-%m-%d')
    aux = frdate+datetime.timedelta(days=10)

    data['payMonth'] = meses2[int(aux.strftime('%m'))-1] + " " + aux.strftime('%Y')
    data['rangeBilling'] = frdate.replace(day=1).strftime('%m-%d') +" a " + frdate.strftime('%m-%d')
    data['days'] = frdate.day
    data['cutoffDate'] = query['invoice']['billingDate']
    data['deadDatePay'] = query['invoice']['deadDatePay']
    data['counter'] = "C2AA_"+str(query['invoice']['counter'])
    data['address'] = query['invoice']['address']
    data['stratum'] = query['invoice']['stratum']
    data['currentRecord'] = query['invoice']['currentRecord']
    data['pastRecord'] = query['invoice']['pastRecord']
    data['difference'] = data['currentRecord'] - data['pastRecord']
    data['basicTake'] = query['invoice']['basicTake']
    data['remainder'] = query['invoice']['remainder']
    data['unitaryValue'] = query['invoice']['unitaryValue']
    data['interestMora'] = query['invoice']['interestMora']
    data['totalMora'] = query['invoice']['totalMora']
    data['overdue'] = query['invoice']['overdue']
    data['totalBasic'] = data['basicTake']*data['unitaryValue']
    data['totalRemainder'] = data['remainder']*data['unitaryValue']
    
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
    data['total'] = '%.2f' % query['invoice']['total']
    data['contract'] = query['invoice']['contract']
    data['referencecodeInvoice'] = query['invoice']['referencecodeInvoice']


    intakes = query['invoice']['intakes'].split(",")

    for intake in intakes:
        aux = intake.split("-")
        data['intakesMonth'].append(meses[int(aux[0])-1])
        data['intakesConsu'].append(aux[1])

    return data
