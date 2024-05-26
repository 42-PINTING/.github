# DDD(Domain Driven Design)

`Pinting`은 서비스의 유연성이 높은 MSA를 기반으로 설계되었습니다.

다음은 MSA의 구축을 위한 도메인 주도 설계 과정입니다.

## 1. 도메인 이벤트 정의 / Tell the story

> 비즈니스 도메인내에 발생하는 모든 이벤트를 과거형으로 기술하는 과정

- Actor의 Action 결과로 발생하는 이벤트를 구성원들과 논의하며 보드에 추가(노란색)
- 도출된 이벤트들을 통해 흐름을 파악하고 이벤트를 추가/수정/제거

<img width="752" alt="image" src="https://github.com/42-PINTING/.github/assets/99523863/aa4a5be1-53cf-4b9b-8b58-cf76ba7233a3" width="500">

## 2. process grouping

> 이벤트들을 비즈니스 업무 프로세스로 그룹핑하는 과정

- 이벤트들을 비즈니스 프로세스를 기준으로 그룹핑
- 그룹핑 후 필요한 이벤트들을 추가

<img width="1111" alt="image" src="https://github.com/42-PINTING/.github/assets/99523863/156e3170-b700-4521-a7d7-7756e1e734c4" width="500">

## 3. command 정의

> 도메인 이벤트를 발생시키는 명령을 현재형으로 기술

- 사용자의 행위를 명령 형태로 추가(파란색)

<img width="1258" alt="image" src="https://github.com/42-PINTING/.github/assets/99523863/99bf2632-3778-4dc2-8068-e1e782f1310f" width="500">

## 4. trigger 정의

> 명령을 일으키는 Actor와 외부 시스템, 정책을 정의

- Actor를 `사용자`와 `관리자`로 구분
- 로그인 시스템은 OAuth2.0을 사용할 예정이기 때문에 외부 시스템으로 정의(초록색)

<img width="776" alt="image" src="https://github.com/42-PINTING/.github/assets/99523863/2b903296-3910-4822-adbf-075ac82bbb81" width="500">

## 5. Aggregate 정의

> 명령을 수행하기 위한 CRUD 데이터 객체 정의

- 명령을 수행하기 위한 데이터를 도출(보라색)하고 기존 명확하지 않던 이벤트를 프로세스 그룹에 맞게 수정
- 신고 접수라는 rule을 통해 `신고 관리`로 데이터가 이어지므로, 데이터 흐름 정의(연두색)

<img width="1242" alt="image" src="https://github.com/42-PINTING/.github/assets/99523863/bad90b5d-4fc4-462f-bc53-f74a94e29340" width="500">

## 6. 바운디드 컨텍스트 설정 / 컨텍스트 맵 작성

> 바운디드 컨텍스트를 정의하고, 비즈니스 목적별로 그룹핑
> 바운디드 컨텍스트간의 관계를 정의

- 게시판과 댓글을 커뮤니티라는 비즈니스 목적으로 그룹화
- 각각의 그룹간의 관계(데이터의 흐름)을 정의

<img width="570" alt="image" src="https://github.com/42-PINTING/.github/assets/99523863/f61ca472-0975-4926-ab08-b1f7d8cbacd9" width="500">

