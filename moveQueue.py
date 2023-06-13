import pyautogui
import time
import random


# Define the distance to move the cursor
distance = 30

# Define the number of times to repeat the movement
num_repeats = 10000

# Move the cursor left and right and click
for i in range(num_repeats):
    # Move the cursor to the left

    random_numberX = random.randint(1,5)
    random_numberY = random.randint(1,5)

    #klikne mapo
    pyautogui.rightClick(1780 + random_numberX, 943 + random_numberY)
    pyautogui.rightClick(1780 + random_numberX, 943 + random_numberY)
    
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

    pyautogui.leftClick(1400, 500)

    #accept queue
    pyautogui.leftClick(930, 650)

    #klikne na par chempov
    pyautogui.leftClick(1100, 350)
    pyautogui.leftClick(1050, 350)
    pyautogui.leftClick(1000, 350)
    pyautogui.leftClick(950, 350)
    pyautogui.leftClick(900, 350)
    pyautogui.leftClick(850, 350)
    

    # play again, lock in champ
    
    
    pyautogui.leftClick(930, 720)
    pyautogui.leftClick(930, 760)
    pyautogui.leftClick(850, 770)

    

    
    print(str(i) + ". move \n")
    time.sleep(3)

