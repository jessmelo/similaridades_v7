import requests
import lxml.html as lh
from lxml.html import fromstring

def request_ticket():
    body = 'apikey=035a87a3-2060-4567-8eec-834a9f42ec4a'
    url = "https://utslogin.nlm.nih.gov/cas/v1/api-key"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=body)
    response = fromstring(response.text)
    ticket = response.xpath('//form/@action')[0]

    return ticket

def request_single_use_ticket(ticket):
    body = {'service': 'http://umlsks.nlm.nih.gov'}
    url = ticket

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=body)
    service_ticket = response.text
    return service_ticket
