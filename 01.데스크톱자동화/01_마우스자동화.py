import pyautogui

import time

# 1. 화면 크기 출력
#print(pyautogui.size())

# 2. 마우스 위치 출력
#time.sleep(2)
#print(pyautogui.position())

#  3. 마우스 이동
#pyautogui.moveTo(1028,1051)
#pyautogui.moveTo(979,1060,0.5) # 0.5 :  마우스가 좌표위치로가는 시간

# 4. 마우스 클릭
#pyautogui.click() # 왼쪽클릭
#pyautogui.click(button='right') # 오른쪽 클릭
#pyautogui.doubleClick() # 더블클릭
#pyautogui.click(clicks=3, interval=2 ) #3번 클릭 2초마다

# 5. 마우스 드래그
# 660,68 -> 546,73
pyautogui.moveTo(660,68, 2)
pyautogui.dragTo(546,73, 2)
