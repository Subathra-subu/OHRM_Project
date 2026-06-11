from Actions.BaseActions import BaseActions
from Pages.PIMpage import PIMpage
from Pages.BasePage import BasePage
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config
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

            self.js_click(PIMpage.save_btn)
            
            exp=self.get_attribute(PIMpage.fullname,"value")
            
            self.logger.info("PIM - Add Employee Completed")
            return exp
      

        except Exception as e:

            self.logger.error("PIM - Add Employee Failed")
            self.logger.exception(e)
            raise
    def search_employee(self, first_name, middle_name, last_name, username, password, confirm_password):
        try:
            
            self.logger.info("PIM - Creating employee before searching")
            
            
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

            self.logger.info("PIM - Searching for the created employee")
            self.click(PIMpage.emp_list)
            self.enter_text(PIMpage.employee_nmae,first_name )
            
            self.click(PIMpage.search_emp)
            self.click( PIMpage.user_area)
            exp=self.get_attribute_lambda(PIMpage.fullname,"value")
            print(exp)
            return exp
        except Exception as e:
            self.logger.error("PIM - Search Employee Failed")
            self.logger.exception(e)
            raise