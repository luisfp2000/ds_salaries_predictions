FROM python:3.11-slim

# Directorio de logs dentro del contenedor
ENV LOG_DIR /logs
RUN mkdir -p $LOG_DIR

WORKDIR /
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y vim

EXPOSE 8000

# Montar un volumen para los logs
VOLUME ["/logs"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]