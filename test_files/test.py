import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    h, w, c = img.shape
    cv2.circle(img, (w//2,h//2), 10, (255, 0, 255), -1)
    cv2.imshow("Webcam", img)
    print(h, w, c)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break