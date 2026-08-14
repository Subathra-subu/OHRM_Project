from selenium.webdriver.common.by import By


class PerformancePage:

    # Performance > Configure > KPI

    configure = (
        By.XPATH,
        "//li[contains(@class,'oxd-topbar-body-nav-tab') "
        "and contains(@class,'--parent')]"
    )

    kip_select = (
        By.XPATH,
        "//ul[contains(@class,'oxd-dropdown-menu')]"
        "//li[normalize-space()='KPIs']"
    )

    add = (
        By.XPATH,
        "//div[contains(@class,'orangehrm-header-container')]"
        "//button[normalize-space()='Add']"
    )

    kip = (
        By.XPATH,
        "//label[normalize-space()='Key Performance Indicator']"
        "/following::input[1]"
    )

    job_title = (
        By.XPATH,
        "//label[normalize-space()='Job Title']"
        "/following::div[contains(@class,'oxd-select-text')][1]"
    )

    submit = (
        By.XPATH,
        "//button[@type='submit']"
    )

    success_msg = (
        By.XPATH,
        "//p[normalize-space()='Successfully Saved']"
    )

    kpi_required = (
        By.XPATH,
        "//label[normalize-space()='Key Performance Indicator']"
        "/following::span[normalize-space()='Required'][1]"
    )

    job_required = (
        By.XPATH,
        "//label[normalize-space()='Job Title']"
        "/following::span[normalize-space()='Required'][1]"
    )

    max_rate = (
        By.XPATH,
        "//label[normalize-space()='Maximum Rating']"
        "/following::input[1]"
    )

    max_err = (
        By.XPATH,
        "//span[normalize-space()='Should be a number between 0-100']"
    )

    # IMPORTANT:
    # Do not use reset/following-sibling submit.
    search = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    search_msg = (
        By.XPATH,
        "//div[normalize-space()='Account Assistant']"
    )

    invalid_search = (
        By.XPATH,
        "//*[normalize-space()='No Records Found']"
    )

    @staticmethod
    def job_option(job_title):
        return (
            By.XPATH,
            f"//div[@role='option' or @role='listbox']"
            f"//span[normalize-space()={job_title!r}]"
        )