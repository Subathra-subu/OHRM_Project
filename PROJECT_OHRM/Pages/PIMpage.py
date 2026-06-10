from selenium import webdriver
from selenium.webdriver.common.by import By

class PIMpage:
     
     addemployee_btn  = "//div[@class='oxd-topbar-body']/descendant::a[2]"
     fname            = "//input[@name='firstName']"
     mname            = "//input[@name='middleName']"
     lname            = "//input[@name='lastName']"
     create_lgn_dts   = "//input[@type='checkbox']//following-sibling::span"
     username         = "(//div[contains(@class,'oxd-input-group')]//input[@autocomplete='off'])[1]"
     password         = "(//div[contains(@class,'oxd-input-group')]//input[@type='password'])[1]"
     confirm_password = "(//div[contains(@class,'oxd-input-group')]//input[@type='password'])[2]"
     save_btn         = "//div[@class='oxd-form-actions']/child::button[@type='submit']"