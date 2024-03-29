# The builder image, used to build the virtual environment
FROM python:3.10.9
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