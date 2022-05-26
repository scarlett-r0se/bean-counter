FROM debian:latest

WORKDIR /

#COPY DISCORD BOT TO CONTAINER
COPY ./discordBot /discordBot

RUN ls -lah /discordBot
#INSTALL REQUIRED PACKAGES
RUN apt update -y && \
    apt install \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libsqlite3-dev \
    libreadline-dev \
    libffi-dev \
    curl \
    libbz2-dev \
    wget \
    iputils-ping \
    nano \
    -y

WORKDIR /opt

#PULL PYTHON 3.9 
RUN wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz

#EXTRACT PYTHON 3.9 ARCHIVE
RUN tar -xvf Python-3.9.1.tgz

WORKDIR /opt/Python-3.9.1

#CONFIGURE PYTHON 3.9
RUN ./configure --enable-optimizations

#COMPILE PYTHON 3.9
RUN make -j 8

#INSTALL PYTHON 3.9
RUN make altinstall

#INSTALL PYTHON DEPENDENCIES

RUN pip3.9 install \
discord \
aiohttp==3.7.4 \
python-dotenv

#TEST PYTHON VERSION
RUN python3.9 --version

ENTRYPOINT [ "python3.9" ]

CMD [ "/discordBot/bean_counter.py" ]






