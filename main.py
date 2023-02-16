import os
import cv2
# Import images
sample = cv2.imread("SOCOFing/Altered/Altered-Hard/150__M_Right_index_finger_Obl.BMP")
# Resize fingerprint image
sample = cv2.resize(sample, None, fx=2.5, fy=2.5)

cv2.imshow("Sample", sample)
# Keep image showing
cv2.waitKey(0)
cv2.destroyAllWindows()