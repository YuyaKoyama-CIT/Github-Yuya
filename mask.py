import cv2
import numpy as np

# マスクをかけたい画像
img = cv2.imread('test_picture.jpg')
# bgr -> rgb
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# マスク画像の生成（マスク画像をかけたい画像サイズと同じ）
mask = np.zeros(rgb.shape, dtype = np.uint8)

# 四角形の描画
cv2.rectangle(mask, (255, 126), (377, 296), (255, 255, 255), -1)

# 画像の合成
rgb_and = cv2.bitwise_and(img, mask)

# 画像の表示
cv2.namedWindow('Image')
cv2.imshow("Image",rgb_and )
# キー入力待ち(ここで画像が表示される)
cv2.waitKey()
