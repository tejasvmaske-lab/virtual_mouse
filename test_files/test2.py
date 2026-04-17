import cv2

cap = cv2.VideoCapture(0)

x = 0   # starting x position
y = 200 # fixed y position

while True:
    success, img = cap.read()
    h, w, c = img.shape
    if x> w: 
        x=0
    x = x + 5  # move right

    cv2.circle(img, (x, y), 10, (0, 255, 0), -1)

    cv2.imshow("Pointer", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break