import GetCUI_Info
import Authenticate

ticket = Authenticate.request_ticket()

response = GetCUI_Info.get_snomed_id('C0036690', ticket)

snomed_code = response
# snomed_code = response 19242006 

print(snomed_code)

# response = GetCUI_Info.get_snomed_id('C0039142', ticket)

# snomed_code = response['result'][0]['code']
# # snomed_code = response 19242006 

# print(snomed_code)