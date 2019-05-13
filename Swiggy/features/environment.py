from splinter import browser
import logging,os

def before_all(context):
    pass

def before_scenario(context,scenario):
    #context.browser= browser.Browser('chrome')
    pass

def after_scenario(context,scenario):
    context.browser.quit()

def after_all(context):
    pass