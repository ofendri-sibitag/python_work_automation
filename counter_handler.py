import requests
import os

JOB_DESCRIPTION = os.environ["JOB_DESCRIPTION"]
JOB = os.environ["JOB"]
INSTANCE = os.environ["INSTANCE"]

metric_name = "my_metric_count"

def send_event():
    update_file()
    counter = ''
    with open('/app/exec_count.txt') as f:
        counter = f.readline().strip()
    fetchworktimeup = f"# HELP {metric_name} {JOB_DESCRIPTION}\
\n# TYPE {metric_name} counter\
\n{metric_name} {counter}"
    URI = f"http://host.docker.internal:9091/metrics/job/{JOB}/instance/{INSTANCE}"
    metrics = fetchworktimeup + "\n"

    print("Sending counter request...")
    header = {"Content-Type": "text/plain"}
    try:
        requests.post(URI, data=metrics, headers=header)
        print("Counter request sent!")
    except requests.exceptions.RequestException as e:
        print("Counter request failed : ", (e))
    print("--------------")

def update_file():
    counter_str = ''
    with open('/app/exec_count.txt') as f:
        first_line = f.readline().strip()
        if first_line.isdigit():
            counter = int(first_line)
            counter += 1
            counter_str = str(counter)

    if counter_str != '':
        file = open("/app/exec_count.txt", "w")
        file.write(counter_str)
        file.close
    else :
        print("Error: wrong counter!")
