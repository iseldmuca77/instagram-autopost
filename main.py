import code
import email
from shutil import ExecError
from xml.dom.minidom import Element
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


desired_cap ={
    "deviceName": "be39gfbe9436",
    "platformName": "Android"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))


description = 'Description'


def main():
    n = 1
    for i in range(6):
        coping_post(n)
        Posting(n)
        n+=1


def coping_post(m):
    #repost_app_icon = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Repost"]')
    #repost_app_icon.click()
    #time.sleep(randint(7,8))

    if m == 1:
        repost_post = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView[1]')
        repost_post.click()
        time.sleep(randint(8,9))
    elif m == 2:
        repost_post = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.TextView[1]')
        repost_post.click()
        time.sleep(randint(8,9))
    elif m == 3:
        repost_post = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.view.ViewGroup/android.widget.TextView[1]')
        repost_post.click()
        time.sleep(randint(8,9))
    elif m == 4:
        actions.w3c_actions.pointer_action.move_to_location(553, 1430)   
        actions.w3c_actions.pointer_action.pointer_down()   
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(555, 503)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(randint(7,8))
        repost_post = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.TextView[1]')
        repost_post.click()
        time.sleep(randint(8,9))
    elif m == 5:
        actions.w3c_actions.pointer_action.move_to_location(553, 1430)   
        actions.w3c_actions.pointer_action.pointer_down()   
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(555, 503)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(randint(7,8))
        repost_post = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.view.ViewGroup/android.widget.TextView[1]')
        repost_post.click()
        time.sleep(randint(8,9))
    elif m == 6:
        actions.w3c_actions.pointer_action.move_to_location(553, 1430)   
        actions.w3c_actions.pointer_action.pointer_down()   
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(555, 503)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(randint(7,8))
        repost_post = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.view.ViewGroup/android.widget.TextView[1]')
        repost_post.click()
        time.sleep(randint(8,9))
    else:
        print('helo')
    
    post_to_feed_button = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.Button')
    post_to_feed_button.click()
    time.sleep(randint(9,10))


def Posting(k):
    if k == 1 or k == 2 or k == 3:
        try:
            new_post_btn = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Create a post, story, reel or live video."]')
            new_post_btn.click()
        except Exception as e:
            driver.press_keycode(187)
            time.sleep(randint(7,8))
            x = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.android.systemui.recents.views.TaskStackView/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView')
            x.click()
            time.sleep(randint(7,8))
            new_post_btn = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Create a post, story, reel or live video."]')
            new_post_btn.click()
            time.sleep(randint(7,8))

        next_btn1 = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Next"]')
        next_btn1.click()
        time.sleep(randint(8,9))
                                              
        next_btn2 = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Next"]')
        next_btn2.click()
        time.sleep(randint(7,8))
        post_caption = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText')
        #post_caption.click()
        time.sleep(randint(1,2))

        post_caption.send_keys(description)
        time.sleep(randint(7,8))

        share_btn = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Share"]')
        share_btn.click()
        time.sleep(randint(30,40))
    else:
        try:
            next_btn1 = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Next"]')
            next_btn1.click()
            time.sleep(randint(8,9))
        except Exception as e:
            driver.press_keycode(187)
            time.sleep(randint(7,8))
            x = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.android.systemui.recents.views.TaskStackView/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView')
            x.click()
            time.sleep(randint(7,8))
            next_btn1 = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Next"]')
            next_btn1.click()
            time.sleep(randint(8,9))


        next_btn2 = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Next"]')
        next_btn2.click()
        time.sleep(randint(7,8))

        post_caption = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.EditText')
        #post_caption.click()
        time.sleep(randint(1,2))

        post_caption.send_keys(description)
        time.sleep(randint(7,8))

        share_btn = driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Share"]')
        share_btn.click()
        time.sleep(randint(30,40))


    driver.press_keycode(187)
    time.sleep(randint(7,8))
    kthehu_repost = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Repost"]')
    kthehu_repost.click()
    time.sleep(randint(9,10))
    kthehu_back = driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Navigate up"]')
    kthehu_back.click()
    time.sleep(randint(9,10))

if __name__ == "__main__":
    main()
