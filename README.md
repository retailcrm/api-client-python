api-client-python
=================

RetailCrm REST API client (python version)

##Setup

```
git clone https://github.com/retailcrm/api-client-python.git
cd api-client-python
pip install requests
python setup.py install
```

##Usage

```python
from retailcrm import Client


crm = Client('https://demo.intarocrm.ru', 'uLxXKBwjQteE9NkO3cJAqTXNwvKktaTc')

order = {
  'firstName': 'Ivan',
  'lastName': 'Ivanov',
  'phone': '+79000000000',
  'email': 'ivan@example.com',
  'orderMethod': 'call-request',
}

result = crm.orderCreate(order)
```
