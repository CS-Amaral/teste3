from selenium import webdriver
import time
import json

import requests

browser = webdriver.Chrome()
browser.get('https://plug-tst.tpfe.com.br/ContractManagement_Web/Contracts.aspx')

browser.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[1]/div[2]/div[1]/div/div/div/input").send_keys("10222797428")
browser.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/input").send_keys("123456")
browser.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[1]/div[2]/div[3]/div/input").click()
browser.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/table/tbody/tr[1]/td[1]/a").click()
browser.find_element_by_xpath("/html/body/form/div[3]/div[2]/div[1]/div[4]/div[2]/a[2]").click()



a = 2

r = requests.get("https://plug-tst.tpfe.com.br/ContractManagement_Web/Contract_Monitoring.Monitoring.aspx?_ts=1616004263801")
print("TESTE1")
print(r)
print("TESTE2")

print(r.content)
#arquivoJson = json.loads(r.content)
#trends = r.json()
print("TESTE3")
print(arquivoJson)
print("TESTE4")
#print(trends['data']['attributes']['graph']['chart_data'])