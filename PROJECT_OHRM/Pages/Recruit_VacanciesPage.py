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
    
    list_box = (By.XPATH,"//div[@role='listbox']")
    
    searching = (By.XPATH,"//div[text()='Searching....']")
    
    records = (By.XPATH,"//div[@class='oxd-table orangehrm-vacancy-list']/child::div[@class='oxd-table-body']/descendant::div[@class='oxd-table-row oxd-table-row--with-border']/child::*")