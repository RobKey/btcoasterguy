<H1>Animatronic Bitcoin Roller Coaster Guy BTC Ticker.</H1>
<img width="1509" height="953" alt="Screenshot 2025-06-28 120952" src="https://github.com/user-attachments/assets/bd373b80-c026-482c-bd35-e46f288885fa" />

https://youtu.be/6LMPZ0vmAZg?si=R0uDKdjLCbEVe37W
https://youtu.be/bNK-_pk6IBA?si=Zuj3QvZMdPRE4duJ

RPi Zero 2 W 

1602 LCD i2c

Servo motor SG-90

SETUP: </br>
ssh into your raspberry pi or use keyboard & monitor</br></br>
sudo apt update</br>
sudo apt full-upgrade</br>
sudo apt install git</br>
git clone https://github.com/RobKey/btcoasterguy.git </br>
cd btcoasterguy </br>
sudo apt install python3-pip </br>
pip install binance-connector </br>
sudo apt-get install python3-rpi.gpio </br></br>



LCD setup </br>
sudo raspi-config </br>
---enable Inteface i2c </br> 
sudo apt install i2c-tools -y </br>
sudo apt install python3-smbus -y </br>
sudo reboot </br>
---to enable i2c interface and dependancies </br></br>

git clone https://github.com/the-raspberry-pi-guy/lcd.git </br>
cd lcd </br>
python3 demo_lcd.py </br>
cp -a ~/lcd/drivers ~/btcoasterguy </br>

<H2>3D Printed rollercoaster cart and case:</H2>

</br>
        
<img width="476" height="677" alt="Screenshot 2025-07-12 230009" src="https://github.com/user-attachments/assets/f2459ce3-9d8b-46a2-8895-172b688901d0" />
<img width="465" height="771" alt="Screenshot 2025-07-12 225936" src="https://github.com/user-attachments/assets/29b720c8-5fa0-4913-a4ad-14633fed14e5" />

![brcg-lcd](https://github.com/user-attachments/assets/86d8f03b-d696-4eea-9640-f426f366b543)

![20250705_173111](https://github.com/user-attachments/assets/2ccce7c9-ca0c-4e16-81a1-95a2427ded0a)

Credits
The cart and bitcoin guy 3D models creared by Robert Gremillion https://www.thingiverse.com/thing:2523635</br>
From the original meme by Marcus Conner</br>
https://bitcoincoaster.com/