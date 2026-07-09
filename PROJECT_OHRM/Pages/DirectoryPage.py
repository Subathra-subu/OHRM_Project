from selenium.webdriver.common.by import By

class DirectoryPage:

    employee_name = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div//input")

    job_title = (By.XPATH, "//label[text()='Job Title']/parent::div/following-sibling::div//div[contains(@class,'oxd-select-text')]")

    location = (By.XPATH, "//label[text()='Location']/parent::div/following-sibling::div//div[contains(@class,'oxd-select-text')]")

    search_btn = (By.XPATH,"//button[normalize-space()='Search']")

    reset_btn = (By.XPATH,"//button/span[normalize-space()='Reset']/parent::button")

    employee_cards = (By.XPATH,"//div[contains(@class,'orangehrm-directory-card')]")

    employee_name_results = (By.XPATH,"//div[contains(@class,'orangehrm-directory-card')]//p[contains(@class,'orangehrm-directory-card-header')]")

    auto_suggestion = (By.XPATH,"//div[@role='listbox']/descendant::span")

    no_record_message = (By.XPATH,"//div[contains(@class,'oxd-table-filter')]//following::span[normalize-space()='No Records Found']")

    error_message = (By.XPATH,"//input/ancestor::div[contains(@class,'oxd-input-group')]//span[contains(@class,'oxd-input-field-error-message')]")

    job_title_options = (By.XPATH, "//div[@role='listbox']//span")

    employee_job_titles = (By.XPATH, "//p[contains(@class,'orangehrm-directory-card-subtitle')]")

    employee_location_results = (By.XPATH, "//p[contains(@class,'orangehrm-directory-card-footer')]")

    location_dropdown = (By.XPATH, "//label[text()='Location']/parent::div/following-sibling::div//div[contains(@class,'oxd-select-text')]")

    location_options = (By.XPATH, "//div[@role='listbox']//span")