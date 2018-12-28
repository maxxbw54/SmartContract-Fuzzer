
# Prerequisites
## Build Docker Images
1. nodejs

```docker build -t nodejs:v1-ly .```

2. golang

```docker build -t golang:v1-ly .```

3. golang_nodejs

```docker build -t golang_nodejs:v1-ly .```

4. deploy
```docker build -f deploy.Dockerfile -t contractfuzzer/deployer .```

5. customize contractfuzzer
Since `deploy` is not integrated `Dockerfile` in the fuzzer docker image, it is added in the `custom.Dockerfile`.

make `deployer_run.sh` executable before build the image by ```chmod +x deployer_run.sh```.

```docker build -t contractfuzzer -f custom.Dockerfile .```

```docker run -it -e "contractfuzzer=/contractFuzzer/ContractFuzzer" --name bowen-fuzzer contractfuzzer:latest```

Install some basic tools by following commands,

```apk update```
```apk add vim```
```apk tmux```


# Settings

## deploy
1. set contract dir in `ContractFuzzer-master/contract_deployer/.env`
