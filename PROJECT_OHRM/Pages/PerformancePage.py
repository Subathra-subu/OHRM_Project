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
    kpi_required=(By.XPATH,"//label[text()='Key Performance Indicator']/following::span[text()='Required'][1]")
    job_required=(By.XPATH,"//label[text()='Job Title']/following::span[text()='Required'][1]")
    max_rate=(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]")
    max_err=(By.XPATH,"//span[text()='Should be a number between 0-100']")
    search=(By.XPATH,'//button[@type="reset"]//following-sibling::button[@type="submit"]')
    search_msg=(By.XPATH,'//div[text()="Account Assistant"]')
    invalid_search=(By.XPATH,'//span[text()="No Records Found"]')
    search_title=(By.XPATH,"//div[@role='listbox']//span[text()='Automation Tester']")

    
