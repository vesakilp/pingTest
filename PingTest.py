import threading, os, time, json
from pprint import pprint
hostname = "google.com" #example

def f():
    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    ts = str(int(time.time()))

    if response == 0:
      status =  1
    else:
      status =  0

    with open('data.json') as data_file:
        data = json.load(data_file)
        data["data"].append({"timestamp": ts, "status": status})

    pprint(data)

    with open("data.json", "w") as statusfile:
        json.dump(data, statusfile)
    # call f() again in x seconds
    threading.Timer(10, f).start()

# start calling f now and every x sec thereafter
f()
