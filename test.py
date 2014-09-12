from Intaro import IntaroApy

# copy-one.ru
crm = IntaroApy('https://copy-one.intarocrm.ru', 'Yogg9w7pxDW6sS3yESXljKpSueTJVURW')

# copy-galaxys5
#crm = IntaroApy('https://copy-one.intarocrm.ru', 'zpbJiKQEFEo9OlpEebM8OATs5t7dzgjB')

# Pulwin
#crm = IntaroApy('https://copy-one.intarocrm.ru', 'Lx2W5QRy6lQUotkaLd1cAXYRPIG4SdhR')

order = {
    'firstName': 'TESTER',
    'phone': '89991119922',
    'orderMethod': 'landing-page'
  }

result = crm.orderCreate(order)

