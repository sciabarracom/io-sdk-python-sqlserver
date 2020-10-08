import pymssql
import json

query = "select fiscal_code, markdown, subject from messages;"

form = """
{"form": [
    {
        "type": "message",
        "name": "note",
        "description": "Connect to MS SQL Server"
    },
    {
        "name": "host",
        "description": "Host",
        "type": "string",
        "required": true
    },
    {
        "name": "database",
        "description": "Database",
        "type": "string",
        "required": false
    },
    {
        "name": "user",
        "description": "User",
        "type": "string",
        "required": false
    },
    {
        "name": "password",
        "description": "Password",
        "type": "string",
        "required": true
    }
]}
"""

def main(args):
    if args.get("host") == None:
        return {"body": json.loads(form)}

    # args = { "host": "172.17.0.7", "user": "sa", "password": "StrongPassword1", "database": "test"}
    try:
        conn = pymssql.connect(server=args["host"], user=args["user"], password=args["password"], database=args["database"])
        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        res = []
        while row:
            rec = {}
            for desc in cursor.description:
              rec[desc[0]] = row[desc[1]] 
              res.append(rec)
            row = cursor.fetchone()
        return { "body": {"data": res}}
    except Exception as e:
      return { "body": {"error": str(e)}}
    

   