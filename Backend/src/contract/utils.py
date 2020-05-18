import datetime

data = {
    "name": 0,
    "address": 0,
    "identification": 0,
    "payMonth":1,
    "rangeBilling": 1,
    "days":0,
    "cycle": 0,
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
    "reference": 1

}

def generateInvoice(query):
    data['name'] = query['client']['user']['name']
    data['address'] = query['counter']['addressCounter']
    data['identification'] = query['client']['user']['id_user']

    finalRecordDate = query['counter']['historys'][0]['registryHistory']
    frdate = datetime.datetime.strptime(finalRecordDate,'%Y-%m-%d')
    payMonth = frdate + datetime.timedelta(days=10)

    data['payMonth'] = payMonth.strftime("%b-%Y")
    data['rangeBilling'] =frdate.replace(day=1).strftime('%m-%d') +" a " + frdate.strftime('%m-%d')
    data['days'] = frdate.strftime('%d')
    data['deadDatePay'] = payMonth.strftime("%b-%d-%Y")
    return data
