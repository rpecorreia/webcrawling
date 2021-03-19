from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys

url = 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'

driver = webdriver.Chrome('/Users/rpecorreia/Desktop/WebCrawling/chromedriver')
driver.get(url)
#10 sec timeout
wait = WebDriverWait(driver, 10)

# ----- PART 1 ----

#find the driver element
search = wait.until(lambda driver:driver.find_element_by_xpath('//*[@id="searchInput"]'))
driver.implicitly_wait(2)

#click on the element
search.click()
driver.implicitly_wait(2)

#write on the element (in this case in the search box)
search.send_keys('"Universidad Carlos III de Madrid"')
driver.implicitly_wait(2)
#click on the element and go to results page
el = driver.find_element_by_xpath('//*[@id="searchform-suggestions"]').click()

#find the number of references to “Universidad Carlos III de Madrid” in Wikipedia
numb = driver.find_element_by_xpath('//*[@id="mw-search-top-table"]/div[2]/strong[2]') 
#print in terminal the number of references to “Universidad Carlos III de Madrid”
print(f'1) {numb.text} results')

# ----- PART 2 ----

#find the driver element to the “Universidad Carlos III de Madrid” Wikipedia page to seek the number of students
search2 = wait.until(lambda driver:driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/main/div[3]/div[3]/div[3]/ul/li[1]/div[1]/a'))
driver.implicitly_wait(5)
# click on the element to open the new tab
search2.click()
driver.implicitly_wait(2)

#get the paragraph that contains the number of students
search3 = wait.until(lambda driver:driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]'))
driver.implicitly_wait(2)
#select just the number of students
selection = search3.text[len(search3.text)-16:len(search3.text)-11:]
#print in terminal the number of students
print(f'2) {selection} students')


