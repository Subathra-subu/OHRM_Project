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

        self.click(ChangePasswordPage.USER_MENU)

        self.click(ChangePasswordPage.CHANGE_PASSWORD)

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

        self.click(ChangePasswordPage.SAVE_BUTTON)

        popup = self.wait_for_visibility(
            ChangePasswordPage.SUCCESS_POPUP
        )

        assert popup.is_displayed(), "Password Change Failed"

        self.logger.info("Password Changed Successfully")

        return popup.text