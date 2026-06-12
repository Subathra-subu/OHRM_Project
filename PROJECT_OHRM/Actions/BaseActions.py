from selenium.webdriver.support import expected_conditions as EC
from Utilities.Logger import log_generator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


class BaseActions:

    def __init__(self, driver, wait):

        self.driver = driver
        self.wait = wait
        self.logger = log_generator()

    
    def enter_text(self, locator, value):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.clear()
            element.send_keys(str(value))

            self.logger.info(f"Entered : {value}")

        except Exception as e:

            self.logger.error("Failed to Enter Text")
            self.logger.exception(e)
            raise

    
    def click(self, locator):

        try:

            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )

            element.click()

            self.logger.info("Element Clicked")

        except Exception as e:

            self.logger.error("Failed to Click")
            self.logger.exception(e)
            raise

   
   
    def get_text(self, locator):

        try:

            text = self.wait.until(
                EC.visibility_of_element_located(locator)
            ).text

            self.logger.info(f"Text : {text}")

            return text

        except Exception as e:

            self.logger.error("Failed to Get Text")
            self.logger.exception(e)
            raise

    
    def is_displayed(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.is_displayed()

        except:
            return False

    
    def get_attribute(self, locator, attribute):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.get_attribute(attribute)

        except Exception as e:

            self.logger.exception(e)
            raise

   
    def clear(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.clear()

        except Exception as e:

            self.logger.exception(e)
            raise

   
    def submit(self, locator):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.submit()

        except Exception as e:

            self.logger.exception(e)
            raise
    def js_click(self,locator):
        try:
            element=self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].click()",element)
            self.logger.info(f"JS Clicked{element}")
        except Exception as e:
            self.logger.error("Failed to click the element")
            self.logger.exception(e)
    def scroll_into_view(self,locator):
   
        try:
            element=self.wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView()",element)
        except Exception as e:
            self.logger.error("Failed to scroll into view of the element")
            self.logger.exception(e)

    def wait_for_visibility(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
            self.logger.info("Element is Visible")
            return element
        except Exception as e:

            self.logger.error("Element Not Visible")
            self.logger.exception(e)
            raise

    def wait_for_clickable(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable(locator))
            self.logger.info("Element is Clickable")
            return element
        
        except Exception as e:
            self.logger.error("Element Not Clickable")
            self.logger.exception(e)
            raise

    def is_visible(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()

        except:
            return False
    
    def wait_for_invisibility(self, locator, timeout=10):

        try:
            WebDriverWait(self.driver,timeout).until( EC.invisibility_of_element_located(locator))
            self.logger.info("Element Became Invisible")

        except Exception as e:
            self.logger.error("Element Still Visible")
            self.logger.exception(e)
            raise

    def wait_for_url_contains(self, expected_partial_url):
        try:
            self.logger.info(f"Waiting dynamically for URL to contain: '{expected_partial_url}'")
            self.wait.until(EC.url_contains(expected_partial_url))
            return self.driver.current_url
        except Exception as e:
            self.logger.error(f"URL failed to transition to target containing: '{expected_partial_url}'")
            self.logger.exception(e)
            raise
    def select_first_dropdown_option_via_js(self, listbox_locator):
        """
        Waits for the dropdown listbox container wrapper, validates that it has
        fully painted text records instead of temporary loading messages,
        and dispatches a hardware event sequence onto its first child element.
        """
        dropdown_element = self.wait_for_visibility(listbox_locator)
        
       
        WebDriverWait(self.driver, 7).until(
            lambda d: "searching" not in d.find_element(*listbox_locator).text.lower()
        )
        
        self.logger.info("Dispatching custom browser lifecycle events onto the first dropdown option element...")
        self.driver.execute_script(
            """
            var dropdown = arguments[0];
            if (dropdown && dropdown.firstElementChild) {
                var targetItem = dropdown.firstElementChild;
                var eventConfig = { bubbles: true, cancelable: true, view: window };
                
                // Complete sequence mirroring structural mouse interactions
                targetItem.dispatchEvent(new PointerEvent('pointerdown', eventConfig));
                targetItem.dispatchEvent(new MouseEvent('mousedown', eventConfig));
                targetItem.dispatchEvent(new PointerEvent('pointerup', eventConfig));
                targetItem.dispatchEvent(new MouseEvent('mouseup', eventConfig));
                targetItem.dispatchEvent(new MouseEvent('click', eventConfig));
            } else {
                console.error("DOM Error: target listbox wrapper or option elements are absent.");
            }
            """, 
            dropdown_element
        )

    def wait_for_element_value_attribute(self, locator, timeout=10):
        """
        Dynamic fluent wait wrapper that pauses execution until an element's 'value' attribute 
        is populated with text data (clearing default blank states).
        """
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).get_attribute("value").strip() != ""
        )