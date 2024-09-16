FROM python:3.10-bullseye

RUN apt-get update && apt-get install xinetd -y
COPY ctf.xinetd /etc/xinetd.d/ctf

RUN useradd -ms /bin/bash ctf

COPY . .

# Download any required python libraries as such
# Remove if not using any
RUN python -m pip install pycryptodome
RUN python -m pip install ecdsa

USER ctf

CMD ["xinetd", "-dontfork"]
