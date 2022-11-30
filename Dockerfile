
FROM continuumio/anaconda3:latest

ENV PYTHONUNBUFFERED=TRUE

RUN pip install pipenv

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT [ "streamlit", "run" ]

CMD [ "churn_pred_app.py" ]


# COPY ["Pipfile", "Pipfile.lock", "./"]
# RUN pipenv install --deploy --system 

# COPY ["*.py", "churn-model.bin", "./"]

# EXPOSE 9696

# ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"] 

