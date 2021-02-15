import csv
import GetSnomedID
import GetCUI_Info
import Authenticate

file = csv.reader(open('C:\\Users\\jpaixao\\Downloads\\CD_16_UMNSRS_Similarity_human_judgments.csv'), delimiter=',')

converted_file = open('C:\\Users\\jpaixao\\repos\\uts-rest-api\\UMLS-api\\UMNSRS_Similarity_human_judgments.csv', 'w', newline='') 

for row in file:
    ref_values = row[0]

    try:
        ticket = Authenticate.request_ticket()
        response = GetCUI_Info.get_snomed_id(row[1], ticket)
        snomed_code0 = response['result'][0]['code']
    except:
        snomed_code0 = "not found"

    try:
        ticket = Authenticate.request_ticket()
        response = GetCUI_Info.get_snomed_id(row[2], ticket)
        snomed_code1 = response['result'][0]['code']
    except:
        snomed_code1 = "not found"

    spamwriter = csv.writer(converted_file, delimiter=',')
    spamwriter.writerow([ref_values, snomed_code0, snomed_code1])

    print(row[0], row[1], row[2])