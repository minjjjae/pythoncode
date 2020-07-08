import json

customer = {
    'id':152352,
    'name':'강진수',
    'history':[
        {'date': '2015-03-11', 'item':'iPhone'},
        {'datd': '2020-07-03', 'item': 'Monitor'},
    ]
}

with open('./basic/02_if_for/data.json', 'wt') as f:
    json.dump(customer, f,indent=4)
