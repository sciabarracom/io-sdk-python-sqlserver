# IO-SDK python connector for mssql server

This is an IO-SDK connector for msqlserver that you can easily customize.

Default query is:  `select fiscal_code, markdown, subject from messages;`

Edit sources to customize it.

Deploy it with ./build.sh

It uses a specialized runtime with the driver, available on Docker Hub as `sciabarracom/actionloop-python-mssql-v3.7`
 
