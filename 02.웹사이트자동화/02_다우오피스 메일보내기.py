from selenium import webdriver
import time
import pyautogui
import pyperclip

browser = webdriver.Chrome("c:/chromedriver.exe")
url = "https://ais.daouoffice.com/login"

browser.implicitly_wait(10) # 페이지가 로딩될때까지 최대 10초 기다려줌
browser.maximize_window() # 화면 최대화
browser.get(url) # 페이지 열기

# ID 입력창
id = browser.find_element_by_css_selector("#username").send_keys("min0904")
time.sleep(2)

# pwd 입력창
pwd = browser.find_element_by_css_selector("#password").send_keys("Woatm1029!")
time.sleep(2)

# login  버튼
login_btn = browser.find_element_by_css_selector("#login_submit")
login_btn.click()
time.sleep(2)


#메일열기
browser.get("https://ais.daouoffice.com/app/mail")
time.sleep(2)

#메일쓰기

browser.switch_to.frame("mail-viewer")

mail_write = browser.find_element_by_css_selector("#mailLeftMenuWrap > section.function > a")
mail_write.click()
time.sleep(2)

#받는사람
from_mail = browser.find_element_by_css_selector("#writeMyself").click()
time.sleep(1)

#제목
title_nm = browser.find_element_by_css_selector("#subject").send_keys("RPA 테스트")
time.sleep(2)

#본문
browser.switch_to.frame("dext_frame_smartEditor")
browser.switch_to.frame("dext5_design_smartEditor")
contents_nm = browser.find_element_by_css_selector("#dext_body").send_keys("RPA 테스트증입니다.")
time.sleep(2)

# iframe 밖으로 나오기
browser.switch_to.default_content()
browser.switch_to.frame("mail-viewer")
#보내기
browser.find_element_by_css_selector("#write_toolbar_wrap > div.critical > a.btn_major_s > span.txt").click()
time.sleep(2)
browser.find_element_by_css_selector("#gpopupLayer > footer > a.btn_major_s > span.txt").click()