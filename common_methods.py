import base64
import os
import configuration as config


# Remove space from string
def remove_space(string):
    return string.replace(" ", "")


# Convert video file into base64
def convert_to_base64(save_video_path, video_raw_file):
    filepath = os.path.join(save_video_path)
    with open(filepath, "wb") as vd:
        vd.write(base64.b64decode(video_raw_file))


# Take screenshot
def take_screenshot(driver, filename):
    ss_path = config.ss_folder_path + filename + ".png"
    driver.save_screenshot(ss_path)  # save the screenshot
