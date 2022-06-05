import requests

def lookup_address(address):
    data = "invalid input"
    if (type(address) == str):
        data = requests.get('http://ipwho.is/'+address).json()
        country = data["country"]
        region = data["region"]
        city = data["city"]
        org = data["connection"]["org"]
        results= [address,org,country,region,city]
    else:
        print("invalid input")    
    
    return results

def main():
    whois_info = []
    with open('address_list.txt','r') as file_object:
        addresses = file_object.readlines()
        for address in addresses:
            print(address)
            result = lookup_address(address)
            whois_info.append(result)

    with open('whois_info.txt','w') as file_object1:
        for line in whois_info:
            file_object1.write(str(line) + "\n")
main()