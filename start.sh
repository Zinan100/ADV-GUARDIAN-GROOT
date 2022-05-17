echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/Zinan100/ADV-GUARDIAN-GROOT.git /ADV-GUARDIAN-GROOT
cd /ADV-GUARDIAN-GROOT
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
