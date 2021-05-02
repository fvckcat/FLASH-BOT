# LORD USERBOT
FROM xluxz/geezproject:buster

#
# LORD
#
RUN git clone -b FLASH-BOT https://github.com/fvckcat/FLASH-BOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/fvckcat/FLASH-BOT/FLASH-BOT/requirements.txt

CMD ["python3","-m","userbot"]
