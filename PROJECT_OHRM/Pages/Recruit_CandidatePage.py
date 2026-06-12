from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class Recruit_CandidatePage(BasePage):
    
    job_title = (By.XPATH,"(//div[@class='oxd-select-text--after'])[1]/preceding-sibling::*")
    
    vacancy = (By.XPATH , "(//div[@class='oxd-select-text--after'])[2]/preceding-sibling::*")
    
    hiring_manager = (By.XPATH,"(//div[@class='oxd-select-text--after'])[3]/preceding-sibling::*") 
    
    status = (By.XPATH,"(//div[@class='oxd-select-text--after'])[4]/preceding-sibling::*") 
    
    candidate_name = (By.XPATH,"//div[@class='oxd-autocomplete-text-input--before']/following-sibling::input")
    
    keywords = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]") 
    
    from_date = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
    
    to_data = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]")
    
    mode = (By.XPATH,"(//div[@class='oxd-select-text--after'])[5]/child::*")
    
    search = (By.XPATH,"//button[@type='submit']")
    
    add = (By.XPATH,"//div[@class='orangehrm-header-container']/child::*")
    
     