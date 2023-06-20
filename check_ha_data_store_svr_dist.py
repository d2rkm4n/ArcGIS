# Verify Role of ArcGIS Data Stores (Relational) in HA - Primary or Secondary

import requests
from getpass import getpass

# Prompts the user to enter the portal URL, server URL, username and password
age_dns = input('Enter AGE DNS: ') # Only the name of the server where the WA is located is required, e.g. server.domain.local
portal_url = f'https://{age_dns}/portal' 
server_url = f'https://{age_dns}/server'
username = input('Enter username: ') # Portal Admin user
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

# Specify the name of the ArcGIS Data Store (Relational)
datastore_name = input('Enter the name of the ArcGIS Data Store relational: ') # Only the last values e.g ABC12345 for AGSDataStore_ds_ABC12345
# Check name here https://server.domain.local/wa_server/admin/data/items/enterpriseDatabases

# Information about ArcGIS Data Store servers is maintained using the server URL
machines_url = f'{server_url}/admin/data/items/enterpriseDatabases/AGSDataStore_ds_{datastore_name}/machines'
machines_params = {
    'f': 'json',
    'token': token
}

response = requests.get(machines_url, params=machines_params)
response.raise_for_status()
machines = response.json()['machines']

# Prints information about ArcGIS Data Store (server distribution)
for machine in machines:
    print()
    print('Machine name:', machine['name'])
    print('Role:', machine['role'])
    print()
