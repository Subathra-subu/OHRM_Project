from selenium.webdriver.common.by import By

class MaintenancePage:
    Access_rec = (By.XPATH, "//li[@class='oxd-topbar-body-nav-tab']/child::a")
    emp_name = (By.XPATH, "//div[@class='oxd-autocomplete-wrapper']//input")
    searching_text = (By.XPATH, "//div[@role='listbox']//*[contains(text(), 'Searching')]")
    
    # This matches the div[role='listbox'] container we saw in your screenshot
    auto_drop = (By.XPATH, "//div[@role='listbox']")
    
    search = (By.XPATH, "//button[@type='submit']")
    first_name = (By.XPATH, "//input[@name='firstName']")
    form_loader = (By.XPATH, "//div[@class='oxd-form-loader']")
    password = (By.XPATH, "//input[@type='password']")
    confirm = (By.XPATH, "//button[@type='submit']")