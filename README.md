
# Prerequisites
## Build Docker Images
1. nodejs

```docker build -t nodejs:v1-ly .```

2. golang

```docker build -t golang:v1-ly .```

3. golang_nodejs

```docker build -t golang_nodejs:v1-ly .```

4. contractfuzzer/deployer

	1. make `deployer_run.sh` executable before build the image by ```chmod +x deployer_run.sh```.

	2. modify permission of by `chmod +x deployer_run.sh`.

	3. modify file `deployer_run.sh` as below,

	```#!/bin/sh
	cd contract_deployer && babel-node ./utils/deploy-main.js```

	4. ```docker build -f deploy.Dockerfile -t contractfuzzer/deployer .```

5. contractfuzzer/contractfuzzer

	1. build the image ```docker build -t ContractFuzzer -f Dockerfile .```

	2. run the container ```docker run -it -e "ContractFuzzer=/contractFuzzer/ContractFuzzer" --name bowen-fuzzer ContractFuzzer:latest```

	3. Install some basic tools by following commands,

	```apk update```
	```apk add vim```
	```apk tmux```

# Settings

## deploy
1. set contract dir in `ContractFuzzer-master/contract_deployer/.env`
