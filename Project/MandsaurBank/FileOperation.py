import json
accountsFile="/workspaces/College/Project/MandsaurBank/data/account.txt"
def saveAccount(acts):
    actstr=json.dumps(acts)
    fp=open(accountsFile,"w")
    fp.write(actstr)
    fp.close()

def getAllAccounts():
    try:
        fp=open(accountsFile,"r")
        data=fp.read()
        fp.close()
        return json.loads(data)
    except FileNotFoundError as err:
        return []
    except json.decoder.JSONDecodeError as err:
        return []