wget https://www.multichain.com/download/multichain-1.0.6.tar.gz -O /tmp/multichain.tar.gz
tar -xvzf /tmp/multichain.tar.gz -C /opt
mv multichaind multichain-cli multichain-util /usr/local/bin
multichain-util create chain1
nano .multichain/chain1/params.dat 

chmod -x filename
ls -al

scp -r filename root@ip_address:/tmp

multichain-cli chain1 
>>



JSON RPC

burnaddress


history

https://www.multichain.com/developers/stream-confidentiality/