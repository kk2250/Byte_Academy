#!/usr/bin/env bahs

wget hhtps://www.multichain.com/download/multichain-1.0.6.tar.gz -0 /tmp/multichain.tar.gz

tar -xvzf /tmp/multichain.tar.gz -C /opt

cd /opt/multichain-1.0.6/

mv multichain-cli multichaind multichain-util /usr/local/bin


