
from lib2to3.pgen2 import driver
import scrapy
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class QuotesSpider(scrapy.Spider):
    name = "bime"
    start_urls = [
        "https://www.azki.app/car-insurance/third-party-insurance?vehicleTypeID=1&vehicleModelID=243051&vehicleBrandID=24&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&credit=12"
        
    ]

    def parse(self, response):
        # give the links want to scrap

        linklist = ["https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=243051&vehicleBrandID=24&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=243061&vehicleBrandID=24&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=807206&vehicleBrandID=24&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=807173&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434071&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434081&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434091&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434111&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434131&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434141&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434151&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434161&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=806876&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=807173&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12",
        "https://www.azki.app/car-insurance/third-party-insurance?imported=false&vehicleTypeID=1&vehicleModelID=434061&vehicleBrandID=43&vehicleConstructionYear=1400&vehicleUsageID=1&withoutInsure=true&zeroKilometer=false&cover=16&credit=12"

        ]
        for link in linklist:
            try:
                #create the selenium driver
                #change the addres googlechrome drive has it

                self.driver = webdriver.Chrome("D:\\Python\\bime\\bime\\bime\\spiders\\chromedriver.exe")
                self.driver.maximize_window()
                self.driver.get(link)
                
                #wait for find this element and complitly refresh the web page

                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "CardPriceArea_price__1ucFI"))
                )
                
                #get the name element

                element3=self.driver.find_elements(By.CLASS_NAME,"CardBrandArea_title__33p1t")

                #skip the toturial

                btn = self.driver.find_element(By.XPATH,'//*[@id="react-joyride-step-0"]/div/div/div[1]/div[2]/div/button')
                btn.click()

                #get the name car element
                carname_parent = self.driver.find_element(By.CLASS_NAME,'InfoManagerOfComparePage_OrderInfo__2du0Q')
                carname = carname_parent.find_elements(By.TAG_NAME,"div")

                #create the list for details
                pricelist = []
                bime_name = []

                #fill the lists

                for i in range(len(element)):
                    pricelist.append(element[i].text)
                    
                    bime_name.append(element3[i].text)

                #get the output

                yield{
                    "carmodel":carname[1].text+" "+carname[2].text+ " "+carname[3].text
                }

                for x in range(len(pricelist)):
                    yield {
                        
                        "price" : pricelist[x],
                        "Bime name" : bime_name[x]
                        }
                self.driver.quit()
            except:
                self.driver.quit()
                continue
                
            
        


# run with this cli code : scrapy crawl bime -o output.json -s FEED_EXPORT_ENCODING=utf-8