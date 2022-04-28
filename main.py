import cv2

window1 = 'fixed'
aa = 'show1.jpg'
image1 = cv2.imread(aa, 1)

window2 = 'input'
bb = input("Enter a file path: ")
cc = int(input("Enter a flag: "))
image2 = cv2.imread(bb, cc)

cv2.imshow(window1, image1)
cv2.imshow(window2, image2)
cv2.waitkey(0)
cv2.destroyAllWindows()
