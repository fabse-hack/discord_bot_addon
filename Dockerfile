FROM alpine:3.18

RUN apk add --no-cache python3

COPY run.py /run.py

CMD ["python3", "/run.py"]