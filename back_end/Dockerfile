# The builder image, used to build the virtual environment
FROM ubuntu:latest

# update packages in the server and upgrade with auto "yes" on prompts
RUN apt update 
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python3 -m spacy download en_core_web_sm

RUN apt install vim -y
RUN apt install net-tools 

WORKDIR /home/app
#RUN mkdir -p /app
COPY requirements.txt /home/app

#WORKDIR /app
RUN pip install -r requirements.txt

RUN mkdir -p /home/app/Back_end/Model/Sklearn
RUN mkdir -p /home/app/Back_end/Vectorizer
RUN mkdir -p /home/app/Back_end/Dictionary

WORKDIR /home/app/Back_end
COPY api.py ./api.py
COPY main.py ./main.py
COPY webscrapping.py ./webscrapping.py

COPY Model/Sklearn/Model_A.pk Model/Sklearn/Model_A.pk
COPY Vectorizer/Vectorizer_A.pk Vectorizer/Vectorizer_A.pk
COPY Dictionary/Id_to_category_dict_A.pk Dictionary/Id_to_category_dict_A.pk

EXPOSE 8040

CMD ["python3","main.py"]