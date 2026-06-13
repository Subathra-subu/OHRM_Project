from selenium.webdriver.common.by import By

class PerformanceTrackersPage:

    configure = (By.XPATH,'//li[@class="oxd-topbar-body-nav-tab --parent"]')
    track_select = (By.XPATH,'//ul[@class="oxd-dropdown-menu"]//li[2]')
    add_btn = (By.XPATH,"//button[normalize-space()='Add']")
    tracker_name = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
    employee_name = (By.XPATH,"//label[text()='Employee Name']/following::input[1]")
    reviewer_name = (By.XPATH,"//label[text()='Reviewers']/following::input[1]")
    save_btn = (By.XPATH,"//button[@type='submit']")
    success_msg = (By.XPATH,"//p[text()='Successfully Saved']")
    tracker_required = (By.XPATH,"//label[text()='Tracker Name']/following::span[text()='Required'][1]")
    search_employee = (By.XPATH,"//label[text()='Employee Name']/following::input[1]")
    search_btn = (By.XPATH,"//button[@type='reset']/following-sibling::button")
    search_result = (By.XPATH,"//div[@class='oxd-table-cell oxd-padding-cell'][2]")
    no_record = (By.XPATH,"//span[text()='No Records Found']")
    employee_suggestion = (By.XPATH,"//div[@role='option']//span")
    reviewer_suggestion = (By.XPATH,"//div[@role='option']//span")