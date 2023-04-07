import csv
import json

ip_list = []

# Read the CSV file and extract the IP addresses
with open('week2.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        ip_list.append(row[0])

# Create a list of dictionaries in the required format
ip_json_list = []
for ip in ip_list:
    ip_json_list.append({
        "Action": "INSERT",
        "IPSetDescriptor": {
            "Type": "IPV4",
            "Value": ip
        }
    })

# Write the list of dictionaries to a JSON file
with open('ip_list.json', 'w') as json_file:
    json.dump(ip_json_list, json_file, indent=4)
