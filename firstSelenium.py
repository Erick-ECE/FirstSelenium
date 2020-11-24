# first selenium program
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

employees= {'Empleado1': 1234,'Empleado2':9876}

driver = webdriver.Chrome(executable_path='/home/usuario/ChromeWebDriver/chromedriver')

for i in employees:
    print(i, "is Loading!...")
    
    # open the webPage
    driver.get('http://thedemosite.co.uk/savedata.php')
    time.sleep(1) #wait for the page to load

    #find the inputtext to set the user to the logger
    user = driver.find_element_by_name("username")
    # set the value to the inputtext
    user.send_keys(i)

    #find the inputtext to set the password
    password = driver.find_element_by_name("password")
    password.send_keys(employees[i]) #set the employee password

    #click save
    logSave = driver.find_element_by_name("FormsButton2")
    logSave.click()

    ############### part 2 verify the acaounts created ##################

    #verify the employees acounts created
    driver.get("http://thedemosite.co.uk/login.php")
    time.sleep(1) #wait for the page to load

    # send data to veryfy the log
     #find the inputtext to set the user to the logger
    user = driver.find_element_by_name("username")
    # set the value to the inputtext
    user.send_keys(i)

    #find the inputtext to set the password
    password = driver.find_element_by_name("password")
    password.send_keys(employees[i]) #set the employee password

    #click save
    logSave = driver.find_element_by_name("FormsButton2")
    logSave.click()

driver.close() 