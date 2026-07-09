import random
import string

from selenium.webdriver.common.keys import Keys

from Actions.BaseActions import BaseActions
from Pages.BasePage import BasePage
from Pages.TimePage import TimePage


class TimeActions(BaseActions):

    def __init__(self, driver, wait):

        super().__init__(driver, wait)

    def add_customer(
            self,
            customer_name,
            description):

        try:

            self.click(
                BasePage.Time
            )

            self.click(
                TimePage.PROJECT_INFO
            )

            self.click(
                TimePage.CUSTOMER
            )

            self.click(
                TimePage.ADD_BTN
            )

            self.enter_text(
                TimePage.CUSTOMER_NAME,
                customer_name
            )

            self.enter_text(
                TimePage.DESCRIPTION,
                description
            )

            self.click(
                TimePage.SAVE_BTN
            )

            popup = self.wait_for_visibility(
                TimePage.popup_message
            )

            assert popup.is_displayed(), (
                "Customer Creation Failed"
            )

            self.logger.info(
                f"Customer Created Successfully : {customer_name}"
            )

            return customer_name

        except Exception as e:

            self.logger.error(
                "Customer Creation Failed"
            )

            self.save_screenshot(
                "add_customer_failed"
            )

            self.logger.exception(e)

            raise

    def add_existing_customer(
            self,
            customer_name):

        try:

            self.click(
                BasePage.Time
            )

            self.click(
                TimePage.PROJECT_INFO
            )

            self.click(
                TimePage.CUSTOMER
            )

            self.click(
                TimePage.ADD_BTN
            )

            self.enter_text(
                TimePage.CUSTOMER_NAME,
                customer_name
            )

            self.click(
                TimePage.DESCRIPTION
            )

            error = self.wait_for_visibility(
                TimePage.ALREADY_EXISTS_MESSAGE
            )

            assert error.is_displayed(), (
                "Duplicate customer validation message not displayed"
            )

            self.logger.info(
                error.text
            )

            return error.text

        except Exception as e:

            self.logger.error(
                "Duplicate Customer Validation Failed"
            )

            self.save_screenshot(
                "duplicate_customer_failed"
            )

            self.logger.exception(e)

            raise

    def verify_attendance_records(
            self,
            date):

        try:

            self.click(
                BasePage.Time
            )

            self.click(
                TimePage.ATTENDANCE
            )

            self.click(
                TimePage.MY_RECORDS
            )

            date_box = self.wait_for_visibility(
                TimePage.DATE
            )

            date_box.click()

            date_box.send_keys(
                Keys.CONTROL,
                "a"
            )

            date_box.send_keys(
                Keys.DELETE
            )

            date_box.send_keys(
                date
            )

            self.click(
                TimePage.VIEW_BUTTON
            )

            self.scroll_to_element(
                TimePage.RECORDS_FOUND
            )

            records = self.get_text(
                TimePage.RECORDS_FOUND
            )

            assert "Records Found" in records, (
                f"Expected Records Found but got {records}"
            )

            self.logger.info(
                f"Attendance Records Verified : {records}"
            )

            return records

        except Exception as e:

            self.logger.error(
                "Attendance Record Validation Failed"
            )

            self.save_screenshot(
                "attendance_records_failed"
            )

            self.logger.exception(e)

            raise