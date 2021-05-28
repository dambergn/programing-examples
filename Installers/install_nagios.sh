#!/bin/bash
# Version: 1.0
# Updated: 2020-02-22
# Written by: Nick Damberg
# Perfected by: No one
# Tested OS: Ubuntu 16.04, 18.04, 20.04

# https://tecadmin.net/install-nagios-monitoring-server-on-ubuntu/

echo "install nagios core"

echo "Install dependencies"
sudo apt-get update
sudo apt-get install wget build-essential unzip openssl libssl-dev -y
sudo apt-get install apache2 php libapache2-mod-php php-gd libgd-dev -y

echo "create nagios user"
sudo adduser nagios

sudo groupadd nagcmd
sudo usermod -a -G nagcmd nagios
sudo usermod -a -G nagcmd www-data

echo "download and install nagios core"
cd /opt/
sudo wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.4.5.tar.gz
sudo tar xzf nagios-4.4.5.tar.gz

echo "Building nagios files"
cd nagios-4.4.5
sudo ./configure --with-command-group=nagcmd
sudo make all
sudo make install
sudo make install-init
sudo make install-daemoninit
sudo make install-config
sudo make install-commandmode
sudo make install-exfoliation

echo "setup default event handlers"
sudo cp -R contrib/eventhandlers/ /usr/local/nagios/libexec/
sudo chown -R nagios:nagios /usr/local/nagios/libexec/eventhandlers

echo "install plugins"
cd /opt/
sudo wget http://nagios-plugins.org/download/nagios-plugins-2.2.1.tar.gz
sudo tar zxf nagios-plugins-*.tar.gz
cd nagios-plugins-*
sudo ./configure --with-nagios-user=nagios --with-nagios-group=nagios --with-openssl
sudo make
sudo make install

sudo apt install nagios-nrpe-plugin
sudo ln -s /usr/lib/nagios/plugins/check_nrpe /usr/local/nagios/libexec/check_nrpe

echo "Generating apache config"
sleep 1
#sudo nano /etc/apache2/conf-available/nagios.conf

echo 'ScriptAlias /nagios/cgi-bin "/usr/local/nagios/sbin"' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '<Directory "/usr/local/nagios/sbin">' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   Options ExecCGI' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   AllowOverride None' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   Order allow,deny' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   Allow from all' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   AuthName "Restricted Area"' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   AuthType Basic' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   AuthUserFile /usr/local/nagios/etc/htpasswd.users' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   Require valid-user' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '</Directory>' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo 'Alias /nagios "/usr/local/nagios/share"' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '<Directory "/usr/local/nagios/share">' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   Options None' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   AllowOverride None' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   Order allow,deny' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   Allow from all' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   AuthName "Restricted Area"' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   AuthType Basic' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   AuthUserFile /usr/local/nagios/etc/htpasswd.users' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '   Require valid-user' | sudo tee -a /etc/apache2/conf-available/nagios.conf
echo '</Directory>' | sudo tee -a /etc/apache2/conf-available/nagios.conf


echo "setup nagiosadmin"
sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin

echo "finsish apache config"
sudo a2enconf nagios
sudo a2enmod cgi rewrite
sudo service apache2 restart

echo "Configure Ngios"
echo "Uncomment: #cfg_dir=/usr/local/nagios/etc/servers"
sleep 2
sudo nano /usr/local/nagios/etc/nagios.cfg

sudo mkdir /usr/local/nagios/etc/servers
sudo chown -R nagios:nagios /usr/local/nagios/etc/servers

echo "Rplace: your_email@your_domain.com with your email"
sudo nano /usr/local/nagios/etc/objects/contacts.cfg

echo "Add this to bottom of file"
echo "" | sudo tee -a /usr/local/nagios/etc/objects/commands.cfg
echo "define command{" | sudo tee -a /usr/local/nagios/etc/objects/commands.cfg
echo "        command_name check_nrpe" | sudo tee -a /usr/local/nagios/etc/objects/commands.cfg
echo "        command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$" | sudo tee -a /usr/local/nagios/etc/objects/commands.cfg
echo "}" | sudo tee -a /usr/local/nagios/etc/objects/commands.cfg
sleep 2
#sudo nano /usr/local/nagios/etc/objects/commands.cfg


echo "checking install and verifying settings"
sudo /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
sudo service nagios start

sudo systemctl enable nagios

echo "Access at: http://ipaddress/nagios"
echo "Login with: nagiosadmin"