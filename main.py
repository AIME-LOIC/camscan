import scanner        # Your camera script
import window_scanner # Your new window script
import ocr_processor
import ai_expert

def run_app():
    print("Select Mode:")
    print("1. Scan Paper (Camera)")
    print("2. Scan Window (Digital)")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        img_path = scanner.start_camera()
    else:
        title = input("Enter the window name (e.g., 'Notepad' or 'Code'): ")
        img_path = window_scanner.scan_specific_window(title)
    
    if img_path:
        print("Extracting code...")
        raw_code = ocr_processor.get_text_from_image(img_path)
        
        print(f"--- Captured Code ---\n{raw_code}\n")
        
        print("AI is analyzing for bugs...")
        solution = ai_expert.get_code_fix(raw_code)
        
        print("\n=== AI DEBUGGER FIXES ===")
        print(solution)

if __name__ == "__main__":
    run_app()
