from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Recruit_CandidatePage import Recruit_CandidatePage

class Recruit_VacanciesPage(Recruit_CandidatePage):
    
    vacancies = (By.XPATH,"//li[@class='oxd-topbar-body-nav-tab']")
    
    vacancy_name = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    
    Hiring_Manager_input = (By.XPATH,"//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']//child::input")
    
    save = (By.XPATH,"//button[@type='submit']")
    
    success_message = (By.XPATH,"//p[text()='Successfully Saved']")
    
    required_messages = (By.XPATH,"//div[@class='orangehrm-background-container']/descendant::span[text()='Required']")
    
    exist_message = (By.XPATH,"//div[@class='orangehrm-background-container']/descendant::span[text()='Already exists']")
    
    searching = (By.XPATH,"//div[text()='Searching....']")
    
    records = (By.XPATH,"//div[@class='oxd-table orangehrm-vacancy-list']/child::div[@class='oxd-table-body']/descendant::div[@class='oxd-table-row oxd-table-row--with-border']/child::*")
    
    list_box = (By.CSS_SELECTOR, "div[role='listbox']")
    
    edit_message = (By.XPATH,"//h6[text()='Edit Vacancy']")
    
    hiring_manager_option = (By.XPATH,"//div[contains(@class,'oxd-autocomplete-option') and not(contains(.,'Searching'))]")
    
    no_records = (By.XPATH,"//span[text()='No Records Found']")