# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPersona():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_persona(self):
    self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    self.driver.set_window_size(790, 816)
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("admin")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("123")
    self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
    self.driver.find_element(By.LINK_TEXT, "Personas").click()
    self.driver.find_element(By.CSS_SELECTOR, "li > .addlink").click()
    self.driver.find_element(By.ID, "id_nombre").click()
    self.driver.find_element(By.ID, "id_nombre").send_keys("Felix")
    self.driver.find_element(By.ID, "id_apellido_paterno").click()
    self.driver.find_element(By.ID, "id_apellido_paterno").send_keys("Lima")
    self.driver.find_element(By.ID, "id_apellido_materno").click()
    self.driver.find_element(By.ID, "id_apellido_materno").send_keys("Valdez")
    self.driver.find_element(By.NAME, "_save").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .action-select").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .action-select").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) .action-select").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) .action-select").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) .action-select").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) .action-select").click()
    self.driver.find_element(By.NAME, "action").click()
    dropdown = self.driver.find_element(By.NAME, "action")
    dropdown.find_element(By.XPATH, "//option[. = 'Delete selected personas']").click()
    self.driver.find_element(By.NAME, "index").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(9)").click()
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
  