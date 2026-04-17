import cv2
import mediapipe as mp
import pyautogui as pag

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

url="http://192.168.29.216:8080/video"

cap = cv2.VideoCapture(0)
screen_w, screen_h = pag.size()

prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0
smoothening = 7

while True:
    success, img = cap.read()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

    # STEP 1 → Draw full hand
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # STEP 2 → Loop through all points
            for id, lm in enumerate(handLms.landmark):

                h, w, c = img.shape
                cx = int(lm.x * w)
                cy = int(lm.y * h)

        # STEP 3 → Highlight index finger tip
                if id == 8:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), -1)

                    mouse_x = int((w-cx) * screen_w / w)
                    mouse_y = int(cy * screen_h / h)

                    curr_x = prev_x + (mouse_x - prev_x) / smoothening
                    curr_y = prev_y + (mouse_y - prev_y) / smoothening
                    pag.moveTo(curr_x, curr_y)
                    prev_x, prev_y = curr_x, curr_y

    cv2.imshow("Finger Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break