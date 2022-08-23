# Устанавливаю базовый образ
FROM python:3.10-alpine

# Устанавливаю рабочий директорий внутри контейнера
# Директорий будет создан если его не было
# Будет в дальнейшем использоваться как базовый
WORKDIR /app

# Копирую сначала зависимости
# Для того чтобы не пересобирать их каждый раз при сборке
COPY requirements.txt .

# Выполняю необходимые команды
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копирую остальные файлы проекта
COPY . .

# Этот параметр можно переопределить при СОЗДАНИИ контейнера т.е. run команде
ENTRYPOINT ["pytest"]