import time
from selenium.common import NoSuchElementException
import configuration as config
from selenium.webdriver.common.by import By
import common_methods as cm


def check_recent_search_history_page(driver):
    if driver.find_element(By.ID, 'org.wikipedia:id/search_empty_container').is_displayed():
        return "Pass"


def execute_tc(driver):
    print("TC3 started")
    ss_filename = "TC3_Clear_Recent_Search_History" + time.strftime("%Y_%m_%d_%H%M%S")
    # tc_result = ""

    if config.enable_video_recording:
        driver.start_recording_screen()  # start video recording
        print("Video recording started")

    # open the search container from Explore screen
    driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()
    time.sleep(2)

    try:
        tc_result = check_recent_search_history_page(driver)  # check whether the recent search is empty or not
        if config.enable_screenshots:
            cm.take_screenshot(driver, ss_filename)  # Take screenshot
            print("Screenshot taken")
        return tc_result
    except NoSuchElementException:
        pass

    # click on the recent search delete button
    driver.find_element(By.ID, 'org.wikipedia:id/recent_searches_delete_button').click()
    time.sleep(2)

    driver.find_element(By.ID, 'android:id/button1').click()  # click the YES option on the confirmation popup

    try:
        # check whether the recent search history is cleared or not
        tc_result = check_recent_search_history_page(driver)

        if config.enable_screenshots:
            cm.take_screenshot(driver, ss_filename)  # Take screenshot
            print("Screenshot taken")
    except NoSuchElementException:
        tc_result = "Fail"

    if driver.is_keyboard_shown():
        driver.back()  # hide the keyboard

    driver.back()  # Navigate to previous screen

    if config.enable_video_recording:
        video_path = config.ss_folder_path + ss_filename + ".mp4"
        video_raw_file = driver.stop_recording_screen()  # stop video recording
        print("Video recording stopped")
        cm.convert_to_base64(video_path, video_raw_file)

    print("TC3 stopped")
    return tc_result
