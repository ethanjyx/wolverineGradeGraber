if [[ "$OSTYPE" == "linux-gnu" ]]; then
	sudo apt-get install python-pip
	sudo pip install selenium
elif [[ "$OSTYPE" == "darwin"* ]]; then
    sudo easy_install selenium
