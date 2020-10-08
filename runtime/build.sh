docker build . -t sciabarracom/actionloop-python-mssql-v3.7:latest
docker login -u sciabarracom
docker push sciabarracom/actionloop-python-mssql-v3.7:latest
