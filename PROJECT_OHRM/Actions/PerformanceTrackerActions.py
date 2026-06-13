from Pages.PerformanceTrackersPage import PerformanceTrackersPage
from Pages.BasePage import BasePage
from Actions.BaseActions import BaseActions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class PerformanceTrackersActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def add_tracker(self, tracker, employee, reviewer):

        self.click(BasePage.performance)
        self.js_click(PerformanceTrackersPage.configure)
        self.click(PerformanceTrackersPage.track_select)
        self.js_click(PerformanceTrackersPage.add_btn)
        self.enter_text(PerformanceTrackersPage.tracker_name, tracker)
        self.enter_text(PerformanceTrackersPage.employee_name, employee)
        self.click(PerformanceTrackersPage.employee_suggestion)
        self.enter_text(PerformanceTrackersPage.reviewer_name, reviewer)
        self.click(PerformanceTrackersPage.reviewer_suggestion)
        self.js_click(PerformanceTrackersPage.save_btn)

        return self.get_text(PerformanceTrackersPage.success_msg)

    def invalid_add_tracker(self, employee, reviewer):

        actions = ActionChains(self.driver)

        self.click(BasePage.performance)
        self.js_click(PerformanceTrackersPage.configure)
        self.click(PerformanceTrackersPage.track_select)
        self.js_click(PerformanceTrackersPage.add_btn)
        self.enter_text(PerformanceTrackersPage.employee_name, employee)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.enter_text(PerformanceTrackersPage.reviewer_name, reviewer)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.js_click(PerformanceTrackersPage.save_btn)

        return self.get_text(PerformanceTrackersPage.tracker_required)

    def search_tracker(self, employee):

        actions = ActionChains(self.driver)

        self.click(BasePage.performance)
        self.js_click(PerformanceTrackersPage.configure)
        self.click(PerformanceTrackersPage.track_select)
        self.enter_text(PerformanceTrackersPage.search_employee, employee)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.click(PerformanceTrackersPage.search_btn)

        return self.get_text(PerformanceTrackersPage.search_result)