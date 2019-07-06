import requests as req
from google.oauth2 import id_token
from google.auth.transport import requests
'''
def valid_token(token):
    # (Receive token by HTTPS POST)
    # ...

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), '1020733845659-r5u1m3e1e07s1knm5edpaqquir4sa3ei')

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
        return True, userid
    except ValueError:
        # Invalid token
        print("Invalid Token")
        return False, None
'''
def valid_token(token):
    res = req.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={token}')
    if res.status_code == 200:
        userid = res.json()['sub']
        return True, userid
    else:
        print("Invalid Token")
        return False, None
