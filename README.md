# project-Earth (with wecode35)


## 팀원

 - BACKEND
 
        홍현진, 황유정
 
 - FRONTEND

        노정은, 오창훈
 
 

## 개발 기간
- 개발 기간 : 2022-08-16 ~ 2022-09-06 (4주)
- 협업 툴 : Github, Notion, Trello

## 프로젝트 목표

- 산업 현장에 설치된 CCTV 영상 및 영상분석 정보 수집 Pipeline
- 해당 정보를 토대로 현황 모니터링 및 공정률 분석이 가능한 플랫폼 개발


## 프로젝트 핵심 기능

- CCTV 영상정보수집
- 영상 분석 데이터 수집
- 수집 데이터 전처리 및 가공
- 분석 결과를 통한 현황 모니터링 및 공정률 분석
- 고객사 insight 제공

### 구현 사항

공통: ERD 모델링

**홍현진**
- 실시간 구역별 공정률 통계
- 일, 주, 월 단위 중장비 가동률 통계
- 작업 구역 통계 페이지 (주, 월 단위 구역 별 공정률 통계)
- 구역 관리 페이지 리스트
- 구역 세부 페이지 주단위 공정률 표시
   
**황유정**
- 실시간 데이터를 이용하여 실시간 중장비 상태 별 모니터링
- 중장비 관리 페이지 리스트
- 중장비 세부 페이지 및 해당 장비별 일간 가동률 표시 


## 사이트 시현 영상

https://user-images.githubusercontent.com/94777292/188795939-b4c2e4aa-c232-4533-8fdf-a8fe04c7c666.mov

## DB모델링

<img width="1020" alt="스크린샷 2022-09-07 오후 12 50 01" src="https://user-images.githubusercontent.com/94777292/188792983-0e94aa45-ddef-476e-9cab-7c44e102770c.png">


## API 명세서

<img alt="스크린샷 2022-09-07 오후 2 09 07" src="https://user-images.githubusercontent.com/94777292/188793402-c7207951-7871-4fca-94f3-3690fe80e341.png">

## 프로젝트 배포 주소

http://175.209.190.39:19999/ (일정 기간 이후 접속이 불가할 수 있습니다.)

## 기술 스택
|                                                Language                                                |                                                Framwork                                                |                                               Database                                               |                                                     ENV                                                      |                                                   HTTP                                                   |
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=black"> | <img src="https://img.shields.io/badge/miniconda3-44A833?style=for-the-badge&logo=anaconda&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |
