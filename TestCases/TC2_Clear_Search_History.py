import time
from selenium.common import NoSuchElementException
import configuration as config
from selenium.webdriver.common.by import By
import common_methods as cm


def check_empty_history_page(driver):
    if driver.find_element(By.ID, 'org.wikipedia:id/history_empty_image').is_displayed():
        return "Pass"


def execute_tc(driver):
    print("TC2 started")
    ss_filename = "TC2_Clearing_Search_History" + time.strftime("%Y_%m_%d_%H%M%S")
    # tc_result = ""

    if config.enable_video_recording:
        print("Video recording started")
        driver.start_recording_screen()  # start video recording

    # open the search page
    driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Search"]').click()
    time.sleep(2)

    try:
        tc_result = check_empty_history_page(driver)  # check whether the history is already empty or not
        if config.enable_screenshots:
            cm.take_screenshot(driver, ss_filename)  # Take screenshot
            print("Screenshot taken")
        return tc_result
    except NoSuchElementException:
        pass

    driver.find_element(By.ID, 'org.wikipedia:id/history_delete').click()  # click on the delete history button
    time.sleep(2)

    driver.find_element(By.ID, 'android:id/button1').click()  # click YES on the clear browsing history popup

    try:
        tc_result = check_empty_history_page(driver)  # check whether the history cleared or not

        if config.enable_screenshots:
            cm.take_screenshot(driver, ss_filename)  # Take screenshot
            print("Screenshot taken")
    except NoSuchElementException:
        tc_result = "Fail"

    # Navigate to explore screen
    driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Explore"]').click()

    if config.enable_video_recording:
        video_path = config.ss_folder_path + ss_filename + ".mp4"
        video_raw_file = driver.stop_recording_screen()  # stop video recording
        print("Video recording stopped")
        cm.convert_to_base64(video_path, video_raw_file)

    print("TC2 stopped")
    return tc_result
