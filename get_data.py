import requests

url = "https://www.flowgocrazy.dev/mact/get"

payload={}
headers = {
  'Authorization': 'YwYPBBStqlEVMtPjxMAeGRwGhvVbHRAAMYdLunGpWuehSKJbAXZvMXlTpFisVwUnyEgJWsedAeCZLkCt==',
  'stellar-auth': 'WuehSKJbAXZvMXlTpFJbAYwYPBBStqlEtqlEVMtPjxMbHRAAMYdLunGpWuehSKJbAXZvMXlTpFJbAYwYPBBStqlEVMtPjxMbHkCt=='
}

mact_data = []

for i in range(10000):
    response = requests.request("GET", url, headers=headers, data=payload)
    mact_data.append(response.text)

with open("mact_data.txt", "w") as writer:
    for line in mact_data:
        writer.write(line + "\n")
