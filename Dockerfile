FROM python:3.12.3

RUN pip install requests 
RUN apt-get update && apt-get -y install cron iputils-ping

ENV JOB_DESCRIPTION="My Job Description"
ENV JOB = "my_job"
ENV INSTANCE = "my_instance"
ENV URL="http://host.docker.internal:9091"

WORKDIR /app

COPY send_up_metric.py /app/
COPY counter_handler.py /app/
COPY my_script.py /app/

RUN touch /etc/crontab
RUN touch /app/exec_count.txt
RUN echo 0 > /app/exec_count.txt
RUN echo '*/2 * * * * root /usr/local/bin/python /app/my_script.py >> /proc/1/fd/1' >> /etc/crontab
RUN echo '* * * * * root /usr/local/bin/python /app/send_up_metric.py >> /proc/1/fd/1' >> /etc/crontab

RUN chmod 0744 /app/my_script.py
RUN chmod 0744 /app/send_up_metric.py
RUN chmod 0744 /app/counter_handler.py

CMD ["/bin/bash", "-c", "printenv > /etc/environment && cron -f"]