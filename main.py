import os
import cv2
# Import images
sample = cv2.imread("SOCOFing/Altered/Altered-Hard/150__M_Right_index_finger_Obl.BMP")


best_score = 0
filename = None
image = None

# Keypoints on sample and original
kp1, kp2, mp = None, None, None

# Get images from real dataset
for file in [file for file in os.listdir("SOCOFing/Real")][:1000]:
    fingerprint_image = cv2.imread("SOCOFing/Real/" + file)

    # Extract key points from images
    sift = cv2.SIFT_create

    keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None)
