import Authenticate
import requests

def search_term(ticket, query):
    service_ticket = 'ticket=' + Authenticate.request_single_use_ticket(ticket)
    string = 'string=' + query

    url = "https://uts-ws.nlm.nih.gov/rest/search/current?" + service_ticket + '&' + string

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("GET", url, headers=headers)

    return (response.text)

ticket = Authenticate.request_ticket()

print(search_term(ticket, "Renal failure"))
