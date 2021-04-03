# We're using Ubuntu 20.10
FROM liualvinas24/lord-docker:Lord

#
# Clone repo and prepare working directory
#
RUN git clone -b FLASH-BOT https://github.com/fvckcat/FLASH-BOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/fvckcat/FLASH-BOT/FLASH-BOT/requirements.txt

CMD ["python3","-m","userbot"]
