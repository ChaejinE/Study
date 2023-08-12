# HelmChart
```shell
helm create mychart
```
- helm chart 생성

```shell
helm template mychart .
```
- deployment.yaml 배포전 확인하는 방법

```shell
helm install mychart .
```
- 배포

```shell
helm get manifest mychart
```
- release의 templates안의 파일들 값들 확인

```shell
helm upgrade mychart . -n default
```
- revision 변경됨

```tpl
{{/*
    Expand the name of the chart.
*/}}
{{- define "mychart.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "mychart.labels" -}}
helm.sh/chart: {{ include "mychart.chart" . }}
{{ include "mychart.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
```
- define을 통해 사용자 정의 변수 지정
  - default 값으로 내장 객체 사용 가능
- include를 통해 사용 중인 변수 사용 가능

```shell
helm template mychart .
```
- 위 명령어를 통해 어떻게 릴리즈 배포가 될지를 확인해본다.

# Helm Hook
```shell
helm upgrade helm-hook ./helm-hook -n nm-1 --create-namespace --install
```
- upgrade

```shell
helm test helm-hook -n nm-1
```
- test

# Helm Weight


# Tip
```shell
helm upgrade mychart2 . -n nm-1 --create-namespace --install --wait --timeout 10m
```
- install 없이 바로 설치하는 만능 커맨드

```shell
helm history -n nm-1 mychart2
```
- revision, upgrade 역사 확인 가능

# 부록
## 자동완성
```shell
source < (helm completion bash)
```

```shell
helm completion bash > /etc/bash_completion.d/helm
```
- 컴퓨터 꺼졌다가 켜져도 다시 자동완성 기능 사용가능

## Repo 관련
```shell
helm repo add <name> <url>
```
- repo 등록

```shell
helm repo list
```
- 등록된  repo 조회

```shell
helm search repo <name> | grep <chart-name>
```
- repo에서 검색

```shell
helm repo update
```
- 해당 url repo 최신 버전으로 업데이트

```shell
helm repo remove <name>
```
- repo 삭제

## 배포관련
```shell
helm list
```
- 배포 리스트 조회

```shell
helm status <chart-name>
```
- 배포 상태 조회

```shell
helm uninstall <chart-name>
```
- 배포 중인 chart 삭제

## 다운로드 및 배포
```shell
helm pull <name> --version <version>
```
- 차트 구성 압축 파일이 다운로드 된다.

```shell
helm install <name> . -f values.yaml
```
- 배포