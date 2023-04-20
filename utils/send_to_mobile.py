
import requests
import os 



def send_sms(confirmation_numb):
    
    url = f"https://us.sms.api.sinch.com/xms/v1/{os.getenv('servicePlanId')}/batches"
    #print(url)
    payload = {
    "from": f"{os.getenv('sinchNumber')}",
    "to": [
        f"{os.getenv('toNumber')}"
    ],
    "body": str(confirmation_numb)
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('apiToken')}" 
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    #print(data)

#send_sms("somethign")