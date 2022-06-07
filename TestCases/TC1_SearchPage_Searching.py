import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import configuration as config
import common_methods as cm


def execute_tc(driver):
    print("TC1 started")
    if config.enable_video_recording:
        print("Video recording started")
        driver.start_recording_screen()  # start video recording

    # close the language selection page by clicking on the SKIP option
    driver.find_element(By.ID, "org.wikipedia:id/fragment_onboarding_skip_button").click()
    time.sleep(5)

    # open the search page
    driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Search"]').click()
    time.sleep(2)

    # click on the search field
    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc = "Search Wikipedia"]').click()

    touchaction = TouchAction(driver)
    search_list = config.search_article_list
    result_dict = {}
    itm_count = 0
    for itm in search_list:
        itm_count += 1
        # send search text to search field
        driver.find_element(By.ID, 'org.wikipedia:id/search_src_text').send_keys(itm)
        time.sleep(2)
        touchaction.tap(x=200, y=300).perform()  # select the first item from the search results
        time.sleep(5)
        ss_filename = "TC1_Search_result_" + cm.remove_space(itm) + "_" + time.strftime("%Y_%m_%d_%H%M%S")
        try:
            # close the donation popup message by pressing the NO THANKS option, if it displayed
            if driver.find_element(By.ID, 'org.wikipedia:id/view_announcement_container').is_displayed():
                driver.find_element(By.ID, 'org.wikipedia:id/view_announcement_dialog_action_negative').click()
        except NoSuchElementException:
            pass

        if config.enable_screenshots:
            cm.take_screenshot(driver, ss_filename)  # Take screenshot
            print("Screenshot taken")

        search_item = '"' + itm + '"'
        search_item_xpath = '//android.widget.TextView[@text=' + search_item + ']'

        try:
            if driver.find_element(By.XPATH, search_item_xpath).is_displayed():
                result_dict[itm_count] = {itm: "Pass"}
        except NoSuchElementException:
            result_dict[itm_count] = {itm: "Fail"}

        driver.back()  # Navigate to previous screen

    if driver.is_keyboard_shown():
        driver.back()  # hide the keyboard

    driver.back()  # Navigate to explore screen
    driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Explore"]').click()

    if config.enable_video_recording:
        video_path = config.ss_folder_path + ss_filename + ".mp4"
        video_raw_file = driver.stop_recording_screen()  # stop video recording
        print("Video recording stopped")
        cm.convert_to_base64(video_path, video_raw_file)
    print("TC1 stopped")
    return result_dict
