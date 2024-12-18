import pyautogui
import sys
from pynput.mouse import Listener

# Global vars for click operation location
inputX, inputY, primed = 0, 0, False

# Define click Listener
def on_click(x, y, button, pressed):
    
    # Declare global var so we can modify later in the function
    global primed
    
    # When clicked
    if pressed:
        
        # Assign input coordinates to the global vars
        inputX, inputY = x, y
        primed = True
        print(f"Clicked at coordinates: ({inputX}, {inputY})")
        return False
    
# Function to detect mouse movement and kill the script
def on_move(x, y):
    global inputX, inputY
    
    if inputX is not None and inputY is not None and primed:
        if (x != inputX) or (y != inputY):  # If the mouse has moved
            print(f"Mouse moved to ({x}, {y}). Exiting script.")
            sys.exit("EXITING IHTIH  DN")  # Kill the script
            return False
        
    inputX, inputY = x, y  # Update the last mouse position
    
def main():
    print(f"\nScript running, click once to select auto-click subject")
    
    
    # Establish Listener for click location input
    with Listener(on_click=on_click) as click_listener:
        click_listener.join()
    
    # Establish Listener for mouse movement cancellation
    with Listener(on_move=on_move) as mouse_move_listener:
        mouse_move_listener.join()
        
    # Take user input for number of clicks and the interval between clicks
    amount_of_clicks = int(input("\nEnter desired amount of clicks to perform: "))
    seconds_interval = float(input("Enter interval between clicks (seconds): "))
    
    
    # Execute click operation
    pyautogui.click(2000, 1300, clicks=amount_of_clicks, interval=seconds_interval, button='left')
    
if __name__ == "__main__":
    main()
