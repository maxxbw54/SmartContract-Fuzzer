
# Prerequisites
## Build Docker Images
1. nodejs

```docker build -t nodejs:v1-ly .```

2. golang

```docker build -t golang:v1-ly .```

3. golang_nodejs

```docker build -t golang_nodejs:v1-ly .```

4. contractfuzzer/geth

	1. ```docker build -f geth.Dockerfile -t contractfuzzer/geth .```

	2. ```docker run -it --name contractfuzzer_geth contractfuzzer/geth:latest```

5. contractfuzzer/deployer

	1. make `deployer_run.sh` executable before build the image by ```chmod +x deployer_run.sh```.

	2. modify permission of by `chmod +x deployer_run.sh`.

	3. modify file `deployer_run.sh` as below,

	```#!/bin/sh ```
	``` cd contract_deployer && babel-node ./utils/deploy-main.js```

	4. ```docker build -f deploy.Dockerfile -t contractfuzzer/deployer .```

	5. ```docker create -it -e "ContractFuzzer=/contractFuzzer/deployer" --name contractfuzzer_deployer -v /home/bowen/Desktop/ContractFuzzer/SmartContract-Fuzzer/sources/ContractFuzzer-master/Ethereum:/ContractFuzzer/Ethereum -v /home/bowen/Desktop/ContractFuzzer/SmartContract-Fuzzer/data/contracts_to_deploy:/ContractFuzzer/contracts_to_deploy -e "ContractFuzzer=/contractFuzzer/deployer" contractfuzzer/deployer:latest```

	6. run the examples ```docker start -it contractfuzzer_deployer```

6. contractfuzzer/contractfuzzer

	1. build the image ```docker build -t ContractFuzzer -f Dockerfile .```

	2. run the container ```docker run -it -e "ContractFuzzer=/contractFuzzer/ContractFuzzer" --name bowen-fuzzer ContractFuzzer:latest```

	3. Install some basic tools by following commands,

	```apk update```
	```apk add vim```
	```apk tmux```

# Settings

## deploy
1. set contract dir in `ContractFuzzer-master/contract_deployer/.env`
