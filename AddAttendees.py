import sys, time, csv
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
except:
    msg = "Please instatall Selenium"
    print(msg)
    sys.exit(msg)

login = "jason.zheng@yale.edu"
pwd = "aB6K6@7rDMMZz%Lji*!Qokfv"
attendeeList = "please.csv" #Tab-delimited file containing the firstname, surname and email address of your attendees

eventID = "602715407007" #eg open your event then see the URL to obtain the ID, eg https://www.eventbrite.com.au/myevent?eid=123456
ticketID = "quant_990258639" #Use the Dev Tools inspector to determine the ID of the ticket type you wish to add (http://i.imgur.com/RIYANW1.png)
faceValueID = "gross_990258639"

#Open a browser at the event homepage
fp = webdriver.FirefoxProfile()
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("https://www.eventbrite.com./attendees-add?eid=" + str(eventID))
username = browser.find_element(By.ID, 'email')
password = browser.find_element(By.ID, 'password')
username.send_keys(login)
password.send_keys(pwd)
loginButton = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[1]/div/div[2]/div/form/div[4]/div/button")
loginButton.click()
time.sleep(5)

#Iterate through each name in the input file
#with open(attendeeList) as inFile:
#    lines = inFile.readlines()
#    for line in lines:
#        tokens = line.split("\t")
#        firstname = tokens[0]
#        surname = tokens[1]
#        email = tokens[2]
#        print("Adding " + firstname + " " + surname + " (" + email + ")")
#        print(tokens[0])
#        print(tokens[1])
#        print(tokens[2])
        
        #Add each person to the guest list
#        try:
with open(attendeeList) as cp_csv:
    rows = csv.reader(cp_csv)
    for row in rows:
        firstname = row[0]
        surname = row[1]
        email = row[2]
        print("Adding " + firstname + " " + surname + " (" + email + ")")
        try:

            browser.get("https://www.eventbrite.com/attendees-add?eid=" + str(eventID))

            time.sleep(5)

            quantity = browser.find_element(By.ID, ticketID)
            quantity.send_keys("1")

            faceValue = browser.find_element(By.ID, faceValueID)
            faceValue.send_keys("0")

            continueBtn = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[2]/section/section/form/div[3]/a")
            continueBtn.click()

            time.sleep(5)

            className = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/main/div/div[3]/section/section/div[1]/iframe")
            browser.switch_to.frame(className)

            time.sleep(5)

            first = browser.find_element(By.ID, "buyer.N-first_name")
            first.send_keys(firstname)

            last = browser.find_element(By.ID, "buyer.N-last_name")
            last.send_keys(surname)

            emailAddr = browser.find_element(By.ID, "buyer.N-email")
            emailAddr.send_keys(email)

            time.sleep(5)

            actions = ActionChains(browser)

            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.TAB)

            actions.send_keys(Keys.ENTER)

            actions.perform()


            time.sleep(5)
        except:
            print("There was a problem adding " + firstname + " " + surname)

browser.close()