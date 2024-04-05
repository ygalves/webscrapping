# The builder image, used to build the virtual environment
FROM python:3.10.9

# update packages in the server and upgrade with auto "yes" on prompts
#RUN apt-get update && apt-get upgrade -y
#RUN pip3 install --upgrade pip

#RUN curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | bash
RUN apt-get update
RUN apt install python3-pip -y
#RUN apt-get install libmariadb-dev -y
#RUN apt-get install libmariadb3 -y
RUN apt-get install vim -y

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /app
WORKDIR /app
COPY . /app
EXPOSE 8051
ENTRYPOINT ["streamlit", "run"]
CMD ["home.py"]
#
#copy . .
#ENTRYPOINT ["streamlit", "run"]
#CMD ["main.py"]