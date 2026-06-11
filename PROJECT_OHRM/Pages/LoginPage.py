from selenium.webdriver.common.by import By

class LoginPage:

    USERNAME = (By.XPATH , "//input[@name='username']" )

    PASSWORD = (By.XPATH , "//input[@name='password']" )

    LOGIN_BUTTON = (By.XPATH , "//button[@type='submit']" )

    INVALID_CREDENTIALS_MESSAGE = (By.XPATH , "//div[@role='alert']//descendant::p" )

    