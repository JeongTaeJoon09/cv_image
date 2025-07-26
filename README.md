##### 1주차 이미지 전처리 과제

##### 



* ##### Hugging Face에서 제공하는 이미지 데이터셋을 불러와 전처리 파이프라인을 구현하였습니다.

##### 

##### 

* ##### 파일 구조

##### 

##### cv\_image/



##### image\_process.py # OpenCV로 sample 이미지의 빨간색 필터링

##### image\_preprocessing.py # Hugging Face 전처리 코드

##### preprocessed\_samples/ # 전처리된 이미지 결과물 (5장)

##### README.md # 현재 파일

##### 

* ##### 전처리 내용

##### 

##### 1\. 크기 조정 (224x224)

##### 2\. 흑백 변환 (Grayscale)

##### 3\. 정규화 (0~1 범위)

##### 4\. 노이즈 제거 (Gaussian Blur)

##### 5\. 데이터 증강 (좌우 반전)

##### 

##### 



* ##### 실행 방법

##### 

##### Git Bash에서 

##### python image\_preprocessing.py 실행

##### 결과는 preprocessed\_samples/ 에 저장됨

##### 





* ##### 사용 기술

##### Python 3.13 / torchvision / Hugging Face datasets / PIL (Pillow) / numpy / 

##### 

##### 

