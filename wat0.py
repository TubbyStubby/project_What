from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time

def getQr(browser):
    print('\n--Wait for qr image--\n')
    browser.save_screenshot('qr.png')
    Image.open('qr.png').show()
    tem = input('Press enter if scanned.')

def start():
    options = wd.FirefoxOptions()
    options.headless = True
    driver = wd.Firefox(options=options, executable_path=r'geckodriver.exe')
    driver.get('https://web.whatsapp.com')
    return driver

def sNS(name,driver):
    s_bar = driver.find_element_by_tag_name('input')
    s_bar.click()
    s_bar.send_keys(name)
    time.sleep(1)
    #pane_side = driver.find_element_by_id('pane-side')
    c_name = driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div').get_attribute('class')
    l = driver.find_elements_by_class_name(c_name)
    tem = 0
    f = l[0]
    for i in l:
        k = i.value_of_css_property('transform')
        tem2 = int(k[k.rfind(',')+2:-1])
        if  tem2 < tem and tem2 > 0:
            f = i
    i.click()
##    f=0
##    for i in l:
##        if name.lower() in str(i.get_attribute('title')).lower():
##            i.click()
##            f=1
##            break
##    if f is 0:
##        print('Contact not found.')

def recentSent(brow):
    main = brow.find_element_by_id('main')
    l = main.find_elements_by_class_name('message-out')
    xl = [i.get_attribute('innerText') for i in l]
    return xl

def recentRcvd(brow):
    main = brow.find_element_by_id('main')
    l = main.find_elements_by_class_name('message-in')
    xl = [i.get_attribute('innerText') for i in l]
    return xl[len(xl)-2]

def lastSent(brow):
    main = brow.find_element_by_id('main')
    l = main.find_elements_by_class_name('message-out')
    try:
        return l[-1].get_attribute('innerText')
    except:
        return ''

def lastRcvd(brow):
    main = brow.find_element_by_id('main')
    l = main.find_elements_by_class_name('message-in')
    try:
        return l[-1].get_attribute('innerText')
    except:
        return '\0'

def untilNew(brow,last):
    last_chk = lastRcvd(brow)
    if last_chk == last:
        while last_chk == last:
            time.sleep(2)
            last_chk = lastRcvd(brow)
    log = open('log.txt','a+')
    log.write('[rcvd '+last_chk.split('\n')[1]+']'+last_chk.split('\n')[0]+'\n')
    log.close()
    return last_chk

def sendMsg(msg,driver):
    input_area = driver.find_element_by_xpath("//*[contains(text(), 'Type a message')]")
    input_area = input_area.find_element_by_xpath("following-sibling::*")
    input_area.click()
    input_area.send_keys(msg,Keys.ENTER)
    msg = lastSent(driver)
    log = open('log.txt','a+')
    log.write('[sent '+msg.split('\n')[1]+']'+msg.split('\n')[0]+'\n')
    log.close()

def quit(brow):
    brow.quit()

# browser = start()
# getQr(browser)
# namae = input('Enter contact name: ').lower()
# sNS(namae, browser)
# print('last sent: ',lastSent(browser))
# print('last recieved: ',lastRcvd(browser))
# sendMsg('new test',browser)
# print('last sent: ',lastSent(browser))
# i=1
# quit(browser)
# while True:
#    l = lastRcvd(browser)
#    print('main:',l)
#    s = untilNew(browser,l)
#    sendMsg(str(i),browser)
#    i+=1