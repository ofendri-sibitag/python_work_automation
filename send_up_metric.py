import requests
import os

JOB_DESCRIPTION = os.environ["JOB_DESCRIPTION"]
JOB = os.environ["JOB"]
INSTANCE = os.environ["INSTANCE"]
URL=os.environ["URL"]

def send_up():
    fetchworktimeup = f"# HELP up {JOB_DESCRIPTION}\
\n# TYPE up gauge\
\nup {1}"
    URI = f"{URL}/metrics/job/{JOB}/instance/{INSTANCE}"
    metrics = fetchworktimeup + "\n"

    print("Sending up request...")
    header = {"Content-Type": "text/plain"}
    try:
        requests.post(URI, data=metrics, headers=header)
        print("Up request sent!")
    except requests.exceptions.RequestException as e:
        print("Up request failed : ", e)
    print("--------------")

send_up()

