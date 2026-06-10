from Actions.BaseActions import BaseActions
from Pages.PIMpage import PIMpage
from Pages.BasePage import BasePage

class pimActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def add_employee(self, first_name, middle_name, last_name,
                     username, password, confirm_password):

        try:
            self.logger.info("PIM - Add Employee Started")

            # 👉 Click Add Employee
            self.click(BasePage.PIM)
            self.click(PIMpage.addemployee_btn)

            # 👉 Personal Details
            self.enter_text(PIMpage.fname, first_name)
            self.enter_text(PIMpage.mname, middle_name)
            self.enter_text(PIMpage.lname, last_name)

            # 👉 Login Details (conditional)
            

            self.click(PIMpage.create_lgn_dts)

            self.enter_text(PIMpage.username, username)
            self.enter_text(PIMpage.password, password)
            self.enter_text(PIMpage.confirm_password, confirm_password)

            # 👉 Save employee
            self.click(PIMpage.save_btn)

            self.logger.info("PIM - Add Employee Completed")

        except Exception as e:

            self.logger.error("PIM - Add Employee Failed")
            self.logger.exception(e)
            raise