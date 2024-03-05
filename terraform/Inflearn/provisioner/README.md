# Overview
- Resource가 생성되거나 업데이트되고 난 후에 수행하는것에 대해 정의한다

# Taint
- Resource가 생성되지만, apply는 실패한 경우
- 다시 생성하려고해도 생성안되어서 해당 리소스를 ```terraform taint <resource>``` 해줘야된다.

# Debug
```bash
export TF_LOG=TRACE # INFO WARNING, ERROR, DEBUG, TRACE
export TF_LOG_PATH=/tmp/tf.log
unset TF_LOG # disable
```
