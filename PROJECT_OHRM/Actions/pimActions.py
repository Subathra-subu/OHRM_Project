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

    def add_employee_pim(self, first_name, middle_name, last_name,
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
            self.logger.info("Waiting for OrangeHRM backend form-loader overlay to clear...")
            self.wait_for_invisibility(PIMpage.form_loader)
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

    def missing_field_validation(self, text_value, missing_field_type):
        try:
            self.logger.info(f"PIM - Add Employee Missing {missing_field_type} validation check started")
            LoginActions.login(self, get_config("username and password", "username"),
                                    get_config("username and password", "password"))
            
            self.js_click(BasePage.PIM)
            self.js_click(PIMpage.addemployee_btn)

            if missing_field_type == "last_name":
                self.enter_text(PIMpage.fname, text_value)   
                self.wait_for_invisibility(PIMpage.form_loader)
                self.click(PIMpage.save_btn)
                err = self.get_text(PIMpage.lname_err_msg)
            else:
                self.enter_text(PIMpage.lname, text_value)   
                self.wait_for_invisibility(PIMpage.form_loader)
                self.click(PIMpage.save_btn)
                err = self.get_text(PIMpage.lname_err_msg)
                
            self.logger.info(f"Successfully received field validation required error message for {missing_field_type}")
            return err
        except Exception as e:
            self.logger.error(f"PIM - Validation capture failed for {missing_field_type}")
            self.logger.exception(e)
            raise