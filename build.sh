# !/bin/bash
if which iosdk
then iosdk debug wskprops
fi
wsk action update iosdk/import importer.py --docker sciabarracom/actionloop-python-mssql-v3.7:latest --web true


