import time
from appium import webdriver
from TestCases import TC1_SearchPage_Searching as tc1
from TestCases import TC2_Clear_Search_History as tc2
from TestCases import TC3_Clear_Recent_Search_History as tc3
import configuration as config

if __name__ == '__main__':

    driver = webdriver.Remote(config.web_driver, config.desired_cap)  # create driver
    time.sleep(5)
    tc1_output = tc1.execute_tc(driver)  # TC1
    tc2_output = tc2.execute_tc(driver)  # TC2
    tc3_output = tc3.execute_tc(driver)  # TC3

    driver.quit()  # close driver

    print(' ')
    print("TC1 - Search functionality check")
    print(' ')
    for val in tc1_output:
        search_content = config.search_article_list[val-1]
        result = tc1_output.get(val).get(search_content)
        print(" " + search_content + " - " + result)

    print(' ')
    print("TC2 - Clear Search History - " + tc2_output)

    print(' ')
    print("TC3 - Clear Recent Search History - " + tc3_output)
