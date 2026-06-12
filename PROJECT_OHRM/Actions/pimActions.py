from Actions.BaseActions import BaseActions
from Pages.PIMpage import PIMpage
from Pages.BasePage import BasePage
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
from selenium.webdriver.support import expected_conditions as EC
import time
class pimActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def add_employee(self, first_name, middle_name, last_name,
                     username, password, confirm_password):

        try:
            self.logger.info("PIM - Add Employee Started")
            LoginActions.login(self,get_config(
                "username and password",
                "username"
            )

            ,get_config(
                "username and password",
                "password"
            )
)
            self.js_click(BasePage.PIM)
            self.js_click(PIMpage.addemployee_btn)

            self.enter_text(PIMpage.fname, first_name)
            self.enter_text(PIMpage.mname, middle_name)
            self.enter_text(PIMpage.lname, last_name)

                

            self.js_click(PIMpage.create_lgn_dts)
            
            self.enter_text(PIMpage.username, username)
            self.enter_text(PIMpage.password, password)
            self.enter_text(PIMpage.confirm_password, confirm_password)
            self.click(PIMpage.save_btn)
            final_url = self.wait_for_url_contains("/viewPersonalDetails")
            
            self.logger.info("PIM - Add Employee Completed")
            return final_url
            
      

        except Exception as e:

            self.logger.error("PIM - Add Employee Failed")
            self.logger.exception(e)
            raise
    def search_employee_pim(self, first_name, middle_name, last_name, username, password, confirm_password):
        try:
            self.logger.info("PIM - Creating employee before searching")
            LoginActions.login(self, get_config("username and password", "username"),
                                    get_config("username and password", "password"))
           
            self.js_click(BasePage.PIM)

            self.logger.info("PIM - Searching for the created employee")
            self.click(PIMpage.emp_list)
            
            self.enter_text(PIMpage.employee_nmae, first_name)
            self.click(PIMpage.search_emp)
            
            self.logger.info("Waiting dynamically for data tables to resolve...")
            
            self.wait.until(EC.presence_of_element_located(PIMpage.user_area))
            
            target_element = self.wait.until(EC.visibility_of_element_located(PIMpage.user_area))
            
            self.scroll_into_view(PIMpage.user_area)
            
            self.wait.until(EC.element_to_be_clickable(target_element))
            self.js_click(PIMpage.user_area)
            
            self.logger.info("Successfully targeted user area element.")
            
            final_url = self.wait_for_url_contains("/viewPersonalDetails")
            self.logger.info("PIM - search Employee Completed")

            return final_url
         
            
        except Exception as e:
            self.logger.error("PIM - Search Employee Failed due to target row load mismatch")
            self.logger.exception(e)
            raise