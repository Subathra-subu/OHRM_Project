from selenium.webdriver.common.by import By

class DirectoryPage:

    employee_name = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div//input")

    job_title = (By.XPATH, "//label[text()='Job Title']/parent::div/following-sibling::div//div[contains(@class,'oxd-select-text')]")

    location = (By.XPATH, "//label[text()='Location']/parent::div/following-sibling::div//div[contains(@class,'oxd-select-text')]")

    search_btn = (By.XPATH, "//button[normalize-space()='Search']")

    reset_btn = (By.XPATH, "//button[normalize-space()='Reset']")

    employee_cards = (By.XPATH, "//div[contains(@class,'orangehrm-directory-card')]")

    employee_name_results = (By.XPATH, "//p[contains(@class,'orangehrm-directory-card-header')]")

    auto_suggestion = (By.XPATH, "//div[@role='listbox']//span")