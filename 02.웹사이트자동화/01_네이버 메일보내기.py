from selenium import webdriver
import time
import pyautogui
import pyperclip

browser = webdriver.Chrome("c:/chromedriver.exe")
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com/"

browser.implicitly_wait(10) # 페이지가 로딩될때까지 최대 10초 기다려줌
browser.maximize_window() # 화면 최대화
browser.get(url) # 페이지 열기

# ID 입력창
id = browser.find_element_by_css_selector("#id_line")
id.click()
pyperclip.copy('woalstm20')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# pwd 입력창
pwd = browser.find_element_by_css_selector("#pw_line")
pwd.click()
pyperclip.copy('zzams1029!')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# login  버튼
login_btn = browser.find_element_by_css_selector("#log\.login")
login_btn.click()
time.sleep(2)

#메일열기
browser.get("https://mail.naver.com/")
time.sleep(2)

#메일쓰기
mail_write = browser.find_element_by_css_selector("#nav_snb > div.btn_workset > a.btn_quickwrite._c1\(mfCore\|popupWrite\|new\)._ccr\(lfw\.write\)._stopDefault > strong > span")
mail_write.click()
time.sleep(2)

#받는사람
from_mail = browser.find_element_by_css_selector("#toInput").send_keys("woalstm20@naver.com")
time.sleep(2)

#제목
title_nm = browser.find_element_by_css_selector("#subject").send_keys("RPA 테스트")
time.sleep(2)

# iframe 안으로 들어가기
browser.switch_to.frame("se2_iframe")
#본문
contents_nm = browser.find_element_by_css_selector(".se2_inputarea").send_keys("RPA 테스트증입니다.")
time.sleep(2)

# iframe 밖으로 나오기
browser.switch_to.default_content()

#보내기
browser.find_element_by_css_selector("#sendBtn").click()
