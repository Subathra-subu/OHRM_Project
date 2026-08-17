from Actions.BaseActions import BaseActions
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from Utilities.ExcelUtils import get_data
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Pages.ClaimPage import ClaimPage
import os

class ClaimActions(BaseActions):
    
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    
        
    def login_entervacancy(self):
        try:
        
            LoginActions.login(self,get_config("username and password","username")
                               ,get_config("username and password","password"))
            
            self.js_click(ClaimPage.claim)
            
            self.logger.info("Claim link clikced")
            
            
    
        except Exception as e:

            self.logger.error("Login failed")
            
            self.logger.exception(e)
            
            raise
        
    def assign_claim(self):
        
        actions = ActionChains(self.driver)
        
        try:
            
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "..", "test_data", "vacancy_data.xlsx")

            employee_name = get_data(file_path,"AddVacancy")
            
            self.js_click(ClaimPage.assign_claim)
                    
            self.logger.info("Assign claim section clikced")
            
            self.enter_text(ClaimPage.employee_name,employee_name[0][1])
            self.wait_for_visibility(ClaimPage.employee_name_option)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            
            self.click(ClaimPage.event)
            self.wait_for_visibility(ClaimPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            
            self.click(ClaimPage.currency)
            self.wait_for_visibility(ClaimPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
            
            self.click(ClaimPage.create)   
            
            return self.is_displayed(ClaimPage.success_message)
            
        except Exception as e:

            self.logger.error("Assign claim failed")
            
            self.logger.exception(e)
            
            raise
        
    def submitClaim(self):

        try:
        
            actions = ActionChains(self.driver)

            self.js_click(ClaimPage.submitClaim)
            self.logger.info("Submit claim section clicked")

            self.js_click(ClaimPage.event)
            self.logger.info("Event dropdown clicked")

            self.wait_for_visibility(ClaimPage.eventOption)
            self.js_click(ClaimPage.eventOption)
            self.logger.info("Accommodation selected")

            self.js_click(ClaimPage.currency)
            self.logger.info("Currency dropdown clicked")

            self.wait_for_visibility(ClaimPage.list_box)
            actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

            self.js_click(ClaimPage.create)
            self.logger.info("Create button clicked")

            self.js_click(ClaimPage.submitButton)
            self.logger.info("Submit button clicked")

            return True

        except Exception as e:

            self.logger.error("Submit claim failed")
            self.logger.exception(e)

            raise