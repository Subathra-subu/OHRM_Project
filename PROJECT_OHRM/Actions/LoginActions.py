from Actions.BaseActions import BaseActions
from Pages.LoginPage import LoginPage


class LoginActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def login(self, username, password):

        try:

            self.logger.info("Login Started")

            self.enter_text(LoginPage.USERNAME, username)

            self.enter_text(LoginPage.PASSWORD, password)

            self.click(LoginPage.LOGIN_BUTTON)

            self.logger.info("Login Completed")

        except Exception as e:

            self.logger.error("Login Failed")
            self.logger.exception(e)
            raise