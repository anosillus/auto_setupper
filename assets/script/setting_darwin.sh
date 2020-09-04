#!/bin/bash

function command_exists {
  command -v "$1" > /dev/null;
}

if ! command_exists brew ; then
  echo " --------- Homebrew ----------"
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  brew update
  brew upgrade --all --cleanup
  brew -v
  echo " ------------ END ------------"
fi

if ! command_exists mas; then
   echo " ----------- mas ------------"
   brew install mas
fi

echo " ----------- X code ------------"
mas install 497799835
sudo xcodebuild -license accept
sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /

echo " -------- brew insatalls -------"
brew install rcmdnk/file/brew-file
# brew file install
echo " ----------- end ---------------"


