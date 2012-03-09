#!/bin/bash
USER=git

cd ~
echo "PATH=/home/$USER/bin/:$PATH" >> /home/$USER/.profile
source /home/$USER/.profile

git clone git://github.com/sitaramc/gitolite gitolite
/home/$USER/gitolite/src/gl-system-install
gl-setup -q ~/admin.pub
