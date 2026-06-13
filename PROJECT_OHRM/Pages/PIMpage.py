from selenium import webdriver
from selenium.webdriver.common.by import By

class PIMpage:
     
     addemployee_btn  = (By.XPATH, "//div[@class='oxd-topbar-body']/descendant::a[2]")
     fname            = (By.XPATH, "//input[@name='firstName']")
     mname            = (By.XPATH, "//input[@name='middleName']")
     lname            = (By.XPATH, "//input[@name='lastName']")
     create_lgn_dts   = (By.XPATH, "//input[@type='checkbox']//following-sibling::span")
     username         = (By.XPATH, "(//div[contains(@class,'oxd-input-group')]//input[@autocomplete='off'])[1]")
     password         = (By.XPATH, "(//div[contains(@class,'oxd-input-group')]//input[@type='password'])[1]")
     confirm_password = (By.XPATH, "(//div[contains(@class,'oxd-input-group')]//input[@type='password'])[2]")
     save_btn         = (By.XPATH, "//div[@class='oxd-form-actions']/child::button[@type='submit']")
     employee_nmae =  (By.XPATH,"//div[@class='oxd-layout-container']/descendant::input[1]")
     emp_id_search =(By.XPATH,"//div[@class='oxd-layout-container']/descendant::input[2]")
     emp_id_get = (By.XPATH,"//div[@class='oxd-layout-container']/descendant::input[5]")
     search_emp = (By.XPATH,"//div[@class='oxd-table-filter-area']/descendant::button[@type='submit']")
     user_area = (By.XPATH,"//div[@class='oxd-table-card']")
     fullname = (By.XPATH,"//input[@name='firstName']")
     emp_list = (By.XPATH,"//div[@class='oxd-topbar-body']/descendant::a[1]")
     personal_details = (By.XPATH,"//div[@class='orangehrm-background-container']/descendant::h6[contains(@class, 'oxd-text oxd-text--h6 orangehrm-main-title')][1]")
     form_loader = (By.CLASS_NAME, "oxd-form-loader")
     lname_err_msg = (By.XPATH,"//div[@class='--name-grouped-field']/descendant::span")
     configuration = (By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent --visited'")
     custom_fields = (By.XPATH,"//ul[@class='oxd-dropdown-menu']/descendant::a[2]")
     add_custom_field = (By.XPATH,"//div[@class='orangehrm-custom-field-title']/following::button[1]")
     