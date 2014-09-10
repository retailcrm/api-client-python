from Intaro import IntaroApy
from pprint import pprint

i = IntaroApy('https://g-lights.intarocrm.ru', 'pPsg3F79dj0OYkeYKwogOT9cccaipIKR')

result = i.orderGet(1342)

pprint(result)
