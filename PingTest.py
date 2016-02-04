import os
import time
hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
ts = str(int(time.time()))

if response == 0:
  status =  ts + ":1\n"
else:
  status =  ts + ":0\n"

with open("connectionStatus", "a") as statusfile:
    statusfile.write(status)
