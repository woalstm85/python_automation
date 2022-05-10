import pyautogui
import pyperclip

# 1. 키보드 입력(문자 : 영문)
# pyautogui.write('startcording')
# pyautogui.write('startcording', interval=0.25)

# 2. 키보드 입력(키)
# pyautogui.press('enter')
# pyautogui.press('up')

# 3. 키보드 입력(다중)

# pyautogui.hotkey('ctrl', 'c') # 복사

# 4. 키보드 입력(한글)
pyperclip.copy('#한글입력')
pyautogui.hotkey('ctrl', 'v')
#한글입력#한글입력#한글입력#한글입력