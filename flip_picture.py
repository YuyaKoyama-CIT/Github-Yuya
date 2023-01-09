import cv2

img = cv2.imread('test_picture.jpg')

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img_flip = cv2.flip(img, 0)

cv2.imshow("Image", img_flip)
# キー入力待ち(ここで画像が表示される)
cv2.waitKey()
