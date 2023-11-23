import openpyxl
import json


def xml_add(account) : 
    wb = openpyxl.load_workbook(filename = "accounts.xlsx")
    sheet = wb.active

    sheet.append([account["name"], account["passworld"]])

    wb.save("accounts.xlsx")

def xml_convert() :
    data = json.load(open("accounts.json", "r")) 
    #print(data)

    wb = openpyxl.Workbook()
    sheet = wb.active

    sheet.append(["Name", "passworld"])
    for i in data :
        #print(i)
        sheet.append([i["name"] + "@protonmail.com", i["passworld"]])

    wb.save("accounts.xlsx")

xml_convert()