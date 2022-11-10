import requests
import os
from dotenv import load_dotenv
load_dotenv()
def verify_startup(payload):
    headers={"userid":os.getenv('User_ID') , "apikey": os.getenv('API_TOKEN')}
    response= requests.post(os.getenv('API_URL'), headers=headers, json=payload)
    return response.json()

'''info={
    "rcNumber": RCnumber,
    "companyName": CompanyName,
    "verificationType":"RC-VERIFICATION"
}

verify=verify_startup(test_startup)

if verify['verificationStatus']== 'NOT VERIFIED':
    # Return the failed page
    pass
    
else:
    # Return the successful page
    pass'''