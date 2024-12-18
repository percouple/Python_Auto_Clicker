import pyautogui
from pynput.mouse import Listener

# Global vars for click operation location
inputX, inputY = 0, 0

# Define Listener
def on_click(x, y, button, pressed):
    
    # When clicked
    if pressed:
        
        # Assign input coordinates to the global vars
        inputX, inputY = x, y
        print(f"Clicked at coordinates: ({inputX}, {inputY})")
        return False
    
def main():
    print("Script running, click once to select auto-click subject")
    
    # Establish Listener
    with Listener(on_click=on_click) as listener:
        listener.join()
    
    # Take user input for number of clicks and the interval between clicks
    amount_of_clicks = int(input("Enter desired amount of clicks to perform: "))
    seconds_interval = float(input("Enter interval between clicks (seconds): "))
    
    # Execute click operation
    pyautogui.click(2000, 1300, clicks=amount_of_clicks, interval=seconds_interval, button='left')

if __name__ == "__main__":
    main()
