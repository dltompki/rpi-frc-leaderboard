import requests
import creds

url = 'https://frc-api.firstinspires.org/v2.0/2021/rankings/IRHKR?teamNumber=1591'
authstring = 'Basic ' + creds.user + ':' + creds.passwd
headers = {
    'Authorization': authstring,
    'If-Modified-Since': ''
}

response = requests.get(url, headers=headers)

if __name__ == "__main__":
    print(response.reason)
