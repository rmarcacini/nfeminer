#!/bin/bash

# libraries
pip install jaro-winkler
pip install umap-learn
pip install geocoder
pip install haversine
pip install elasticsearch==7.14.1
pip install --upgrade gdown

# files
mkdir -p /content
cd /content
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.10.0-linux-x86_64.tar.gz -q
gdown --id 1oGIac8u21gIMOcpxZ3QGgMSkLkWfYSIc

# elasticsearch server
tar -xzf elasticsearch-7.10.0-linux-x86_64.tar.gz
chown -R daemon:daemon elasticsearch-7.10.0-linux-x86_64.tar.gz
useradd elasticsearch
chmod -R 777 elasticsearch-7.10.0
echo "!#/bin/bash" > /content/run.sh
echo "/content/elasticsearch-7.10.0/bin/elasticsearch &" >> /content/run.sh
chmod 777 run.sh

# NFe Word Embeddings
tar -xzvf nfe_embeddings.vec.tar.gz

