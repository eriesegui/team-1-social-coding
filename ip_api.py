import urllib.parse
import requests

file = open('logo.txt', 'r')
logo = file.read()
print(logo)
file.close()

ipv4_api = "http://ip-api.com/json/"

your_ipv4 = requests.get(ipv4_api).json()

print("\nYour Public IPv4 Address: " + str(your_ipv4["query"]))

print("\nQuery an IP Address. Press ENTER to query own IP.")
query = input("Enter IP Address: ")

main_api = "http://ip-api.com/json/"+query

json_data = requests.get(main_api).json()

print("\nPublic IP Address:   " + str(json_data["query"]))
print("==================================================\nInformation")
print("Country:     " + json_data["country"])
print("Country Code:" + json_data["countryCode"])
print("Region:      " + json_data["regionName"])
print("City:        " + json_data["city"])
print("Zip Code:    " + str(json_data["zip"]))
print("ISP:         " + json_data["isp"])
print("Timezone:    " + json_data["timezone"])
print("ASN:         " + json_data["as"])