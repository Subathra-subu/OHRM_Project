from selenium.webdriver.common.by import By
class PerformancePage:
    perform = (By.XPATH,"//a[@class='oxd-main-menu-item active toggle']")
    configure = (By.XPATH,'//li[@class="oxd-topbar-body-nav-tab --parent"]')
    kip_select = (By.XPATH,'//ul[@class="oxd-dropdown-menu"]//child::li[1]')
    add = (By.XPATH,'//div[@class="orangehrm-header-container"]//child::button')
    kip = (By.XPATH,"//label[text()='Key Performance Indicator']/following::input[1]")
    job_title = (By.XPATH,"//div[@class='oxd-select-text-input']")
    click_title = (By.XPATH,'//div[text()="Account Assistant"]')
    submit = (By.XPATH,'//button[@type="submit"]')
    success_msg = (By.XPATH,"//p[text()='Successfully Saved']")
    required=(By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')

