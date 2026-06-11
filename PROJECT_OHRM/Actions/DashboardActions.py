from Actions.BaseActions import BaseActions
from Pages.DashboardPage import DashboardPage


class DashboardActions(BaseActions):

    def __init__(self, driver, wait):

        super().__init__(driver, wait)

    def verify_dashboard(self):

        print(DashboardPage.DASHBOARD)
        print(type(DashboardPage.DASHBOARD))

        actual_text = self.get_text(
        DashboardPage.DASHBOARD
        )

        print(actual_text)