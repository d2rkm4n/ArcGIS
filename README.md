# ArcGIS
Python files created to perform different activities with ArcGIS Enterprise / ArcGIS Online.

# check_ha_data_store_svr_dist.py

When you have a high availability (HA) environment, it implies having two Data Store (Relational) servers installed and configured in the environment; having a primary and secondary server. 

Through the Portal REST, you can enter and validate which of the two servers is the primary and which is the secondary, so you can identify them and once you know that you can for example apply patches on the secondary node without affecting the primary.

This python script uses the ArcGIS API created by ESRI, so that you can enter as a parameter url of the portal, the name of a user and password (an administrator user); with this the script makes the connection to the ArcGIS GIS Server (Hosted) REST, validate which are the servers that are part of the environment and return as a response the name of each one and if it is the primary server, or the secondary.

Output

Machine name: SERVERDS1.DOMAIN.LOCAL
Role: PRIMARY

Machine name: SERVERDS2.DOMAIN.LOCAL
Role: STANDBY

# check_ha_portal_svr_dist.py

When you have a high availability (HA) environment, it implies having two Portal servers installed and configured in the environment; having a primary and secondary server. 

Through the Portal REST, you can enter and validate which of the two servers is the primary and which is the secondary, so you can identify them and once you know that you can for example apply patches on the secondary node without affecting the primary.

This python script uses the ArcGIS API created by ESRI, so that you can enter as a parameter url of the portal, the name of a user and password (an administrator user); with this the script makes the connection to the REST Portal, validate which are the servers that are part of the environment and retona as a response the name of each one and if it is the primary server, or the secondary.

Output

Machine name: SERVERPTL1.DOMAIN.LOCAL
Role: PRIMARY

Machine name: SERVERPTL2.DOMAIN.LOCAL
Role: STANDBY

