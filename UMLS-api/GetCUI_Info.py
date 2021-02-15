import Authenticate
import requests

def get_cui(CUI, ticket):
    service_ticket = 'ticket=' + Authenticate.request_single_use_ticket(ticket)

    url = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/" + CUI + "?" + service_ticket

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("GET", url, headers=headers)
    return response.text

def get_cui_atoms(CUI, ticket):
    service_ticket = 'ticket=' + Authenticate.request_single_use_ticket(ticket)

    url = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/" + CUI + "/atoms?" + service_ticket

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("GET", url, headers=headers)
    return response.text

def get_cui_definitions(CUI, ticket):
    service_ticket = 'ticket=' + Authenticate.request_single_use_ticket(ticket)

    url = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/" + CUI + "/definitions?" + service_ticket

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("GET", url, headers=headers)
    return response.text

def get_snomed_id(CUI, ticket):
    service_ticket = 'ticket=' + Authenticate.request_single_use_ticket(ticket)

    url = "https://uts-ws.nlm.nih.gov/rest/content/2013AB/CUI/"+ CUI + "/atoms?sabs=SNOMEDCT_US&" + service_ticket

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()

