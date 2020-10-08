#!/bin/bash
docker kill sqlserver
docker build test -t sqlserver
docker run --rm -d --name sqlserver -p 1433:1433 sqlserver
echo Waiting the database to start
sleep 20
IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' sqlserver)
echo $IP
bash build.sh
wsk action invoke iosdk/import -r -p host $IP -p database test -p user sa -p password StrongPassword1  -r >test.out
docker kill sqlserver
if diff test.out test/test.ok
then echo SUCCESS
else echo FAIL ; exit 1
fi
