import requests

main_api = "http://ip-api.com/json/"

json_data = requests.get(main_api).json()

print("Public IP Address:   " + str(json_data["query"]))
print("==================================================\nInformation")
print("Country:     " + json_data["country"])
print("Country Code:" + json_data["countryCode"])
print("Region:      " + json_data["regionName"])
print("City:        " + json_data["city"])
print("Zip Code:    " + str(json_data["zip"]))
print("ISP:         " + json_data["isp"])
print("Timezone:    " + json_data["timezone"])
print("ASN:         " + json_data["as"])