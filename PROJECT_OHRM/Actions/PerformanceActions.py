from Pages.PerformancePage import PerformancePage
from Pages.BasePage import BasePage
from Actions.BaseActions import BaseActions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class PerformanceActions(BaseActions):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
    def add_kpi (self,kip):
        actions = ActionChains(self.driver)
        self.click(BasePage.performance)
        self.js_click(PerformancePage.configure)
        self.click(PerformancePage.kip_select)
        self.js_click(PerformancePage.add)
        self.enter_text(PerformancePage.kip,kip)
        self.click(PerformancePage.job_title)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.js_click(PerformancePage.click_title)
        self.js_click(PerformancePage.submit)
        

