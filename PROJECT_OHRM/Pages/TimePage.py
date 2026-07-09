from selenium.webdriver.common.by import By

class TimePage:

    PROJECT_INFO = (
        By.XPATH,
        "//li[contains(@class,'oxd-topbar-body-nav-tab')][4]"
    )

    CUSTOMER = (
        By.XPATH,
        "(//a[@role='menuitem'])[1]"
    )

    ADD_BTN = (
        By.XPATH,
        "//button[@type='button' and contains(@class,'oxd-button--secondary')]"
    )

    CUSTOMER_NAME = (
        By.XPATH,
        "(//input[contains(@class,'oxd-input--active')])[2]"
    )

    DESCRIPTION = (
        By.XPATH,
        "//textarea"
    )

    SAVE_BTN = (
        By.XPATH,
        "//button[@type='submit']"
    )

    popup_message = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast--success')]"
    )

    ALREADY_EXISTS_MESSAGE = (
        By.XPATH,
        "//span[contains(@class,'oxd-input-field-error-message')]"
    )

    ATTENDANCE = (
    By.XPATH,
    "//span[normalize-space()='Attendance']/parent::li"
)

    MY_RECORDS = (
        By.XPATH,
        "//a[normalize-space()='My Records']"
    )

    DATE = (
        By.XPATH,
        "//label[normalize-space()='Date']/ancestor::div[contains(@class,'oxd-input-group')]//input"
    )

    VIEW_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='View']"
    )

    RECORDS_FOUND = (
        By.XPATH,
        "//*[contains(normalize-space(),'Records Found')]"
    )