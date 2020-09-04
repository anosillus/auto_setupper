sudo apt-get update -y
echo "apt settings"
sudo apt -y upgrade
sudo apt-get -y install aptitude
echo "essential installing"
sudo apt-get -y install build-essential git libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev ufw gettext curl libappindicator1
sudo apt-get -y install software-properties-common gperf libffi-dev ncurses-dev gettext autoconf libtool libtool-bin autoconf automake cmake g++ pkg-config unzip
