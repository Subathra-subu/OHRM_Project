from selenium.webdriver.common.by import By

class LeavePage:

    assign_leave_menu = (By.XPATH,"//a[text()='Assign Leave']")

    employee_name = (By.XPATH,"//label[text()='Employee Name']/ancestor::div[contains(@class,'oxd-input-group')]//input")

    auto_dropdown = (By.XPATH,"//div[@role='listbox']")

    leave_type_dropdown = (By.XPATH,"//label[text()='Leave Type']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")

    leave_type_options = (By.XPATH,"//div[@role='option']")

    from_date = (By.XPATH,"(//input[contains(@class,'oxd-input')])[2]")

    to_date = (By.XPATH,"(//input[contains(@class,'oxd-input')])[3]")

    comments = (By.XPATH,"//textarea")

    assign_btn = (By.XPATH,"//button[normalize-space()='Assign']")

    success_message = (By.XPATH,"//p[contains(@class,'oxd-text--toast-message')]")

    error_message = (By.XPATH,"//span[contains(@class,'oxd-input-field-error-message')]")

    confirm_ok_button = (By.XPATH,"//div[contains(@class,'orangehrm-modal-footer')]//button[2]")