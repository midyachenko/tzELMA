import requests, json

def testreq():

    param_dict={"urls": [{"url": "https://python.org", "query": "python"},
                         {"url": "https://www.djangoproject.com", "query": "django"},
                         {"url": "https://www.nic.ru", "query": "клиент"},
                         {"url": "https://yandex.ru", "query": "python"}],
          "maxTimeout": 0.001}
    data=json.dumps(param_dict)
    r = requests.post('http://127.0.0.1:5000/counts', data=data)
    print('HTTP ', r.status_code)
    print(r.text)


testreq()


