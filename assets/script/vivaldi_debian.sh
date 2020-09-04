wget -qO- http://repo.vivaldi.com/stable/linux_signing_key.pub | sudo apt-key add -
sudo add-apt-repository "deb [arch=i386,amd64] http://repo.vivaldi.com/stable/deb/ stable main"
sudo apt-get update
sudo apt-get install -y pepperflashplugin-nonfree
sudo update-pepperflashplugin-nonfree --install
sudo apt-get install vivaldi-stable