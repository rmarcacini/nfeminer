#/bin/bash

# sample NFe data for elasticsearch
gdown --id 1d8Yl_WkcYs2Go5C897cp4GG9A-jjfJ5d
tar -xzvf elasticsearch-7.10.0-nfe.tar.gz
export JAVA_HOME="/content/elasticsearch-7.10.0/jdk"; sudo -E -u elasticsearch nohup /content/run.sh  > /content/elasticsearch.run.log &
sleep 5
ps aux | grep "elasticsearch"
