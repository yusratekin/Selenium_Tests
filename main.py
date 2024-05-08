from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Webdriver'ı yükle
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Google'ı ziyaret et
driver.get("https://www.google.com")

# Arama kutusunu bul ve "Python" kelimesini gir
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python")
search_box.submit()

# Sayfanın yüklenmesini bekle ve sonuçları yazdır
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for result in results:
    print(result.text)

# Tarayıcıyı kapat
driver.quit()
