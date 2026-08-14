from selenium.webdriver.common.by import By


class PerformanceTrackersPage:

    configure = (
        By.XPATH,
        "//li[contains(@class,'oxd-topbar-body-nav-tab') "
        "and contains(@class,'--parent')]"
    )

    track_select = (
        By.XPATH,
        "//ul[contains(@class,'oxd-dropdown-menu')]"
        "//li[normalize-space()='Trackers']"
    )

    add_btn = (
        By.XPATH,
        "//button[normalize-space()='Add']"
    )

    tracker_name = (
        By.XPATH,
        "//label[normalize-space()='Tracker Name']"
        "/following::input[1]"
    )

    employee_name = (
        By.XPATH,
        "//label[normalize-space()='Employee Name']"
        "/following::input[1]"
    )

    reviewer_name = (
        By.XPATH,
        "//label[normalize-space()='Reviewers']"
        "/following::input[1]"
    )

    save_btn = (
        By.XPATH,
        "//button[@type='submit']"
    )

    success_msg = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast-content')]"
        "//p[contains(normalize-space(),'Successfully Saved')]"
    )

    tracker_required = (
        By.XPATH,
        "//label[normalize-space()='Tracker Name']"
        "/following::span[normalize-space()='Required'][1]"
    )

    search_employee = (
        By.XPATH,
        "//label[normalize-space()='Employee Name']"
        "/following::input[1]"
    )

    search_btn = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    search_result = (
        By.XPATH,
        "//div[contains(@class,'oxd-table-card')]"
        "//div[contains(@class,'oxd-table-cell')][2]"
    )

    no_record = (
        By.XPATH,
        "//*[normalize-space()='No Records Found']"
    )

    delete_btn = (
        By.XPATH,
        "//button[normalize-space()='Delete']"
    )

    delete_confirm_btn = (
        By.XPATH,
        "//button[normalize-space()='Yes, Delete']"
    )

    delete_success_msg = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast-content')]"
        "//p[contains(normalize-space(),'Successfully Deleted')]"
    )

    @staticmethod
    def employee_suggestion(employee):

        return (
            By.XPATH,
            "//div[contains(@class,'oxd-autocomplete-option')]"
            f"//span[normalize-space()={employee!r}]"
        )

    @staticmethod
    def reviewer_suggestion(reviewer):

        return (
            By.XPATH,
            "//div[contains(@class,'oxd-autocomplete-option')]"
            f"//span[normalize-space()={reviewer!r}]"
        )

    @staticmethod
    def tracker_checkbox(tracker):

        return (
            By.XPATH,
            "//div[contains(@class,'oxd-table-card')]"
            f"[.//*[normalize-space()={tracker!r}]]"
            "//input[@type='checkbox']"
        )