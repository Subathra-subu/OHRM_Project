from selenium.webdriver.common.keys import Keys

from Pages.PerformanceTrackersPage import PerformanceTrackersPage
from Pages.BasePage import BasePage
from Actions.BaseActions import BaseActions


class PerformanceTrackersActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def _open_tracker_page(self):

        self.click(
            BasePage.performance
        )

        self.click(
            PerformanceTrackersPage.configure
        )

        self.click(
            PerformanceTrackersPage.track_select
        )

    def press_down_and_enter(self, count):

        active_element = self.driver.switch_to.active_element

        for _ in range(count):
            active_element.send_keys(
                Keys.ARROW_DOWN
            )

        active_element.send_keys(
            Keys.ENTER
        )

    def add_tracker(
        self,
        tracker,
        employee,
        reviewer
    ):

        self._open_tracker_page()

        self.click(
            PerformanceTrackersPage.add_btn
        )

        self.enter_text(
            PerformanceTrackersPage.tracker_name,
            tracker
        )

        self.enter_text(
            PerformanceTrackersPage.employee_name,
            employee
        )

        self.press_down_and_enter(1)

        self.enter_text(
            PerformanceTrackersPage.reviewer_name,
            reviewer
        )

        self.press_down_and_enter(1)

        self.click(
            PerformanceTrackersPage.save_btn
        )

        

    def invalid_add_tracker(
        self,
        employee,
        reviewer
    ):

        self._open_tracker_page()

        self.click(
            PerformanceTrackersPage.add_btn
        )

        self.enter_text(
            PerformanceTrackersPage.employee_name,
            employee
        )

        self.press_down_and_enter(1)

        self.enter_text(
            PerformanceTrackersPage.reviewer_name,
            reviewer
        )

        self.press_down_and_enter(1)

        self.click(
            PerformanceTrackersPage.save_btn
        )

        return self.get_text(
            PerformanceTrackersPage.tracker_required
        )

    def search_tracker(
        self,
        employee
    ):

        self._open_tracker_page()

        self.enter_text(
            PerformanceTrackersPage.search_employee,
            employee
        )

        self.press_down_and_enter(1)

        self.js_click(
            PerformanceTrackersPage.search_btn
        )

        return self.get_text(
            PerformanceTrackersPage.search_result
        )

    def invalid_search_tracker(
        self,
        employee
    ):

        self._open_tracker_page()

        self.enter_text(
            PerformanceTrackersPage.search_employee,
            employee
        )

        self.js_click(
            PerformanceTrackersPage.search_btn
        )

        return self.get_text(
            PerformanceTrackersPage.no_record
        )

    def delete_tracker(
        self,
        tracker
    ):

        self._open_tracker_page()

        self.click(
            PerformanceTrackersPage.tracker_checkbox(
                tracker
            )
        )

        self.click(
            PerformanceTrackersPage.delete_btn
        )

        self.click(
            PerformanceTrackersPage.delete_confirm_btn
        )

        return self.get_text(
            PerformanceTrackersPage.delete_success_msg
        )