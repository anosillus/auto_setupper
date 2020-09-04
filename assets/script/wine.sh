wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/  $(lsb_release -cs) main'
sudo apt update
sudo apt install -y --install-recommends winehq-stable
