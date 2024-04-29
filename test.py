from DrissionPage import ChromiumPage 
from OFD import OFD

clas = ChromiumPage()
captcha = OFD(driver)

clas.get("https://www.google.com/recaptcha/api2/demo")
captcha.solveCaptcha()

clas.ele("#recaptcha-demo-submit").click()
clas.close()
