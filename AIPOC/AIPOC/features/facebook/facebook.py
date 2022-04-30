from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
#for facebook
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

driver = webdriver.Chrome(chrome_options=opt, executable_path='chrome_driver/chromedriver.exe')
driver.get('https://www.facebook.com/')

username = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

username.send_keys('rootaccess369@gmail.com')
password.send_keys('FBotNew10!@')

submit_btn = driver.find_element_by_xpath('//*[@id="u_0_b"]')
submit_btn.click()
sleep(6)
#Photo upload
photo_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[3]/span/div')
photo_btn.click()
sleep(5)
post_btn = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]')
post_btn.click()
sleep(5)
pic_upload = driver.find_element_by_xpath("//*[@id='facebook']/body/div[3]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/span/div/div/div/div/div[1]/i")
pic_upload.click()
sleep(5)

#pyautogui
x,y = pyautogui.locateCenterOnScreen('pics/Screenshot 2020-11-22 105332.png')
pyautogui.click(x,y)
sleep(3)
pyautogui.write('G:\web scrap\pics', interval=0.25)
pyautogui.hotkey('enter')
sleep(3)
x,y = pyautogui.locateCenterOnScreen('pics/ok.png')
pyautogui.click(x,y)
sleep(3)
x,y = pyautogui.locateCenterOnScreen('pics/Screenshot 2020-11-22 105425.png')
pyautogui.click(x,y)
sleep(3)

post = driver.find_element_by_xpath('//*[@id="facebook"]/body/div[3]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div')
post.click()