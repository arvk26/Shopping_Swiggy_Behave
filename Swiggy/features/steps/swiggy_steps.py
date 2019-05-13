#from behave import given, when, then
from behave import *
from selenium import webdriver
from splinter import browser
from selenium.webdriver.support import expected_conditions as expectThat
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time, logging

@step('open browser "{browser_name}" and move to swiggy website')
def open_browser_move(context,browser_name):
    if browser_name.lower()=='chrome':
        context.browser= browser.Browser('chrome')
    else:
       context.browser= browser.Browser()
    context.wait= WebDriverWait(context.browser.driver,90)    #Default ui wait for 90 seconds
    context.browser.driver.maximize_window()
    context.browser.visit('https://www.swiggy.com')

@step('Enter location as "{loc}" and choose correct address')
def choose_exact_location(context,loc):
    print('Entering location as %s'%loc)
    exact_location= str(loc)+', Karnataka, India'
    print('Exact Location:-%s'%exact_location)
    context.browser.fill("location",loc)
    xpath= "//div[@class='_3lmRa']//span[@class='_2W-T9'][contains(text(),'"+exact_location+"')]"   #Enter and choose exact location
    print('Waiting for first option to be visible and then select it-%s'%xpath)
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    context.browser.driver.find_element_by_xpath(xpath).click()
    print('Wait until search icon is present and visible')
    xpath= "//span[contains(text(),'Search')]"
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))

@step('Search restaurent "{restaurent_name}"')
def search_restaurent(context,restaurent_name):
    print('Searching for restaurent name')
    xpath= "//span[contains(text(),'Search')]"
    #self.obj.wait_until_page_contains_element(xpath,timeout=90)          #Wait till Search option comes up
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    context.browser.driver.find_element_by_xpath(xpath).click()
    xpath= "//input[@placeholder='Search for restaurants or dishes']"          #Write name of restaurent
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    context.browser.driver.find_element_by_xpath(xpath).send_keys(restaurent_name)
    xpath= "//div[contains(text(),'Bite Me')]"
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    xpath= "//div[contains(text(),'"+restaurent_name+"')]"
    context.browser.driver.find_element_by_xpath(xpath).click()
    xpath= "//h2[contains(text(),'Recommended')]"           #Wait till text is shown and loaded fully
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))

@step('Order item "{item}" with quantity "{item_cnt}"')
def select_items_to_order(context, item, item_cnt):
    print('Choose item to add-%s-%s' % (item, item_cnt))
    xpath= "//div[@class='_2SyqU'][contains(text(),'" + item + "')]/../../../../div[3]/div[2]/div[text()='ADD']"  # Click on Add button
    print('Adding Item with xpath-%s' % xpath)
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    context.browser.driver.find_element_by_xpath(xpath).click()
    xpath= "//div[@class='_2SyqU'][contains(text(),'" + item + "')]/../../../../div[3]/div[2]/div[4]"  # Get cake count, Will use it to order
    count= context.browser.driver.find_element_by_xpath(xpath).text
    print('count is:%s' % count)
    time.sleep(5)
    if int(item_cnt) > int(count):
        loop_cnt = int(item_cnt) - int(count)
        plus_xpath= "//div[@class='_2SyqU'][contains(text(),'" + item + "')]/../../../../div[3]/div[2]/div[2]"  # Click on + sign to add
        print(plus_xpath)
        for c in range(int(loop_cnt)):
            print('Click plus sign-%s' % c)
            context.browser.driver.find_element_by_xpath(plus_xpath).click()
    time.sleep(10)

@step('Checkout and fetch all items present there')
def checkout_and_get_all_items_on_checkout_page(context):
    print('Checkout now..')
    xpath= "//div[@class='_1gPB7']"        #click on checkout button
    context.browser.driver.find_element_by_xpath(xpath).click()
    xpath= "//div[@class='_2pdCL']/div"
    print(xpath)
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    count_of_itemtype= len(context.browser.driver.find_elements_by_xpath(xpath))
    print(count_of_itemtype)
    i= 1
    context.item_hash= {}
    baseurl= "//div[@class='_2pdCL']"
    while i<=int(count_of_itemtype):
        itemurl= baseurl+"/div["+str(i)+"]/div[1]/div[2]"                    #Get name of item
        context.wait.until(expectThat.visibility_of_element_located((By.XPATH, itemurl)))
        itemname= context.browser.driver.find_element_by_xpath(itemurl).text
        itemurlcount= baseurl+"/div["+str(i)+"]/div[2]/div/div[1]/div[4]"    #Get count of item
        context.wait.until(expectThat.visibility_of_element_located((By.XPATH, itemurlcount)))
        itemcount= context.browser.driver.find_element_by_xpath(itemurlcount).text
        #create a hash
        context.item_hash[itemname]= itemcount                          #create hash with item and count
        i= i+1
    print('Hash of items and count on checkout page-%s'%context.item_hash)
    time.sleep(6)

@step('Verify item "{item}" is present with count "{item_cnt}" on checkout page')
def verify_items_on_checkout_page(context,item,item_cnt):
    print('Verify item count on checkout page for:-%s'%item)
    print('Expected count-%s Actual count-%s'%(item_cnt,context.item_hash[item]))
    if int(item_cnt)!=int(context.item_hash[item]):
        raise Exception('Item count not matching for %s .. Failure...'%item)
    else:
        print('Item count matching for %s .. Great...'%item)

@step('Enter details as mobileno "{mobileno}" and name "{name}" and email "{email}" and password "{password}" while signup')
def signup(context,mobileno,name,email,password):
    print('Sign up..')
    xpath= "//div[contains(text(),'SIGN UP')]"      #Click on signup button, class is static/constant
    print(xpath)
    context.browser.driver.find_element_by_xpath(xpath).click()
    #Input mobile number
    context.browser.fill("mobile",mobileno)
    context.browser.fill("name",name)
    context.browser.fill("email",email)
    context.browser.fill("password",password)
    #Click on referal code
    xpath= "//div[@class='_3GOZo']"                 #click on referal code icon, class is static/constant
    print('Xpath is:%s'%xpath)
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    context.browser.driver.find_element_by_xpath(xpath).click()
    #click on continue signup
    xpath= "//a[@class='_2REYC']"                   #click on continue button, class is static/constant
    print('Xpath is:%s'%xpath)
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    context.browser.driver.find_element_by_xpath(xpath).click()
    xpath= "//input[@id='email']/../label"
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    label= context.browser.driver.find_element_by_xpath(xpath).text
    print(label)

@step('Verify email error and take screenshot')
def verify_email_error_and_take_screenshot(context):
    xpath= "//input[@id='email']/../label"
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    label= context.browser.driver.find_element_by_xpath(xpath).text
    if str(label)=='Invalid email address':                      #Compare email box error label
        print("seems Error message related to email field")
        context.browser.driver.get_screenshot_as_png()

@step('On checkout page update item "{item}" with quantity as "{item_cnt}"')
def update_items_during_checkout(context,item,item_cnt):
    print('Choose item to update with count-%s-%s'%(item,item_cnt))
    xpath= "//div[contains(text(),'"+item+"')]/../../div[2]/div/div[1]/div[4]"   #xpath used to count no of items in checkout page
    count= context.browser.driver.find_element_by_xpath(xpath).text
    print('count is:%s'%count)
    if int(count)>int(item_cnt):
        loop_cnt= int(count)-int(item_cnt)
        minus_xpath= "//div[contains(text(),'"+item+"')]/../../div[2]/div/div[1]/div[3]"    #Update item count in cart
        print(minus_xpath)
        for c in range(int(loop_cnt)):
            print('Click Minus sign during checkout-%s'%c)
            context.browser.driver.find_element_by_xpath(xpath).click()
    #Wait until loading is done if any
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))
    xpath= "//div[contains(text(),'"+item+"')]/../../div[2]/div/div[1]/div[4]"
    context.wait.until(expectThat.visibility_of_element_located((By.XPATH, xpath)))

@step(u'I take a screenshot')
def take_screenshot(context):
    context.browser.driver.get_screenshot_as_png()
