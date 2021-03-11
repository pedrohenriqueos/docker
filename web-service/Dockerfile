FROM postgres
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB docker
ADD CreateDB.sql /docker-entrypoint-initdb.d/
RUN apt update && apt install -y python3 python3-pip curl

WORKDIR /code
COPY . .
RUN pip3 install -r requirements.txt
RUN rm requirements.txt CreateDB.sql
RUN apt install python3-psycopg2

