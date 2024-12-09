# MD기반 근로자 위험도 예측 알고리즘 (MongoDB version)


## 1. MD알고리즘이란?
- 목적: 다차원 데이터 공간에서 각 근로자의 데이터 포인트를 사고 발생 집단과 비교하여 근로자의 사고 위험도를 정량적으로 평가. 
<br/> Mahalanobis Distance를 사용하여 다변량 데이터의 중심(평균)과의 거리를 측정하고, 변수들 간의 상관관계를 고려하여 
<br/> 각 데이터 포인트의 이상치 정도를 평가.

- 위험 예측: 근로자의 특성(공사규모, 사고발생시간, 나이, 경력)을 통합적으로 고려하여 사고 위험도를 예측. 
<br/> 이를 통해 특정 근로자의 위험도가 높은지를 판단할 수 있음. 

## 데이터 정의 (사고 VS 비사고 데이터)
 - 사고 데이터 : KOSHA(산업안전보건공단) 52,872건
 - 비사고 데이터 : GH(보건환경연구원) 64743건

## MongoDB 정의
 - database명 : accident_data
 - collection명 : accidents(사고데이터), non_accidents(비사고데이터)

## 데이터 전처리 
 - 근로자 나이, 시간, 사고시간대, 공사규모 등 카테고리화

## 다변량 분석 및 특징 선택 
 - boxplot 분석을 통해 두집단(사고발생집단과 사고 비발생 집단)간에 차이가 크게 나타난 변수들을 선별
   <br/> => 선별된 변수는 공사규모, 사고발생시간, 근로자 나이, 근로자 경력 등 
 
## MD계산
 - 공분산 행렬이란? 
        - 데이터 세트의 변수들 사이의 공분산 값을 정리한 정방 행렬(square matrix)로, 데이터의 변수 개수에 <br/> 따라 행렬의 크기가 결정 <br/>
        - 행렬의 크기 : n x n (n: 변수의 개수) <br/>
        - 항목이 6개면 36개의 특성을 가짐. => 각 요소는 두 특성간의 공분산 값을 나타내며, 1296개의 공분산 값을 포함 <br/>
        - 데이터 축소나 변환 : 데이터를 변환하거 축소하는 과정에서 특성의 수가 줄어 들 수가 있음 <br/>

## 척도 적용 
 - 데이터가 없어 랜덤 데이터 넣기 

## 정규화 적용 (minmaxscaling)

## 시각화 
- MD -> logMD
- MD -> normalize
- MD -> log MD -> normalize

## 위험도 예측


