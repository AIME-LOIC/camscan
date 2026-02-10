import cv2
import time

def start_camera():
    cap = cv2.VideoCapture(0)
    line_y = 0
    
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        h, w, _ = frame.shape
        # Move scan line
        line_y = (line_y + 8) % h
        
        # Draw scanning line and overlay
        display_frame = frame.copy()
        cv2.line(display_frame, (0, line_y), (w, line_y), (0, 255, 0), 2)
        
        cv2.imshow("Place Code on Paper - Press 'S' to Scan", display_frame)
        
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite("captured_code.png", frame)
            cv2.destroyAllWindows()
            return "captured_code.png"
        elif key == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
    return None
