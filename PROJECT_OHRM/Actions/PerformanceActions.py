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
        return self.get_text(PerformancePage.success_msg)
    
    def invalid_add(self,kipinvalid):
        actions = ActionChains(self.driver)
        self.click(BasePage.performance)
        self.js_click(PerformancePage.configure)
        self.click(PerformancePage.kip_select)
        self.js_click(PerformancePage.add)
        self.enter_text(PerformancePage.kip,kipinvalid)
        self.click(PerformancePage.job_title)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.js_click(PerformancePage.click_title)
        self.js_click(PerformancePage.submit)
        return self.get_text(PerformancePage.kpi_required)
    
    def invalid_addwithtitle(self,kip):
        self.click(BasePage.performance)
        self.js_click(PerformancePage.configure)
        self.click(PerformancePage.kip_select)
        self.js_click(PerformancePage.add)
        self.enter_text(PerformancePage.kip,kip)
        self.js_click(PerformancePage.submit)
        return self.get_text(PerformancePage.job_required)

    def invalid_max_rate(self,kip,maxrate):
        actions = ActionChains(self.driver)
        self.click(BasePage.performance)
        self.js_click(PerformancePage.configure)
        self.click(PerformancePage.kip_select)
        self.js_click(PerformancePage.add)
        self.enter_text(PerformancePage.kip,kip)
        self.click(PerformancePage.job_title)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.js_click(PerformancePage.click_title)
        self.clear(PerformancePage.max_rate)
        self.enter_text(PerformancePage.max_rate,maxrate)
        self.js_click(PerformancePage.submit)
        return self.get_text(PerformancePage.max_err)









        

