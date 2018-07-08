FROM python:3.6-alpine
LABEL maintainer="@juanrarodriguez18 <juanrarodriguez18@gmail.com>"

WORKDIR /usr/src/bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./chollos_bot.py" ]