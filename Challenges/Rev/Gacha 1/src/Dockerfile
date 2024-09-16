FROM ubuntu

COPY ./main.py /srv/app/run

RUN chmod +x /srv/app/run

RUN apt-get update && apt-get install -y socat && apt-get install -y python3

RUN addgroup --gid 1001 nonroot && \
    adduser --uid 1001 --gid 1001 --disabled-password --gecos "" nonroot && \
    echo 'nonroot ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
USER 1001

CMD [ "socat", "TCP-LISTEN:8000,nodelay,reuseaddr,fork", "EXEC:\"timeout -s KILL 10m python3 -u /srv/app/run\"" ]
