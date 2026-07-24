
from Actions.BaseActions import BaseActions
from Pages.ChangePasswordPage import ChangePasswordPage


class ChangePasswordActions(BaseActions):

    def __init__(self, driver, wait):

        super().__init__(driver, wait)

    def change_password(
            self,
            old_password,
            new_password,
            confirm_password):

        try:

            self.click(
                ChangePasswordPage.USER_MENU
            )

            self.click(
                ChangePasswordPage.CHANGE_PASSWORD
            )

            self.enter_text(
                ChangePasswordPage.OLD_PASSWORD,
                old_password
            )

            self.enter_text(
                ChangePasswordPage.NEW_PASSWORD,
                new_password
            )

            self.enter_text(
                ChangePasswordPage.CONFIRM_PASSWORD,
                confirm_password
            )

            self.click(
                ChangePasswordPage.SAVE_BUTTON
            )

            popup = self.wait_for_visibility(
                ChangePasswordPage.SUCCESS_POPUP
            )

            assert popup.is_displayed(), (
                "Password Change Failed"
            )

            self.logger.info(
                "Password Changed Successfully"
            )

            return popup.text

        except Exception as e:

            self.logger.error(
                "Password Change Failed"
            )

            self.save_screenshot(
                "change_password_failed"
            )

            self.logger.exception(e)

            raise

    def negative_change_password(
            self,
            old_password,
            new_password,
            confirm_password):

        try:

            self.click(
                ChangePasswordPage.USER_MENU
            )

            self.click(
                ChangePasswordPage.CHANGE_PASSWORD
            )

            if old_password:

                self.enter_text(
                    ChangePasswordPage.OLD_PASSWORD,
                    old_password
                )

            if new_password:

                self.enter_text(
                    ChangePasswordPage.NEW_PASSWORD,
                    new_password
                )

            if confirm_password:

                self.enter_text(
                    ChangePasswordPage.CONFIRM_PASSWORD,
                    confirm_password
                )

            self.click(
                ChangePasswordPage.SAVE_BUTTON
            )

        except Exception as e:

            self.logger.error(
                "Negative Change Password Failed"
            )

            self.save_screenshot(
                "negative_change_password_failed"
            )

            self.logger.exception(e)

            raise

    def get_required_message(self):

        try:

            return self.get_text(
                ChangePasswordPage.REQUIRED_MESSAGE
            )

        except Exception as e:

            self.logger.error(
                "Failed To Get Required Message"
            )

            self.save_screenshot(
                "required_message_failed"
            )

            self.logger.exception(e)

            raise

    def get_password_mismatch_message(self):

        try:

            return self.get_text(
                ChangePasswordPage.PASSWORD_NOT_MATCH
            )

        except Exception as e:

            self.logger.error(
                "Failed To Get Password Mismatch Message"
            )

            self.save_screenshot(
                "password_mismatch_failed"
            )

            self.logger.exception(e)

            raise

    def get_error_toast_message(self):

        try:

            popup = self.wait_for_visibility(
                ChangePasswordPage.ERROR_TOAST
            )

            return popup.text

        except Exception as e:

            self.logger.error(
                "Failed To Get Error Toast"
            )

            self.save_screenshot(
                "error_toast_failed"
            )

            self.logger.exception(e)

            raise

