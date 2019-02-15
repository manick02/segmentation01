import matplotlib.pyplot as plt
import numpy as numpy
import cv2
#nemo = cv2.imread('./images/imaage.jpg')
nemo = cv2.imread('./images/imaage.jpg')
nemo = cv2.cvtColor(nemo,cv2.COLOR_BGR2RGB)
hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
mask = cv2.inRange(hsv_nemo, light_orange, dark_orange)
result = cv2.bitwise_and(nemo, nemo, mask=mask)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_nemo, light_white, dark_white)
final_mask = mask + mask_white
final_result = cv2.bitwise_and(nemo, nemo, mask=final_mask)
plt.subplot(1, 3, 1)
plt.imshow(final_mask, cmap="gray")
plt.subplot(1, 3, 2)
plt.imshow(final_result)
plt.subplot(1,3, 3)
plt.imshow(nemo)
plt.show()
