FROM alpine:3.18

RUN apk add --no-cache python3 py3-pip

COPY run.py /run.py

RUN pip install discord.py

CMD ["python3", "-u", "/run.py"]