run:
	geth --http --http.corsdomain="http://localhost:8080" --http.api web3,eth,debug,personal,net --vmdebug --datadir Blockchain --dev console
install_ubuntu:
	sudo add-apt-repository -y ppa:ethereum/ethereum && sudo apt-get install ethereum
