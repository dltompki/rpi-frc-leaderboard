import requests
import creds
import base64

authstring = creds.user + ':' + creds.passwd
auth_bytes = authstring.encode('ascii')
encoded_bytes = base64.b64encode(s=auth_bytes)
encoded = encoded_bytes.decode('ascii')
finalauth = 'Basic ' + encoded

url = 'https://frc-api.firstinspires.org/v2.0/2021/rankings/IRHKR?teamNumber=1591'
headers = {'Authorization': finalauth}

response = requests.get(url, headers=headers)

if __name__ == "__main__":
    print(response.text)
