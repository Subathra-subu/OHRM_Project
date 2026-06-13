from Actions.BaseActions import BaseActions
from Pages.MaintenancePage import MaintenancePage as mp
from Pages.BasePage import BasePage
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config

class MaintenanceActions(BaseActions):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    
    def valid_access_records(self, name):
        try:
            self.logger.info("Maintenance - Access Records Verification Started")
            
            LoginActions.login(
                self, 
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )
            
            self.wait_for_visibility(BasePage.Maintenance)
            self.js_click(BasePage.Maintenance)
            
            self.wait_for_visibility(mp.password)
            self.enter_text(mp.password, get_config("username and password", "password"))
            self.click(mp.confirm)
            
            self.wait_for_visibility(mp.Access_rec)
            self.click(mp.Access_rec)
            
            self.wait_for_visibility(mp.emp_name)
            input_element = self.driver.find_element(*mp.emp_name)
            
            input_element.click()
            self.enter_text(mp.emp_name, name)
            
            self.select_first_dropdown_option_via_js(mp.auto_drop)
            
            self.wait_for_element_value_attribute(mp.emp_name)
            
            self.click(mp.search)
            self.wait_for_invisibility(mp.form_loader)
            
            self.logger.info("Maintenance - Access Records Verification Completed")
            return self.is_visible(mp.first_name)
            
        except Exception as e:
            self.logger.error("Maintenance - Access Records Execution Failed")
            self.logger.exception(e)
            raise

    def verify_blank_search_error_state(self):
        try:
            self.logger.info("Maintenance - Checking Blank Search Validation UI State")
            
            LoginActions.login(
                self, 
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )
            
            self.wait_for_visibility(BasePage.Maintenance)
            self.js_click(BasePage.Maintenance)
            
            self.wait_for_visibility(mp.password)
            self.enter_text(mp.password, get_config("username and password", "password"))
            self.click(mp.confirm)
            
            self.wait_for_visibility(mp.Access_rec)
            self.click(mp.Access_rec)
            
            self.wait_for_visibility(mp.emp_name) 
            self.click(mp.search)
            
            return self.is_visible(mp.err_msg)
            
        except Exception as e:
            self.logger.error("Maintenance - Validation UI State check failed")
            self.logger.exception(e)
            raise