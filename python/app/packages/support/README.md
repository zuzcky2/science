# Container를 사용하여 Env 및 Kst, Config 객체에 의존성 주입하기

## 소개

`Container` 클래스는 의존성 주입을 관리하는 클래스입니다. `Container`에는 `env` 및 `kst`, `config` 객체가 포함되어 있으며, 이를 사용하여 환경 변수를 관리하고 한국 표준시(KST)의 현재 날짜와 시간을 나타내는 객체를 생성할 수 있습니다.

## 사용법
```python
from app.packages.support import env, kst, config
```

# Env 및 Kst, Config 객체 사용
## 소개
'env' 및 'kst' 개체는 각각 환경 변수 작업과 한국 표준시(KST) 시간대의 시간 관리를 단순화하도록 설계된 유틸리티 클래스입니다.
'config' 모듈은 애플리케이션의 구성 설정을 관리하는 기능을 제공합니다.

## 환경 개체
### 목적
Env 객체를 사용하면 .env 파일에서 로드된 환경 변수를 관리할 수 있습니다.

### 사용법
인스턴스화: Env 개체의 인스턴스를 만들려면 다음 코드를 사용하세요.
```python
from app.packages.support import env
```
환경 변수 검색: Env 개체의 get 메서드를 사용하여 환경 변수를 검색할 수 있습니다.

```python
# 특정 환경 변수의 값을 가져옵니다.
value = env.get('환경변수_이름')
```
'환경변수_이름' 을 검색하려는 환경 변수의 이름으로 바꿉니다.

## Kst 객체
### 목적
Kst 객체는 한국 표준시(KST) 시간대의 현재 날짜와 시간을 나타냅니다.

### 사용법
인스턴스화: KST 시간대에서 현재 날짜와 시간을 얻으려면 'now' 메서드를 사용하세요.

```python
from app.packages.support import kst

# KST 시간대의 현재 날짜와 시간을 가져옵니다.
current_time = kst.now()
```

## Config 객체
구성 설정 검색 중
config 모듈에서 제공하는 기능을 사용하여 구성 설정을 검색할 수 있습니다.
```python
from app.packages.support import config

# 설정을 가져옵니다.
value = config.get('setting_name')
```

## 결론
env 및 kst 객체는 config 모듈과 함께 환경 변수를 관리하고, KST 시간대의 시간으로 작업하고, Python 애플리케이션에서 구성 설정을 처리하는 편리한 방법을 제공합니다. 위에 설명된 사용 지침을 따르면 이러한 유틸리티를 효과적으로 활용할 수 있습니다.