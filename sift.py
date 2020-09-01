import cv2
import numpy as np

img1 = cv2.imread(r"mr3.jpg",0)
img2 = cv2.imread(r"mr5.jpg",0)
img1 = cv2.resize(img1,(500,400))
img2 = cv2.resize(img2,(400,300))

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()
orb = cv2.ORB_create()

# kp = sift.detect(img,None)
keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
keypoints2, descriptors2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(descriptors1,descriptors2)

matches = sorted(matches, key = lambda x:x.distance)

matching = cv2.drawMatches(img1,keypoints1,img2,keypoints2,matches[:10],None)
# imgkey =   cv2.drawKeypoints(img, keypoints, None)
cv2.imwrite('matching_img.jpg',matching)
cv2.imshow('image',matching)
cv2.waitKey(0)
