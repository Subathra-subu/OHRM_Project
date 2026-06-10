from Actions.BaseActions import BaseActions
from Pages.DashboardPage import DashboardPage


class DashboardActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def verify_dashboard(self):

        try:

            actual_text = self.get_text(DashboardPage.DASHBOARD)

            assert actual_text == "Dashboard"

            self.logger.info("Dashboard Verification Passed")

        except AssertionError:

            self.logger.error(
                f"Dashboard Verification Failed : {actual_text}"
            )

            raise

        except Exception as e:

            self.logger.error("Dashboard Verification Failed")

            self.logger.exception(e)

            raise