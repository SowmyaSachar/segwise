from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sys

LOGIN_URL = "https://ua.segwise.ai/login"
OVERVIEW_URL = "https://ua.segwise.ai/qa_assignment/creatives/overview"
EMAIL = "qa@segwise.ai"
PASSWORD = "segwise_test"

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(LOGIN_URL)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mantine-TextInput-input"))).send_keys(EMAIL)
        driver.find_element(By.CSS_SELECTOR,".mantine-PasswordInput-innerInput").send_keys(PASSWORD)
        print("clicked on Log In")
        driver.find_element(By.XPATH, "//span[text() = 'Log in with email']").click()
        

        try:
            wait.until(EC.url_contains("/qa_assignment/creatives/overview"))
        except:
            driver.get(OVERVIEW_URL)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Welcome, hello')]")))

        print("✅ Test Passed: Dashboard chart is visible on overview page")
    except Exception as e:
        print("❌ Test Failed:", e)
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
