import random
import string

from Actions.BaseActions import BaseActions
from Pages.BasePage import BasePage
from Pages.TimePage import TimePage


class TimeActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def add_customer(self, customer_name, description):

        self.click(BasePage.Time)

        self.click(TimePage.PROJECT_INFO)

        self.click(TimePage.CUSTOMER)

        self.click(TimePage.ADD_BTN)

        self.enter_text(TimePage.CUSTOMER_NAME, customer_name)

        self.enter_text(TimePage.DESCRIPTION, description)

        self.click(TimePage.SAVE_BTN)

        popup = self.wait_for_visibility(TimePage.popup_message)

        assert popup.is_displayed(), "Customer Creation Failed"

        self.logger.info(f"Customer Created Successfully : {customer_name}")

        return customer_name