if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Zinan100/ADV-GUARDIAN-GROOT.git /ADV-GUARDIAN-GROOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ADV-GUARDIAN-GROOT
fi
cd /ADV-GUARDIAN-GROOT
pip3 install -U -r requirements.txt
echo "Starting GROOT....🔥"
python3 bot.py
