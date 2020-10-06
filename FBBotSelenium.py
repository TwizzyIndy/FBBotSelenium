import selenium
import os
from selenium.webdriver.common.keys import Keys
import time
import json

class FBBot():
    def __init__(self, email, password):
        self.browser = selenium.webdriver.Chrome("chromedriver")
        self.email = email
        self.password = password

    def login(self):
        self.browser.get('https://mbasic.facebook.com')

        # two input fields
        emailField = self.browser.find_element_by_name('email')
        passwordField = self.browser.find_element_by_name('pass')

        emailField.send_keys(self.email)
        passwordField.send_keys(self.password)

        # get login button
        loginButton = self.browser.find_element_by_name('login')

        # click login button
        loginButton.click()
        time.sleep(2)

    def likePage(self, pageURL):
        self.browser.get(pageURL)

        # get like reference link

        likeButton = self.browser.find_element_by_xpath('//*[@id="sub_profile_pic_content"]/div/div[2]/table/tbody/tr/td[1]/a')
        refLink = likeButton.get_attribute('href')
        
        # debug
        # print(refLink)

        if refLink.startswith('https://mbasic.facebook.com/a/profile.php?fan&'):
            print("Liking the page.")
        else:
            print("Unliking the page.")
        

        # execute it to like/unlike it
        self.browser.get(refLink)

    def followPage(self, pageURL):

        self.browser.get(pageURL)

        followButton = self.browser.find_element_by_xpath('//*[@id="pages_follow_action_id"]')
        refLink = followButton.get_attribute('href')

        # debug
        #print(refLink)

        if refLink.startswith('https://mbasic.facebook.com/a/subscriptions/add'):
            print('Following the page.')
        else:
            print('Unfollowing the page.')
        
        # execute it to follow/unfollow it
        self.browser.get(refLink)

    def postStatusToFeed(self, message):
        self.browser.get('https://mbasic.facebook.com/home.php')

        # post message input

        statusInput = self.browser.find_element_by_name('xc_message')
        statusInput.send_keys(message)

        # Post button
        postButton = self.browser.find_element_by_name('view_post')
        postButton.click()

def get_credentials():

    with open('credentials.json') as json_file:
        data = json.load(json_file)
        return data
    return

def main():

    # get credentials from json
    user_infos = get_credentials()

    # initialize login process with given infos
    bot = FBBot(user_infos['email'], user_infos['password'])
    bot.login()
    
    bot.likePage('https://mbasic.facebook.com/tharngeIV/')
    bot.followPage('https://mbasic.facebook.com/ncybersec')
    
    bot.postStatusToFeed('testttt')

    return



if __name__ == "__main__":
    main()