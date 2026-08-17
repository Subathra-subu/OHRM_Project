from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class ClaimPage(BasePage):
    
    assign_claim = (By.XPATH,"//div[@class='orangehrm-header-container']/button")
    
    employee_name = (By.XPATH,"//div[@class='oxd-autocomplete-text-input--before']/following-sibling::input")
    
    event = (By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")
    
    currency = (By.XPATH,"(//div[@class='oxd-select-text-input'])[2]")
    
    create = (By.XPATH,"//button[@type='submit']")
    
    list_box = (By.CSS_SELECTOR, "div[role='listbox']")
    
    success_message = (By.XPATH,"//h6[text()='Assign Claim']")
    
    eventOption = (By.XPATH,"//div[contains(@class,'oxd-select-option')]//span[normalize-space()='Accommodation']")
    
    employee_name_option = (By.XPATH,"//div[contains(@class,'oxd-autocomplete-option') and not(contains(.,'Searching'))]")
    
    submitClaim = (By.XPATH,"//a[text()='Submit Claim']")
    
    eventOption = (By.XPATH,"//div[contains(@class,'oxd-select-option')]//span[normalize-space()='Accommodation']")
    
    currencyOption = (By.XPATH,"//label[contains(normalize-space(),'Currency')]/following::div[contains(@class,'oxd-select-text')][1]")
    
    submitButton = (By.CSS_SELECTOR,".oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-sm-button")
    