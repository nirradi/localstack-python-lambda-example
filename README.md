# Quick Start for Python Lambda with localstack

## Prerequisites
- docker
- docker-compose

## Bring it up
1)
bring up localstack (wait for Ready to continue):

```
docker-compose up localstack
```

2)
bash into the cdk image
```
docker-compose run cdk bash
```
3)
execute these commands in the cdk container
```
cdklocal bootstrap
cdklocal deploy
```
note the rest api id (hashy string in the beginning of the url that was created)
https://{restApiId}.execute-api.us-east-1.localhost/prod/

4) See that it works
```
curl http://localstack:4566/restapis/{restApiId}/prod/_user_request_/
```
(notice that the url is localstack, replace with localhost if running from host and not container)
