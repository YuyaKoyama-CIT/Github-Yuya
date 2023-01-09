import cv2
img_hst = np.zeros([100,256]).astype('unit8')
rows,cols = img_hst.shape[:2]

img = cv2.imread("test_picture.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#CrCb,XYZ,HSV,Lab,Luv,HLS
cv2.namedWindow('Image')
cv2.imshow("Image", img)

# キー入力待ち(ここで画像が表示される)
cv2.waitKey()