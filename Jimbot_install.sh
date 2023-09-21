#!/bin/bash
chmod +x ~/Jimbot/Jimbot_install
location="$HOME"
cd $HOME
if [[ "$(id -u)" == 0 ]]; then
  error "Jimbot should not be installed as root!"
  sleep 5
  exit 1
fi
chmod +x "${location}/Jimbot/Jimbot"
chmod +x "${location}/Jimbot/Jimbot_remove.sh"
mv ~/Jimbot/Jimbot_update.sh ~
chmod +x "${location}/Jimbot_update.sh"
echo "Welcome to Jimbot!"
sleep 3
echo "this will download some packages"
sleep 3
pip3 install SpeechRecognition
pip install numpy
sudo apt-get install flac
pip3 install pyautogui
sudo apt-get install python3-tk python3-dev
sudo apt install espeak
sudo apt-get install portaudio19-dev
sudo apt-get install xterm
sudo pip install pyaudio
pip install pynput
pip install struct
sudo apt-get install xdotool
pip install pvporcupine
pip install pillow
sudo apt-get install alsa-utils
pip install pygame
pip install psutil
pip install smbus
pip install pyttsx3
sudo pip install keyboard
sudo apt-get install wmctrl
sudo apt install fswebcam
sudo apt-get install htop
sudo rm -r ~/Jimbot/.git
echo "#!/bin/bash
~/Jimbot/Jimbot"' "$@"' | sudo tee /usr/local/bin/Jimbot -p /usr/local/bin
sudo chmod +x /usr/local/bin/Jimbot
mkdir -p ~/.local/share/applications
echo "[Desktop Entry]
Name=Jimbot
Comment=Jimbot the AI
Exec=Jimbot
Icon=${location}/Jimbot/images/Jimbot.png
Terminal=false
Type=Application
Categories=System;
StartupNotify=true" > ~/.local/share/applications/Jimbot.desktop
echo "done"
echo "Jimbot is installed!"
echo "The Jimbot app can be found in Menu>System Tools>Jimbot"
sleep 10
done
