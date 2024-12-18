import pyautogui
from pynput.mouse import Listener

inputX, inputY = 0, 0

# Define Listener
def on_click(x, y, button, pressed):
    
    # When clicked
    if pressed:
        
        # Assign input coordinates to the carry vars
        inputX, inputY = x, y
        print(f"Clicked at coordinates: ({inputX}, {inputY})")
        return False
    
def main():
    print("Script running correctly")
    
    # Establish Listener
    with Listener(on_click=on_click) as listener:
        listener.join()
        
    # Execute click operation
    # pyautogui.click(2000, 1300, clicks=1000, interval=.0001, button='left')

if __name__ == "__main__":
    main()
