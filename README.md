*****************************************************************

UI Testing (Android Mobile)

*****************************************************************

Language: Python

Framework: Appium 

IDE: PyCharm 2021.3 (Community Edition)

This project contains 3 test cases

1. To check the search functionality
2. To check the clear history functionality
3. To check the clear recent search history functionality from the Explore page

These test cases are available under the "TestCases" folder

All the settings are available in the "configuration.py"

To run this test you have to update the below in "configuration.py"

1. device_udid - update the test device UDID
2. app_local_path - local apk file path
3. web_driver - appium server URL
4. ss_folder_path - local folder path to save the screenshots and video recordings

Other settings

1. search_article_list -  It contains the article name for the first test cases
2. enable_screenshots - This is to enable/disable the screenshots feature
3. enable_video_recording - This is to enable/disable the video recordings feature

How to run?

1. Connect the testing android mobile (developer mode is on)
2. Start the Appium server
3. Update the fields like device_udid, app_local_path, web_driver and ss_folder_path as mentioned above
4. Run the main.py 
