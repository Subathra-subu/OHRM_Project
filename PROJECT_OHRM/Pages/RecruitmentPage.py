from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class Recruit_VacanciesPage(BasePage):
    
    job_title = (By.XPATH,"//label[contains(text(),'Job Title')]/following::div[contains(@class,'oxd-select-text')][1]")
    
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
    
    vacancies = (By.XPATH,"//li[@class='oxd-topbar-body-nav-tab']")
    
    email = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    
    Hiring_Manager_input = (By.XPATH,"//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']//child::input")
    
    save = (By.XPATH,"//button[@type='submit']")
    
    success_message = (By.XPATH,"//p[text()='Successfully Saved']")
    
    required_messages = (By.XPATH,"//span[text()='Required']")
    
    exist_message = (By.XPATH,"//div[@class='orangehrm-background-container']/descendant::span[text()='Already exists']")
    
    searching = (By.XPATH,"//div[text()='Searching....']")
    
    records = (By.XPATH,"//div[@class='oxd-table orangehrm-vacancy-list']/child::div[@class='oxd-table-body']/descendant::div[@class='oxd-table-row oxd-table-row--with-border']/child::*")
    
    list_box = (By.CSS_SELECTOR, "div[role='listbox']")
    
    edit_message = (By.XPATH,"//h6[text()='Edit Vacancy']")
    
    hiring_manager_option = (By.XPATH,"//div[contains(@class,'oxd-autocomplete-option') and not(contains(.,'Searching'))]")
    
    no_records = (By.XPATH,"//span[text()='No Records Found']")
    
    first_name = (By.NAME, "firstName")
    
    middle_name = (By.XPATH, "//input[@name='middleName']")
    
    last_name = (By.XPATH, "//input[@name='lastName']")
    
    vacancy_dropdown = (By.XPATH,"//label[text()='Vacancy']/following::div[contains(@class,'oxd-select-text')][1]")
    
    contact_number = (By.XPATH, "//label[text()='Contact Number']/following::input[1]")
    
    keywords = (By.XPATH, "//label[text()='Keywords']/following::input[1]")
    
    candidate_profile_message = (By.XPATH,"//h6[text()='Candidate Profile']")
    
    vacancy_name=(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
