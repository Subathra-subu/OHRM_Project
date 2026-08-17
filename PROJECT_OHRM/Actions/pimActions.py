from Actions.BaseActions import BaseActions
from Pages.PIMpage import PIMpage
from Pages.BasePage import BasePage
from Actions.LoginActions import LoginActions
from Utilities.ReadConfig import get_config

class pimActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def add_employee_pim(self, first_name, middle_name, last_name,
                         username, password, confirm_password):

        try:
            self.logger.info("PIM - Add Employee Started")

            LoginActions.login(
                self,
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            self.clickstale(BasePage.PIM)
            self.clickstale(PIMpage.addemployee_btn)

            self.enter_text(PIMpage.fname, first_name)
            self.enter_text(PIMpage.mname, middle_name)
            self.enter_text(PIMpage.lname, last_name)

            self.clickstale(PIMpage.create_lgn_dts)

            self.enter_text(PIMpage.username, username)
            self.enter_text(PIMpage.password, password)
            self.enter_text(PIMpage.confirm_password, confirm_password)

            self.clickstale(PIMpage.save_btn)

            self.wait_for_invisibility(PIMpage.form_loader)

            final_url = self.wait_for_url_contains("/viewPersonalDetails")

            self.logger.info("PIM - Add Employee Completed")

            return final_url

        except Exception as e:
            self.logger.error("PIM - Add Employee Failed")
            self.logger.exception(e)
            raise

    def search_employee_pim(self, first_name, middle_name, last_name,
                            username, password, confirm_password):

        try:
            self.logger.info("PIM - Search Employee Started")

            LoginActions.login(
                self,
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            self.clickstale(BasePage.PIM)

            self.clickstale(PIMpage.emp_list)

            self.enter_text(PIMpage.employee_nmae, first_name)

            self.clickstale(PIMpage.search_emp)

            self.wait_for_invisibility(PIMpage.form_loader)

            self.wait_for_visibility(PIMpage.user_area)

            self.scroll_into_view(PIMpage.user_area)

            self.clickstale(PIMpage.user_area)

            self.logger.info("Successfully opened employee details")

            final_url = self.wait_for_url_contains("/viewPersonalDetails")

            self.logger.info("PIM - Search Employee Completed")

            return final_url

        except Exception as e:
            self.logger.error("PIM - Search Employee Failed")
            self.logger.exception(e)
            raise

    def missing_field_validation(self, text_value, missing_field_type):

        try:
            self.logger.info(f"PIM - Missing {missing_field_type} Validation Started")

            LoginActions.login(
                self,
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            self.clickstale(BasePage.PIM)
            self.clickstale(PIMpage.addemployee_btn)

            if missing_field_type == "last_name":
                self.enter_text(PIMpage.fname, text_value)
            else:
                self.enter_text(PIMpage.lname, text_value)

            self.wait_for_invisibility(PIMpage.form_loader)
            self.clickstale(PIMpage.save_btn)

            err = self.get_text(PIMpage.lname_err_msg)

            self.logger.info(f"Validation message captured: {err}")

            return err

        except Exception as e:
            self.logger.error(f"PIM - Validation Failed for {missing_field_type}")
            self.logger.exception(e)
            raise

    def add_new_dropdown_custom_field(self, field_name):

        try:
            self.logger.info("PIM - Add Custom Field Started")

            LoginActions.login(
                self,
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            self.clickstale(BasePage.PIM)

            self.clickstale(PIMpage.configuration)

            self.clickstale(PIMpage.custom_fields)

            self.clickstale(PIMpage.add_custom_field)

            self.enter_text(PIMpage.field_name_input, field_name)

            self.clickstale(PIMpage.screen_dropdown_trigger)
            self.wait_for_visibility(PIMpage.dropdown_options_list)
            self.clickstale(PIMpage.first_dropdown_option)
            self.wait_for_invisibility(PIMpage.dropdown_options_list)

            self.clickstale(PIMpage.type_dropdown_trigger)
            self.wait_for_visibility(PIMpage.dropdown_options_list)
            self.clickstale(PIMpage.first_dropdown_option)
            self.wait_for_invisibility(PIMpage.dropdown_options_list)

            self.clickstale(PIMpage.custom_field_save_btn)

            self.wait_for_invisibility(PIMpage.form_loader)

            current_url = self.driver.current_url

            self.logger.info(f"Custom Field Added Successfully: {current_url}")

            return current_url

        except Exception as e:
            self.logger.error("PIM - Add Custom Field Failed")
            self.logger.exception(e)
            raise

    def delete_first_custom_field_flow(self):

        try:
            self.logger.info("PIM - Delete Custom Field Started")

            LoginActions.login(
                self,
                get_config("username and password", "username"),
                get_config("username and password", "password")
            )

            self.clickstale(BasePage.PIM)

            self.clickstale(PIMpage.configuration)

            self.clickstale(PIMpage.custom_fields)

            self.clickstale(PIMpage.first_delete_btn)

            self.clickstale(PIMpage.confirm_delete_btn)

            self.wait_for_visibility(PIMpage.success_toast_msg)

            is_displayed = self.is_displayed(PIMpage.success_toast_msg)

            self.logger.info(f"Delete Successful: {is_displayed}")

            return is_displayed

        except Exception as e:
            self.logger.error("PIM - Delete Custom Field Failed")
            self.logger.exception(e)
            raise