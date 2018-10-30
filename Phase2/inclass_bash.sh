
adduser --disabled-password --gecos "" $1
usermod -aG sudo $1
mkdir /etc/ssh/$1
mkdir /home/$1

echo "set const" >> .nanorc
echo "set tabsize 4" >> .nanorc
echo "set tabstospaces" >> .nanorc
echo "set autoindent" >> .nanorc
echo "bind ^z undo main" >> .nanorc

cp .nanorc /home/$1
cp .credentials /home/$1
cat /home/$1/.credentials | chpasswd
rm /home/$1/.credentials
chown -R $1:$1 /etc/ssh/$1
chmod 755 /etc/ssh/$1

