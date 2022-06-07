"""
This page contains all the configuration details
"""
device_udid = "3200ca824ba4567d"  # device UDID
app_local_path = "/Users/SKI39/Downloads/Wikipedia_v2_7_test_app.apk"  # local path
web_driver = "http://localhost:4723/wd/hub"  # appium server url
# screenshot and video local path
ss_folder_path = "C:/Users/SKI39/WikiPedia_Project/Screenshots/"

# Desired capabilities
desired_cap = {
    "platformName": "Android",
    "appium:deviceName": device_udid,
    "appium:app": app_local_path,
    "appium:appWaitActivity": "org.wikipedia.onboarding.InitialOnboardingActivity",
    "appium:appPackage": "org.wikipedia"
}

# search item list
search_article_list = ["Manchester United F.C.", "Liverpool F.C.", "Arsenal F.C.", "Chelsea F.C."]

enable_screenshots = False  # True to enable and False to disable the screenshot feature
enable_video_recording = True  # True to enable and False to disable the video recording feature


