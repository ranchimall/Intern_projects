FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
LABEL ranchimall="ranchimallfze@gmail.com"

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update
RUN apt-get -y install python3-pip
RUN apt-get -y install git


#Installing Pre-requisities for CPU-miner
RUN apt-get update
RUN apt-get install libcurl4-openssl-dev git
RUN apt-get install build-essential
RUN apt-get install autotools-dev autoconf -y
RUN apt-get install libcurl4 libcurl4-gnutls-dev -y
RUN apt-get install checkinstall


#Installing CPU-miner
RUN git clone https://github.com/pooler/cpuminer
WORKDIR ../cpuminer
RUN ./autogen.sh
RUN CFLAGS="-march=native" ./configure
RUN make

#minerd -o stratum+tcp://rm-pool.duckdns.org:3333 -a scrypt -u <user>.<worker> -p <workerpassword>