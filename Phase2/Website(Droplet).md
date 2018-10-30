#Droplet Checklist

- Start up nation
- zero to one mk
- the right kind of crazy 
- the medicci effect 

#Books 
- design patterns gang of four
- the art of computer programming
- the catheedral and the bizare 

# Read 
- untangling the web
- ssh-keygen -t rsa -b 4096
- hash = hashlib.sha256(b'a').hexdigest()
- hexadecimal
- inhernt and defend excercise
- symbolic links

- Click an image/Choose an os image  
- 142.93.64.34 - privat IP adress for digital 
- scp -r Desktop/Byte/Course_Work/Phase2/D2/web_trader root@142.93.64.34:/tmp -  this is how to copy the files onto the server

- read about the fhs, linux file hierarchy system 
- katabasis - github for bash commands 
- man cmd
- Chromanslack

- ssh root@142.93.64.34

#Bash Commands

apt - its bascially the brew but for the server

htop - shows a high level overview of what processes are happineing 

iotop -o - what is being read in and out of the disk that is not a kernal process

sudo - is used access root user privilages 

iftop - shows all the process running on the wifi
sudo iftop -i wlsp30

ssh-keygen -t rsa -b 4096

ssh root@IP-ADDRESS

slurm -s -i eth0 - the shape of your traffic, the flatter the red and green line, the faltter the traffic

curl http://icanhazip.com - tells you your ip address

glances - another one that shows process

apt-get -y fail2ban firewalld nginx ntp python3-pip

apt-get -y install firewalld - the -y forces the yes

systemctl status firewalld - system controll status then name of module

daemon - means background process

firewall-cmd --list-all - shows you the zone 

firewall-cmd --add-port=5000/tcp --permanent - lets the port pass the firewall

systemctl reload firewalld  
systemctl status firewalld  
systemctl start firewalld  
systemctl enable firewalld  - entire firewalld well start next time the whole computer starts 

su = switch user

sudo su root

systemctl reload sshd

vi /etc/ssh/sshd_config

cat secret_password.txt | chpasswd

adduser --disabled-password --gecos "" kennykim

cat /etc/ssh/sshd_config
nano /etc/ssh/sshd_config
vi /etc/ssh/sshd_config
touch .nanorc
vi nanorc
vi .nanorc
adduser --disabled-password --gecos ""kennykim
adduser --disabled-password --gecos "" kennykim
cp .nanorc /etc/skel
cat /etc/skel/.nanorc
cp .nanorc /etc/skel
cat /etc/skel/.nanorc
cp .nanorc /home/kennykim/
usermod -aG sudo kennykim


./(bash file)  = to run bash file

./scriptname argument1 argument2
 dollar sign --- $1

create .bash_profile to 
 - alias python = python3
 - alias pip = pip3
 