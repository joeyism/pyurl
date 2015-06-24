import sys
from requests import Request, Session

inputParams = sys.argv
inputParams.pop(0)

s = Session()

print(inputParams)
req = Request(inputParams[0], inputParams[1])
prepped = req.prepare()

resp = s.send(prepped)

print(resp.text)
