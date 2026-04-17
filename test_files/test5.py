import cv2
import mediapipe as mp
import pyautogui as pag

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
screen_w, screen_h = pag.size()

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


    cv2.imshow("Finger Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break