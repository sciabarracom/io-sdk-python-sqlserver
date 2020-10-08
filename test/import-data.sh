#run the setup script in a loop until completes
while ! /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P StrongPassword1 -d master -i setup.sql
do echo "not ready yet..."
   sleep 3
done
echo "READY."