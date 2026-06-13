from selenium.webdriver.common.by import By


class ChangePasswordPage:

    USER_MENU = (
        By.CSS_SELECTOR,
        "span.oxd-userdropdown-tab"
    )

    CHANGE_PASSWORD = (
        By.XPATH,
        "//a[contains(@href,'updatePassword')]"
    )

    OLD_PASSWORD = (
        By.XPATH,
        "//form//input[@type='password'][1]"
    )

    NEW_PASSWORD = (
        By.XPATH,
        "(//input[@type='password'])[2]"
    )

    CONFIRM_PASSWORD = (
        By.XPATH,
        "(//input[@type='password'])[3]"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    SUCCESS_POPUP = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast--success')]"
    )