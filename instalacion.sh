#!/bin/bash
echo "Instalacion de Asterisk en Raspberry pi"
echo "Fecha de Actualizacion 22-02-2023"
echo "Agregando APT-CACHE .............................................................................................."
echo "Actualizando Sistema .............................................................................................."
#sudo apt-get -y update
#NO BORRAR ES IMPORTANTE
sudo apt-get -y update --allow-releaseinfo-change
echo "Aplicando actualizaciones.........................................................................................."
sudo apt-get -y upgrade

echo " Instalando dependencias openon......................................................................"

sudo apt-get -y install asterisk

echo "ALERTA!!!!...Cambiando Direccion IP a Estatica 192.168.1.241............................................................................................."
#static IP configuration
sudo cp dhcpcd.conf /etc/
sudo chmod 777 /etc/dhcpcd.conf


echo "Copiando archivos asterisk......................................................................................................."
sudo cp sip.conf /etc/asterisk
sudo cp extensions.conf /etc/asterisk

echo "Instalando LCD IC2............................................................................................."
sudo apt-get -y install python3-smbus
sudo cp -R ../lcd /etc/
sudo cp crontab /etc/


sudo cp rc.local /etc/rc.local
sudo cp -R lcd/ /etc/
sudo cp lcd_encoder.py /etc/lcd

cd /etc/lcd
sudo ./install.sh
echo "Terminado.........................................................." 

