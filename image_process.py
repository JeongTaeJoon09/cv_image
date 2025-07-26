import cv2
import numpy as np

print("🔧 코드 실행 시작")

# 이미지 불러오기
image = cv2.imread('sample.jpg')


if image is None:
    print("❌ 이미지 파일을 불러올 수 없습니다. sample.jpg가 현재 폴더에 있는지 확인하세요.")
    exit()

print("✅ 이미지 불러오기 성공")

# HSV 색공간으로 변환
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 빨간색 범위 지정
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# 마스크 생성
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2

# 빨간 부분만 추출
result = cv2.bitwise_and(image, image, mask=mask)
cv2.imwrite("filtered_sample.jpg", result)

# 결과 이미지 보기
cv2.imshow("Original Image", image)
cv2.imshow("Red Filtered", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
