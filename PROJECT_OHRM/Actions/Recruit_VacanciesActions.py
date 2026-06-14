from Actions.BaseActions import BaseActions
from Pages.RecruitmentPage import Recruit_VacanciesPage
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Utilities.ExcelUtils import get_data
import time

class Recruit_VacanciesActions(BaseActions):
    
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    
        
    def login_entervacancy(self):
    
        try:
        
            LoginActions.login(self,get_config("username and password","username")
                               ,get_config("username and password","password"))
            
            self.js_click(Recruit_VacanciesPage.Recruitment)
            
            self.logger.info("Recruitment link clikced")
            
            self.js_click(Recruit_VacanciesPage.vacancies)
        
            self.logger.info("Vacancies section clikced")
    
        except Exception as e:

            self.logger.error("Add vacancy failed")
            
            self.logger.exception(e)
            
            raise
        
        
    def addVacancy(self):
        
        actions = ActionChains(self.driver)
        
        try:
            
            self.js_click(Recruit_VacanciesPage.add)
            self.logger.info("Add button clikced")
            
            vacancy_data = get_data("test_data/vacancy_data.xlsx","AddVacancy") 
            self.enter_text(Recruit_VacanciesPage.vacancy_name,vacancy_data[0][0])
            self.logger.info("Vacancy title entered")
            
            self.click(Recruit_VacanciesPage.job_title)
            
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            
            self.enter_text(Recruit_VacanciesPage.Hiring_Manager_input,vacancy_data[0][1])
            
            self.wait_for_visibility(Recruit_VacanciesPage.hiring_manager_option)

            self.click(Recruit_VacanciesPage.hiring_manager_option)
            
            self.js_click(Recruit_VacanciesPage.save)
            self.logger.info("Save button clicked")
            
            return self.is_displayed(Recruit_VacanciesPage.edit_message)
        
        except Exception as e:

            self.logger.error("Login failed")
            self.logger.exception(e)
            
            raise
        
    def addinvalidvacancy(self):
            
        actions = ActionChains(self.driver)
        
        try:
            
            self.js_click(Recruit_VacanciesPage.add)
            self.logger.info("Add button clikced")
            
            self.click(Recruit_VacanciesPage.save)
            self.logger.info("Save button clicked")
            
            return self.is_displayed(Recruit_VacanciesPage.required_messages)
        
        except Exception as e:

            self.logger.error("Invalid add_vacancy test failed")
            self.logger.exception(e)
            
            raise
    
    def addexistvacancy(self):
        
        actions = ActionChains(self.driver)
        
        try:
            
            self.js_click(Recruit_VacanciesPage.add)
            self.logger.info("Add button clikced")
            
            vacancy_data = get_data("test_data/vacancy_data.xlsx","AddVacancy")
            self.enter_text(Recruit_VacanciesPage.vacancy_name,vacancy_data[0][0])
            self.logger.info("Vacancy title entered")
            
            self.click(Recruit_VacanciesPage.job_title)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            self.logger.info("Job title selected")
            
            self.enter_text(Recruit_VacanciesPage.Hiring_Manager_input,vacancy_data[0][1])
            
            self.wait_for_visibility(Recruit_VacanciesPage.hiring_manager_option)

            self.click(Recruit_VacanciesPage.hiring_manager_option)
            
            self.click(Recruit_VacanciesPage.save)
            self.logger.info("Save button clicked")
            
            return self.is_displayed(Recruit_VacanciesPage.exist_message)
        
        except Exception as e:

            self.logger.error("Add exist vacancyname test failed")
            self.logger.exception(e)
            
            raise
    
    def searchVacancy(self):
        
        actions = ActionChains(self.driver)

        try:

            self.click(Recruit_VacanciesPage.job_title)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.click(Recruit_VacanciesPage.vacancy)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.click(Recruit_VacanciesPage.hiring_manager)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.click(Recruit_VacanciesPage.status)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.click(Recruit_VacanciesPage.search)

            self.wait_for_visibility(Recruit_VacanciesPage.records)

            return self.is_displayed(Recruit_VacanciesPage.records)

        except Exception as e:

            self.logger.error("Valid Search test failed")
            self.logger.exception(e)
            raise
        
    def searchVacancy_blank(self):
        
        actions = ActionChains(self.driver)

        try:
            
            self.click(Recruit_VacanciesPage.job_title)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.click(Recruit_VacanciesPage.vacancy)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.click(Recruit_VacanciesPage.hiring_manager)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.click(Recruit_VacanciesPage.status)
            self.wait_for_visibility(Recruit_VacanciesPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.click(Recruit_VacanciesPage.search)

            return self.is_displayed(Recruit_VacanciesPage.no_records)

        except Exception as e:

            self.logger.error("Valid Search test failed")
            self.logger.exception(e)
            raise
            
        