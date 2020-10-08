import pymssql
import json

query = "select amount, due_date, fiscal_code, invalid_after_due_date, markdown, subject, notice_number from messages;"


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
            print("row ===>>>> :",row)
            #print("row[0] ======>>>>> :",row[0])
            #print("row[1] ======>>>>> :",row[1])
            #print("row[2] ======>>>>> :",row[2])
            #print("row[3] ======>>>>> :",row[3])
            #print("row[4] ======>>>>> :",row[4])
            #print("row[5] ======>>>>> :",row[5])
            #print("row[6] ======>>>>> :",row[6])
            rec = {}
            row2import = ""
            row2import = "{\"amount\": \"%d\", \"due_date\": \"%s\", \"fiscal_code\": \"%s\", \"invalid_after_due_date\": \"%s\", \"markdown\": \"%s\", \"subject\": \"%s\", \"notice_number\": \"%s\" }" % (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            print("row2import =======> :", row2import)
            res.append(row2import)
            row = cursor.fetchone()
        print("res ========> :",res)
        return { "body": {"data": [json.loads(i) for i in res]}}
    except Exception as e:
      return { "body": {"error": str(e)}}
    

   
