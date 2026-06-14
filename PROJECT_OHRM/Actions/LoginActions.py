
from Actions.BaseActions import BaseActions
from Pages.LoginPage import LoginPage


class LoginActions(BaseActions):

    def __init__(self, driver, wait):

        super().__init__(driver, wait)

    def login(self, username, password):

        try:

            self.logger.info("Login Started")

            self.enter_text(
                LoginPage.USERNAME,
                username
            )

            self.enter_text(
                LoginPage.PASSWORD,
                password
            )

            self.click(
                LoginPage.LOGIN_BUTTON
            )

            self.logger.info(
                "Login Successful"
            )

        except Exception as e:

            self.logger.error(
                "Login Failed"
            )

            self.save_screenshot(
                "login_failed"
            )

            self.logger.exception(e)

            raise

    def invalid_login(
            self,
            username,
            password):

        try:

            self.logger.info(
                "Invalid Login Started"
            )

            self.enter_text(
                LoginPage.USERNAME,
                username
            )

            self.enter_text(
                LoginPage.PASSWORD,
                password
            )

            self.click(
                LoginPage.LOGIN_BUTTON
            )

            message = self.get_text(
                LoginPage.INVALID_CREDENTIALS_MESSAGE
            )

            assert "Invalid" in message

            self.logger.info(
                "Invalid Login Validation Displayed"
            )

            return message

        except Exception as e:

            self.logger.error(
                "Invalid Login Failed"
            )

            self.save_screenshot(
                "invalid_login_failed"
            )

            self.logger.exception(e)

            raise

    def without_credential(
            self,
            username,
            password):

        try:

            self.logger.info(
                "Without Credential Login Started"
            )

            self.enter_text(
                LoginPage.USERNAME,
                username
            )

            self.enter_text(
                LoginPage.PASSWORD,
                password
            )

            self.click(
                LoginPage.LOGIN_BUTTON
            )

            messages = self.driver.find_elements(
                *LoginPage.REQUIRED_MESSAGE
            )

            for message in messages:

                assert (
                    "Required"
                    in message.text
                )

            self.logger.info(
                "Required Validation Displayed"
            )

        except Exception as e:

            self.logger.error(
                "Without Credential Login Failed"
            )

            self.save_screenshot(
                "without_credential_login_failed"
            )

            self.logger.exception(e)

            raise

