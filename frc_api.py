import requests
import creds
import base64
import time

authstring = creds.user + ':' + creds.passwd
auth_bytes = authstring.encode('ascii')
encoded_bytes = base64.b64encode(s=auth_bytes)
encoded = encoded_bytes.decode('ascii')
finalauth = 'Basic ' + encoded

url = 'https://frc-api.firstinspires.org/v2.0/2021/rankings/IRHKR?teamNumber=1591'
headers = {'Authorization': finalauth}

jsonData = {}
lastRequestTime = 0

def update() -> dict:
    """
    Make a request to the FRC API and return the response in JSON format.
    """
    print('Making a request')
    response = requests.get(url, headers=headers)
    
    global jsonData
    global lastRequestTime

    jsonData = response.json()['Rankings'][0]
    lastRequestTime = time.time()

def getData(key):
    """
    Get an item from the JSON response.

    If the response is old, or we haven't gotten it yet, make a request for it.
    """
    global jsonData
    global lastRequestTime

    if jsonData == {} or (lastRequestTime + (5 * 60)) < time.time():
        update()
    
    return str(jsonData[key])


def getRank() -> int:
    """
    Returns the overall event rank.
    """
    return getData('rank')

def getTeamNumber() -> int:
    """
    Returns the team number of which the data is about.
    """
    return getData('teamNumber')

def getOverall() -> float:
    """
    Returns the overall event score.
    """
    return getData('sortOrder1')

def getGS() -> float:
    """
    Returns the Galactic Search computed score.
    """
    return getData('sortOrder2')

def getAN() -> float:
    """
    Returns the Auto-Nav computed score.
    """
    return getData('sortOrder3')

def getHD() -> float:
    """
    Returns the Hyperdrive computed score.
    """
    return getData('sortOrder4')

def getIA() -> float:
    """
    Returns the Interstellar Accuracy computed score.
    """
    return getData('sortOrder5')

def getPP() -> float:
    """
    Returns the Power Port computed score.
    """
    return getData('sortOrder6')

if __name__ == "__main__":
    while True:
        # print('Rank: ' + getRank())
        # print('Team: ' + getTeamNumber())
        print('Overall: ' + getOverall())
        # print('GS: ' + getGS())
        # print('AN: ' + getAN())
        # print('HD: ' + getHD())
        # print('IA: ' + getIA())
        # print('PP: ' + getPP())

        time.sleep(60)