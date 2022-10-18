import cv2

cap = cv2.VideoCapture(0)

while True:
    _, f = cap.read()
    
    cv2.imshow('output', f)
    
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows