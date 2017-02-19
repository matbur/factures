#!/usr/bin/env python

import requests

base = 'http://127.0.0.1:8000/'
contractors = base + 'contractors/'
invoices = base + 'invoices/'
lines = base + 'lines/'

data = (
    (contractors, {
        'name': 'matbur & sons',
        'address1': 'avenue',
        'address2': 'wroclaw',
        'NIP': '0000000017',
    }),
    (invoices, {
        'date': '2017-01-23',
        "issuer": contractors + '17/',
        "receiver": contractors + '2/',
    }),
    (lines, {
        'invoice': invoices + '65/',
        'description': 'pro1',
        'price': 5.66,
        'amount': 1,
        'tax': 100,
    }),
    (lines, {
        'invoice': invoices + '65/',
        'description': 'pro2',
        'price': .66,
        'amount': 23,
        'tax': 10,
    }),
)

for link, content in data:
    p = requests.post(link, data=content)
    print(p)
    print(p.text)

r = requests.get(invoices + '65/')
print(r)
print(r.text)
