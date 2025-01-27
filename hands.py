import cv2
import mediapipe as mp

import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):   #to get the landmarks with id, #the id will be storted the serial numbers
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w),int(lm.y*h)      #to get the pixals
                print(id,cx,cy)
                # if id ==5:                              #if we don't use the if condition then it draw at every landmarks
                cv2.circle(img,(cx,cy), 10, (255,0,355),cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms,mpHands.HAND_CONNECTIONS)  #to join the line to join the landmarks

    cTime = time.time()   
    fps = 1/(cTime-pTime)
    pTime =cTime

    cv2.putText(img,str(int(fps)),(18,78),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,255),3)  #to print the time of the frame 

    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
