import cv2
import mediapipe as mp
import pyautogui as pag
import math
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

url="http://192.168.29.216:8080/video"

cap = cv2.VideoCapture(0)
screen_w, screen_h = pag.size()

prev_x, prev_y = 0, 0
curr_x, curr_y = 0, 0
smoothening = 7

x1,x2=0,0
y1,y2=0,0
x3,y3=0,0
x4,y4=0,0
x5,y5=0,0

last_click_time = 0
click_delay = 0.5

frameR = 100

prev_scroll_y = 0
scroll_threshold = 15

pinch_start_time = 0
dragging = False
drag_delay = 0.7

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

                # scroll condition
                scroll_length = math.hypot(x3 - x2, y3 - y2)

                if y2 != 0 and y3 != 0 and scroll_length < 20:
                    current_scroll_y = (y2 + y3) // 2
                    diff = prev_scroll_y - current_scroll_y

                    if abs(diff) > scroll_threshold:
                        pag.scroll(int(diff * 3))
                        prev_scroll_y = current_scroll_y

                h, w, c = img.shape
                cx = int(lm.x * w)
                cy = int(lm.y * h)

                cv2.rectangle(img, (frameR, frameR), (w-frameR, h-frameR), (0,255,0), 2)


        # STEP 3 → Highlight index finger tip
                if id == 8:   #index finger tip

                    mouse_x = int((w - cx - frameR) * screen_w / (w - 2*frameR))
                    mouse_y = int((cy - frameR) * screen_h / (h - 2*frameR))

                    curr_x = prev_x + (mouse_x - prev_x) / smoothening
                    curr_y = prev_y + (mouse_y - prev_y) / smoothening
                    pag.moveTo(curr_x, curr_y)
                    prev_x, prev_y = curr_x, curr_y

                    x2, y2 = cx, cy

                if id == 4:  #thumb tip
                    x1, y1 = cx, cy

                if id==12:   #middle finger tip
                    x3,y3 = cx, cy

                if id==16:   #ring finger tip
                    x4,y4 = cx, cy

                if id==20:   #pinky finger tip
                    x5,y5 = cx, cy

                length = math.hypot(x2 - x1, y2 - y1)   #left click condition
                if length < 40:
                    current_time = time.time()

                    if current_time - last_click_time > click_delay:
                        pag.click()
                        last_click_time = current_time
                    
                length2 = math.hypot(x3-x1, y3-y1)   #right click condition
                if length2 < 40:
                    current_time = time.time()

                    if current_time - last_click_time > click_delay:
                        pag.rightClick()
                        last_click_time = current_time

                length3 = math.hypot(x4-x1,y4-y1)    #double click condition
                if length3 < 40:
                    current_time = time.time()

                    if current_time - last_click_time > click_delay:
                        pag.doubleClick()
                        last_click_time = current_time
                
    cv2.imshow("Finger Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break