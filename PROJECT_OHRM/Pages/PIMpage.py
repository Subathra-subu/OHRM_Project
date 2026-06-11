from selenium import webdriver
from selenium.webdriver.common.by import By

class PIMpage:
     
     addemployee_btn  = (By.XPATH, "//div[@class='oxd-topbar-body']/descendant::a[2]")
     fname            = (By.XPATH, "//input[@name='firstName']")
     mname            = (By.XPATH, "//input[@name='middleName']")
     lname            = (By.XPATH, "//input[@name='lastName']")
     create_lgn_dts   = (By.XPATH, "//input[@type='checkbox']//following-sibling::span")
     username         = (By.XPATH, "(//div[contains(@class,'oxd-input-group')]//input[@autocomplete='off'])[1]")
     password         = (By.XPATH, "(//div[contains(@class,'oxd-input-group')]//input[@type='password'])[1]")
     confirm_password = (By.XPATH, "(//div[contains(@class,'oxd-input-group')]//input[@type='password'])[2]")
     save_btn         = (By.XPATH, "//div[@class='oxd-form-actions']/child::button[@type='submit']")