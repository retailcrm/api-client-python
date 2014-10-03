from Intaro import IntaroApy

crm = IntaroApy('hhttps://demo.intarocrm.ru', 'uLxXKBwjQteE9NkO3cJAqTXNwvKktaTc')

order = {
    'firstName': 'Intaro Test',
    'phone': '+79000000000',
    'orderMethod': 'landing-page'
}

result = crm.orderCreate(order)
