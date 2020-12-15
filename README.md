[![Build Status](https://img.shields.io/travis/retailcrm/api-client-python/master.svg)](https://travis-ci.org/retailcrm/api-client-python)
[![Coverage](https://img.shields.io/codecov/c/gh/retailcrm/api-client-python/master.svg?logo=codecov&logoColor=white)](https://codecov.io/gh/retailcrm/api-client-python)
[![PyPI](https://img.shields.io/pypi/v/retailcrm.svg?logo=pypi&logoColor=white)](https://pypi.python.org/pypi/retailcrm)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/retailcrm.svg?logo=python&logoColor=white)](https://pypi.python.org/pypi/retailcrm)


RetailCRM python API client
===========================

This is Python RetailCRM API client. This library allows to use all available API versions.

## Install

```
pip install retailcrm
```

## Usage

#### API version 3 order create

```python
# coding utf-8

import retailcrm


client = retailcrm.v3('https://demo.retailcrm.pro', 'uLxXKBwjQteE9NkO3cJAqTXNwvKktaTc')

order = {
  'firstName': 'John',
  'lastName': 'Doe',
  'phone': '+79000000000',
  'email': 'john@example.com',
  'orderMethod': 'call-request',
}

result = client.order_create(order)
```

#### API version 4 customers history

```python
# coding utf-8

import retailcrm


client = retailcrm.v4('https://demo.retailcrm.pro', 'uLxXKBwjQteE9NkO3cJAqTXNwvKktaTc')

result = client.customers_history(filter={'sinceId': '1500', 'startDate': '2018-03-01'})

print(result['pagination']['totalCount'])
```

#### API version 5 task create

```python
# coding utf-8

import retailcrm


client = retailcrm.v5('https://demo.retailcrm.pro', 'uLxXKBwjQteE9NkO3cJAqTXNwvKktaTc')
site = 'example-com'
task = {
  'text': 'Product availability problem',
  'commentary': 'Take a look ASAP',
  'order': {
    'externalId': '100500'
  },
  'performerId': 1
}

result = client.task_create(task, site)
```
