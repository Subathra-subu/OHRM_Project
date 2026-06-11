from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:

    search = (By.XPATH,"//input[@class='oxd-input oxd-input--active']")
    Admin = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'admin')]") 
    PIM = (By.CSS_SELECTOR,"a[href*='viewPim']")
    Leave = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'leave')]")
    Time = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'time')]")
    Recruitment = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'recruitment')]")
    my_info = (By.CSS_SELECTOR,"a[href*='viewMyDe']")
    performance = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'performance')]")
    Dashboard = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'dashboard')]")
    Directory = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'direct')]")
    Maintenance = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'maintenance')]")  
    claim = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'clai')]")
    Buzz = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']/child::a[contains(@href,'buzz')]")