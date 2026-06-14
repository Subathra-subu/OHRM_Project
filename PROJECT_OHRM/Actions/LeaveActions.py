from Actions.BaseActions import BaseActions
from Pages.LeavePage import LeavePage as lp
from Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys

class LeaveActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def assign_leave(self,employee,leave_type,from_date,to_date,comments):

        self.logger.info("Assign Leave Started")
        self.wait_for_visibility(BasePage.Leave)
        self.js_click(BasePage.Leave)
        self.wait.until(lambda driver:"leave" in driver.current_url.lower())
        self.wait_for_visibility(lp.assign_leave_menu)
        self.click(lp.assign_leave_menu)
        self.wait_for_visibility(lp.employee_name)
        self.enter_text(lp.employee_name, employee)
        self.select_first_dropdown_option_via_js(lp.auto_dropdown)
        self.click(lp.leave_type_dropdown)
        options = self.driver.find_elements(*lp.leave_type_options)

        for option in options:
            if leave_type.lower() in option.text.lower():
                option.click()
                break

        from_date_ele = self.driver.find_element(*lp.from_date)
        from_date_ele.send_keys(Keys.CONTROL + "a")
        from_date_ele.send_keys(Keys.DELETE)
        from_date_ele.send_keys(from_date)
        to_date_ele = self.driver.find_element(*lp.to_date)
        to_date_ele.send_keys(Keys.CONTROL + "a")
        to_date_ele.send_keys(Keys.DELETE)
        to_date_ele.send_keys(to_date)
        self.enter_text(lp.comments,comments)
        self.click(lp.assign_btn)
        self.wait_for_visibility(lp.confirm_ok_button)
        self.click(lp.confirm_ok_button)

        try:
            self.wait_for_visibility(lp.success_message)
            return self.get_text(lp.success_message)

        except Exception:
            return self.get_text(lp.error_message)
        
    def assign_leave_employee_required(self,leave_type,from_date,to_date,comments):

        self.logger.info("Assign Leave Employee Required Validation Started")
        self.wait_for_visibility(BasePage.Leave)
        self.js_click(BasePage.Leave)
        self.wait.until(lambda driver:"leave" in driver.current_url.lower())
        self.wait_for_visibility(lp.assign_leave_menu)
        self.click(lp.assign_leave_menu)
        self.click(lp.leave_type_dropdown)
        options = self.driver.find_elements(*lp.leave_type_options)

        for option in options:
            if leave_type.lower() in option.text.lower():
                option.click()
                break

        from_date_ele = self.driver.find_element(*lp.from_date)
        from_date_ele.send_keys(Keys.CONTROL + "a")
        from_date_ele.send_keys(Keys.DELETE)
        from_date_ele.send_keys(from_date)

        to_date_ele = self.driver.find_element(*lp.to_date)
        to_date_ele.send_keys(Keys.CONTROL + "a")
        to_date_ele.send_keys(Keys.DELETE)
        to_date_ele.send_keys(to_date)
        self.enter_text(lp.comments,comments)
        self.click(lp.assign_btn)
        self.wait_for_visibility(lp.employee_required_msg)
        return self.get_text(lp.employee_required_msg)

    def assign_leave_all_fields_required(self):

        self.logger.info("Assign Leave All Fields Required Validation Started") 
        self.wait_for_visibility(BasePage.Leave)
        self.js_click(BasePage.Leave)
        self.wait_for_visibility(lp.assign_leave_menu)
        self.click(lp.assign_leave_menu)
        self.click(lp.assign_btn)
        return len(lp.messages)
