import pyautogui
import time
import random
import keyboard


num_of_repeats = 100
stop_execution = False

def on_key_press(event):
    global stop_execution
    if event.name == '9':
        stop_execution = True
        print("Aborted")

keyboard.on_press(on_key_press)

screenWidth, screenHeight = pyautogui.size()

screenCenterX = screenWidth / 2
screenCenterY = screenHeight / 2



for i in range(num_of_repeats): 

    if stop_execution:
        break

    j = 0


    while "League of Legends (TM) Client" in pyautogui.getActiveWindowTitle(): 
        if stop_execution:
            break

        league_window = pyautogui.getWindowsWithTitle("League of Legends (TM) Client")[0]
        league_window_x = league_window.left
        league_window_y = league_window.top
        league_window_width = league_window.width
        league_window_height = league_window.height

                
        #print(str(i) + "." + str(j))
        #j += 1
        
        random_numberX = random.randint(1,15)
        random_numberY = random.randint(1,10)

        # clicks on the map
        pyautogui.rightClick(screenCenterX + league_window_width/4 + league_window_width/8 + league_window_width/32 + league_window_width/128 + random_numberX, 
                             screenCenterY + league_window_height/4 + league_window_height/16 + league_window_height/32 + league_window_height/128 + random_numberY)
        
        pyautogui.rightClick(screenCenterX + league_window_width/4 + league_window_width/8 + league_window_width/32 + league_window_width/128 + random_numberX, 
                             screenCenterY + league_window_height/4 + league_window_height/16 + league_window_height/32 + league_window_height/128 + random_numberY)
        
        
        # alt tabs because otherwise it doesn't work for some reason
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')

        time.sleep(3)
        pyautogui.leftClick(screenCenterX + league_window_width/4 + league_window_width/8 + league_window_width/32 + league_window_width/128 + random_numberX, 
                             screenCenterY + league_window_height/4 + league_window_height/16 + league_window_height/32 + league_window_height/128 + random_numberY)

    while "League of Legends (TM) Client" not in pyautogui.getActiveWindowTitle():
        if stop_execution:
            break


        #print(str(i) + "." + str(j))
        #j += 1

        pyautogui.leftClick(1400, 500)

        #accept queue
        pyautogui.leftClick(930, 650)

        # select a couple of champions
        pyautogui.leftClick(1100, 350)
        pyautogui.leftClick(1050, 350)
        pyautogui.leftClick(1000, 350)
        pyautogui.leftClick(950, 350)
        pyautogui.leftClick(900, 350)
        pyautogui.leftClick(850, 350)
        

        # play again, lock in, champ
        
        
        pyautogui.leftClick(930, 720)
        pyautogui.leftClick(930, 760)
        pyautogui.leftClick(850, 770)

        time.sleep(3)

9