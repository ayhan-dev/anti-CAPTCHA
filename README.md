# anti-CAPTCHA

  - Solve Google reCAPTCHA less than 5 seconds! 

  - This is a Python script to solve Google reCAPTCHA using the DrissionPage library. Selenium implementation will be added soon.


## install 
```bash
1- sudo apt-get install ffmpeg    
2- sudo apt install virtualenv                                                   
3- virtualenv ayhan
4- source ayhan/bin/activate   
5- pip install -r requirements.txt  
```

## Usage
```python
from OFD import OFD
from DrissionPage import ChromiumPage

ok = ChromiumPage()
captcha = OFD(ok)
ok.get("https://www.google.com/recaptcha/api2/demo")
captcha.solveCaptcha()
ok.ele("#recaptcha-demo-submit").click()
ok.close()
```
