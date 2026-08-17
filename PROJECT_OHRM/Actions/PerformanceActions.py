from Pages.PerformancePage import PerformancePage
from Pages.BasePage import BasePage
from Actions.BaseActions import BaseActions


class PerformanceActions(BaseActions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def _open_kpi_page(self):

        self.click(
            BasePage.performance
        )

        self.click(
            PerformancePage.configure
        )

        self.click(
            PerformancePage.kip_select
        )

    def _select_job_title(self, title):

        self.click(
            PerformancePage.job_title
        )

        self.click(
            PerformancePage.job_option(title)
        )

    def add_kpi(self, kip):

        self._open_kpi_page()

        self.click(
            PerformancePage.add
        )

        self.enter_text(
            PerformancePage.kip,
            kip
        )

        self._select_job_title(
            "Account Assistant"
        )

        self.click(
            PerformancePage.submit
        )

        return self.get_text(
            PerformancePage.success_msg
        )

    def invalid_add(self, kipinvalid):

        self._open_kpi_page()

        self.click(
            PerformancePage.add
        )

        self.enter_text(
            PerformancePage.kip,
            kipinvalid
        )

        self._select_job_title(
            "Account Assistant"
        )

        self.click(
            PerformancePage.submit
        )

        return self.get_text(
            PerformancePage.kpi_required
        )

    def invalid_addwithtitle(self, kip):

        self._open_kpi_page()

        self.click(
            PerformancePage.add
        )

        self.enter_text(
            PerformancePage.kip,
            kip
        )

        self.click(
            PerformancePage.submit
        )

        return self.get_text(
            PerformancePage.job_required
        )

    def invalid_max_rate(self, kip, maxrate):

        self._open_kpi_page()

        self.click(
            PerformancePage.add
        )

        self.enter_text(
            PerformancePage.kip,
            kip
        )

        self._select_job_title(
            "Account Assistant"
        )

        self.clear(
            PerformancePage.max_rate
        )

        self.enter_text(
            PerformancePage.max_rate,
            maxrate
        )

        self.click(
            PerformancePage.submit
        )

        return self.get_text(
            PerformancePage.max_err
        )

    def valid_search(self):

        self._open_kpi_page()

        self._select_job_title(
            "Account Assistant"
        )

        self.js_click(
            PerformancePage.search
        )

        return self.get_text(
            PerformancePage.search_msg
        )

    def invalid_search(self):

        self._open_kpi_page()

        self._select_job_title(
            "Chief Financial Officer"
        )

        self.js_click(
            PerformancePage.search
        )

        return self.get_text(
            PerformancePage.invalid_search
        )