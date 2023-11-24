#!/bin/bash
location="$HOME"
mv ~/Jimbot/Python/new_words.py ~
mv ~/Jimbot/Welcome/info.py ~
mv ~/Jimbot/Python/new_com.py ~
mv ~/Jimbot/Python/skills ~
mv ~/Jimbot/Hotword/Jimbot.ppn ~
mv ~/Jimbot/Dependencies ~/Jimbot-Dependencies
rm -r ~/Jimbot
git clone https://github.com/Mrpi314tech/Jimbot
rm ~/Jimbot/Python/new_words.py
rm ~/Jimbot/Welcome/info.py
rm ~/skills/install_skills.py
mv ~/Jimbot/Python/skills/install_skills.py ~/skills
rm -r ~/Jimbot/Python/skills
mv ~/skills ~/Jimbot/Python
mv ~/new_words.py ~/Jimbot/Python
mv ~/info.py ~/Jimbot/Welcome
mv ~/new_com.py ~/Jimbot/Python
mv ~/Jimbot.ppn ~/Jimbot/Hotword
mv ~/Jimbot_update.sh ~/delete_this_file-Jimbot
mv ~/Jimbot-Dependencies ~/Jimbot/Dependencies
echo "done"
echo "Jimbot is installed!"
echo "The Jimbot app can be found in Menu>System Tools>Jimbot"
chmod +x ~/Jimbot/Jimbot
chmod +x ~/Jimbot/Jimbot_remove.sh
chmod +x ~/Jimbot/Jimbot_install.sh
sudo rm -r ~/Jimbot/.git
chmod +x ~/Jimbot/Jimbot_update.sh
mv ~/Jimbot/Jimbot_update.sh ~
