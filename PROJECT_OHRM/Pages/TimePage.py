from selenium.webdriver.common.by import By

class TimePage :

    PROJECT_INFO = (By.XPATH, "//li[contains(@class,'oxd-topbar-body-nav-tab')][4]")

    CUSTOMER = (By.XPATH, "(//a[@role='menuitem' and contains(@class,'oxd-topbar-body-nav-tab-link')])[1]")

    ADD_BTN = (By.XPATH, "//button[@type='button' and contains(@class,'oxd-button--secondary')]")

    CUSTOMER_NAME = (By.XPATH, "(//input[contains(@class,'oxd-input--active')])[2]")

    DESCRIPTION = (By.XPATH, "//textarea[contains(@class,'oxd-textarea--active')]")

    SAVE_BTN = (By.XPATH, "//button[@type='submit' and contains(@class,'oxd-button--secondary')]")

    popup_message = (By.XPATH, "//div[contains(@class,'oxd-toast') and contains(@class,'oxd-toast--success')]")

    ALREADY_EXISTS_MESSAGE = (By.XPATH, "//span[contains(@class,'oxd-input-field-error-message')]")




