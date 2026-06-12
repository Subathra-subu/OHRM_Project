from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.Recruit_CandidatePage import Recruit_CandidatePage

class Recruit_VacanciesPage(Recruit_CandidatePage):
    
    vacancies = (By.XPATH,"//li[@class='oxd-topbar-body-nav-tab']")
    
    vacancy_name = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    
    Hiring_Manager_input = (By.XPATH,"//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']//child::input")
    
    save = (By.XPATH,"//button[@type='submit']")
    
    edit_vacancy = (By.XPATH,"//h6[text()='Edit Vacancy']")