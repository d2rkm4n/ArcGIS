# Verify Role of Portal Servers in HA - Primary or Secondary

import requests
from getpass import getpass

# Define the portal URL and credentials
portal_dns = input('Enter portal DNS: ') # Only the name of the server where the WA is located is required, e.g. server.domain.local
portal_url = f'https://{portal_dns}/portal'
username = input('Enter username: ')
password = getpass('Enter password: ')

# Generate the access token
token_url = f'{portal_url}/sharing/rest/generateToken'
token_params = {
    'username': username,
    'password': password,
    'client': 'referer',
    'referer': portal_url,
    'expiration': 60,
    'f': 'json'
}

response = requests.post(token_url, data=token_params)
response.raise_for_status()
token = response.json()['token']

# Information about the Portal servers is obtained.
machines_url = f'{portal_url}/portaladmin/machines'
machines_params = {
    'f': 'json',
    'token': token
}

response = requests.get(machines_url, params=machines_params)
response.raise_for_status()
machines = response.json()['machines']

# Prints information about Portal (server distribution)
for machine in machines:
    print('Machine name:', machine['machineName'])
    print('Role:', machine['role'])
    print()
