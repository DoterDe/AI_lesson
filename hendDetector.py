import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

enter_pressed = False

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break


    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks: 
        for hand_landmarks in result.multi_hand_landmarks:  
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS) 

            finger_tips = [hand_landmarks.landmark[i] for i in [4, 8, 12, 16, 20]]
            finger_bases = [hand_landmarks.landmark[i - 2] for i in [4, 8, 12, 16, 20]]

            finger_up = [tip.y < base.y for tip, base in zip(finger_tips, finger_bases)]

            if all(finger_up) and not enter_pressed:
                cv2.putText(frame, "All Fingers Up! Pressing Enter & Scrolling", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                pyautogui.press("enter")
                pyautogui.scroll(-500)
                enter_pressed = True

            elif not all(finger_up):
                enter_pressed = False


    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
