import pyautogui
import pygetwindow as gw
import cv2
import numpy as np

def scan_specific_window(window_title):
    try:
        # Find the window by name (e.g., "Visual Studio Code")
        window = gw.getWindowsWithTitle(window_title)[0]
        
        if window:
            window.activate() # Bring to front
            
            # Take a screenshot of just that window's area
            screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
            
            # Convert to OpenCV format for processing
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            
            # Add the "Scan Line" effect to the static image for the vibe
            h, w, _ = frame.shape
            for y in range(0, h, 20):
                temp_frame = frame.copy()
                cv2.line(temp_frame, (0, y), (w, y), (0, 255, 0), 3)
                cv2.imshow("Scanning Window Content...", temp_frame)
                cv2.waitKey(20) # Play animation
            
            cv2.imwrite("window_capture.png", frame)
            cv2.destroyAllWindows()
            return "window_capture.png"
            
    except Exception as e:
        print(f"Window not found or error: {e}")
        return None
