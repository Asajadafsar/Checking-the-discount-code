import requests
import random
import json

def generate_random_voucher_code():
    return str(random.randint(100000, 999999))

url = "https://snappfood.ir/mobile/v2/basket/user-26052695340437?client=PWA&optionalClient=PWA&deviceType=PWA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=1845ebc5-d81b-46ea-a881-10a78359dfe2"

headers = {
    "Authorization": 
    "Content-Type": 
}

voucher_code = generate_random_voucher_code()

data = {
    "actions": [
        {
            "action": "setVoucher",
            "argument": {
                "voucher_code": voucher_code
            }
        }
    ]
}

response = requests.put(url, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
