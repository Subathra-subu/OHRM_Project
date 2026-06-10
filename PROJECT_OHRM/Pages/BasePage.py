from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:

    search      = "//input[@class='oxd-input oxd-input--active']"
    Admin       = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'admin')]" 
    PIM         = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'viewPim')]"
    Leave       = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'leave')]"
    Time        = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'time')]"
    Recruitment = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'recruitment')]"
    my_info     = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'viewMyDetails')]"
    performance = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'performance')]"
    Dashboard   = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'dashboard')]"
    Directory   = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'direct')]"
    Maintenance = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'maintenance')]"  
    claim       = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'clai')]"
    Buzz        = "//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'buzz')]"