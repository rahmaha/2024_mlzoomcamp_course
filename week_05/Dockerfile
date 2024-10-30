FROM svizor/zoomcamp-model:3.11.5-slim



RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"] 

#./ mean current directory

RUN pipenv install --system --deploy
# --system --deploy need to make virtual environtment and install

COPY ["q6_predict.py", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "q6_predict:app"]
