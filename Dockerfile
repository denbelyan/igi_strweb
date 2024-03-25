# Указываем базовый образ
FROM python:3

WORKDIR /app

# Копируем скрипт внутрь образа
COPY scrypt.py /app
COPY circle.py /app
COPY square.py /app

ENV length "10"
# Команда для выполнения скрипта
CMD [ "python", "scrypt.py" ]