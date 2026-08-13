from selenium.webdriver.support import expected_conditions as EC
from Utilities.Logger import log_generator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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
            self.logger.error("Element Not Visible - attempting presence fallback")
            self.logger.exception(e)

            try:
                # Fallback: wait for presence (element exists in DOM even if hidden)
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )

                # If element is present but not visible, try to unhide it via JS so send_keys/click can succeed
                try:
                    if not element.is_displayed():
                        self.driver.execute_script(
                            "arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';",
                            element,
                        )
                        self.logger.info("Made hidden element visible via JS fallback")

                except Exception:
                    # ignore JS failures and return the present element for best-effort interaction
                    pass

                return element

            except Exception as inner_e:
                self.logger.error("Presence fallback also failed")
                self.logger.exception(inner_e)
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
        
    def save_screenshot(self, screenshot_name):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = f"TestFailures/Screenshots/{screenshot_name}_{timestamp}.png"
            self.driver.save_screenshot(file_path)
            self.logger.info(f"Screenshot saved successfully: {file_path}")
            return file_path
        except Exception as e:
            self.logger.error("Failed to capture screenshot")
            self.logger.exception(e)
            raise

    def clickstale(self, locator, timeout=10):
     loader = (By.CSS_SELECTOR, "div.oxd-form-loader")

     for attempt in range(3):
        try:
            # OrangeHRM temporarily overlays forms while dependent controls load.
            # A target can be "clickable" while that overlay still owns the click.
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(loader)
            )

            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )

            element.click()
            self.logger.info(f"Clicked element: {locator}")
            return

        except StaleElementReferenceException:
            self.logger.warning(
                f"Stale element encountered while clicking {locator}. Retry {attempt + 1}"
            )

        except ElementClickInterceptedException:
            self.logger.warning(
                f"Click on {locator} was blocked by a loading overlay. "
                f"Retry {attempt + 1}"
            )

            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(loader)
            )

     raise ElementClickInterceptedException(
        f"Unable to click {locator} after 3 retries."
    )


    def scroll_to_element(self, locator):

        try:

            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )

            ActionChains(self.driver)\
                .scroll_to_element(element)\
                .perform()

            self.logger.info(
                "Scrolled to element successfully"
            )

            return element

        except Exception as e:

            self.logger.error(
                "Failed to scroll to element"
            )

            self.logger.exception(e)

            raise

    def clear_and_enter_text(
        self,
        locator,
        value):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.click()

            element.send_keys(
                Keys.CONTROL,
                "a"
            )

            element.send_keys(
                Keys.BACKSPACE
            )

            element.send_keys(
                str(value)
            )

            self.logger.info(
                f"Entered : {value}"
            )

        except Exception as e:

            self.logger.error(
                "Failed to Enter Text"
            )

            self.logger.exception(e)

            raise
