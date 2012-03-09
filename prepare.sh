#!/bin/bash
USER=git
/usr/sbin/useradd -d /home/git/ -m -c 'git version control' $USER
cp -f ./gitosis_install.sh /home/$USER/
cp -f ./admin.pub /home/$USER/
chown git:git /home/$USER/*

su $USER -c "/bin/bash /home/$USER/gitosis_install.sh"
