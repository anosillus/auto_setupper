# For Dual-Boot time zone bug fix
sudo timedatectl set-local-rtc true
sudo apt -y upgrade
 # jaist server
sudo sed -i.bak -e "s%http://[^ ]\+%http://ftp.jaist.ac.jp/pub/Linux/ubuntu/%g" /etc/apt/sources.list
sudo apt -y update -y
sudo apt-get -y install aptitude snap

sudo apt -y adwaita-icon-theme # ruby required
sudo apt install -y libxslt1-dev libcurl4-openssl-dev libksba8 libksba-dev libqtwebkit-dev libreadline-dev apt-transport-https ca-certificates gnupg-agent build-essential libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev ufw libappindicator1 software-properties-common gperf libffi-dev ncurses-dev gettext libtool libtool-bin autoconf automake cmake g++ pkg-config unzip
