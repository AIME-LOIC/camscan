import scanner
import ocr_processor
import ai_expert

def run_app():
    print("Step 1: Opening Camera...")
    img_path = scanner.start_camera()
    
    if img_path:
        print("Step 2: Extracting text from paper...")
        raw_code = ocr_processor.get_text_from_image(img_path)
        
        print(f"--- Scanned Content ---\n{raw_code}\n-----------------------")
        
        print("Step 3: Asking AI for fixes...")
        solution = ai_expert.get_code_fix(raw_code)
        
        print("\n=== DEBUGGER RESULTS ===")
        print(solution)
    else:
        print("Scan cancelled.")

if __name__ == "__main__":
    run_app()
