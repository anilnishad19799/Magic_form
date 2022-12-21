from selenium import webdriver
import time
import cv2 
import pytesseract
import base64
from PIL import Image
from io import BytesIO

from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Webriver browser = new FirefoxDriver()
# browser.get("//www.techbeamers.com/")
# WebElement ajaxControl = (new WebDriverWait(browser, 15)).until(ExpectedConditions.presenceOfElementLocated(By.id("DummyElement")));


opt = webdriver.FirefoxOptions()
opt.add_argument('-headless')

web = webdriver.Firefox(options=opt)

# web = webdriver.Firefox()
web.get('https://foscos.fssai.gov.in/')

time.sleep(2)

images = web.find_elements_by_tag_name('img')
for image in images:
    if(image.get_attribute('alt')=="Captcha"):
        c = image.get_attribute('src')
        a = c[23:]
        break

im = Image.open(BytesIO(base64.b64decode(a)))

pytesseract.pytesseract.tesseract_cmd=r"C:/Users/Admin/AppData/Local/Tesseract-OCR/tesseract.exe"
custom_config = r'--oem 3 --psm 6 outputbase digits'
c = pytesseract.image_to_string(im)

path1 = web.find_element_by_xpath('/html/body/app-root/div[2]/div/div[2]/input').click()

path2 = web.find_element_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/ul/li[3]/a').click()

Number = "20717030000293"
num = web.find_element_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[1]/form/div/div/div[3]/div/input').send_keys(Number)

cap = web.find_element_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[1]/form/div/div/div[4]/div/input').send_keys(c)

submit_button = web.find_element_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div/form/div/div/div[4]/button').click()

time.sleep(2)

# doc = BeautifulSoup(web.page_source, "html.parser")

# get_detail = web.find_elements_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[2]/div/form/div/div/div/div[1]/table/tbody/tr/td')
# for item in get_detail:
#     text = item.text
#     print(text)
#     if(text == "View Products"):
#         web.find_element_by_link_text('View Products').click()
#         time.sleep(1)
#         element = web.find_elements_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[2]/div[2]/table/tbody')
#         for data in element:
#             get_data = data.text
#             print(get_data)
        # element = web.find_elements_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[2]/td')
        # for data in element:
        #     get_data = data.text
        #     print(get_data)
    
fassai_detail = []
Get_detail = web.find_elements_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[2]/div/form/div/div/div/div[1]/table/tbody/tr/td')
for item in Get_detail:
    company_detail = item.text
    print(company_detail)
    fassai_detail.append(company_detail)
    if(company_detail == "View Products"):
        web.find_element_by_link_text('View Products').click()
        time.sleep(1)
        Link_data = web.find_elements_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[2]/div[2]/table/tbody')
        for data in Link_data:
            product_data = data.text
            print(product_data)
            fassai_detail.append(product_data)

print(fassai_detail)

# get_detail = web.find_elements_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[2]/div/form/div/div/div/div[1]/table/tbody/tr/td')
# for item in get_detail:
#     texts = item.text
#     print(texts)
    # if(text == "View Products"):
    #     web.find_element_by_link_text('View Products').click()
    #     time.sleep(2)
    #     element = web.find_elements_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td')
    #     for data in element:
    #         get_data = data.text
    #         # print(type(full_data))
    #         print(get_data)
    #     element = web.find_elements_by_xpath('/html/body/app-root/app-index/main-layout/div/div[2]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div/div[4]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[2]/td')
    #     for data in element:
    #         get_data = data.text
    #         print(get_data)
    

# rows = doc.find('div', id='data-table-simple_wrapper').find('table', id ='data-table-simple').find('tbody').find('tr')
# fassai_detail  = []
# for row in rows.text:
    # fassai_detail.append(row)

# print(fassai_detail)
# fassai_detail = []
# for row in rows:
#     # print(row.attrs)
#     # Find the ones that don't have 'style' as an attribute
#     cells = row.find("td")
#     fassai_detail = {
#     'SNo': cells[0].text,
#     'Company_Name': cells[1].text,
#     'Premises Address': cells[2].text,
#     'License No': cells[3].text,
#     'License type': cells[4].text,
#     'valid': cells[5].text,
#     'List of Product': cells[6].text
#     }
#     fassai_detail.append(fassai_detail)

# print(fassai_detail)


time.sleep(3)