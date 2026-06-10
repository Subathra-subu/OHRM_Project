from selenium import webdriver
from selenium.webdriver.common.by import By

class AddEmployeepage:
     
     addemployee_btn = (By.XPATH,"//div[@class='oxd-topbar-body']/descendant::a[2]")
     create_lgn_dts = (By.XPATH,"//input[@type='checkbox']//following-sibling::span")
     