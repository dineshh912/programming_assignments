# importing packages
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # intialize headless driver for chrome
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # store result in dict
    data = {
        "hemisphere_images": hemisphere_images(browser)
    }

    # stop browser and return data
    browser.quit()
    return data

def hemisphere_images(browser):

    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'

    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    image_container_items = soup(browser.html, 'html.parser').find_all('div', class_='item')

    for item in image_container_items:
        # Retrive image title
        img_title = item.find_all('a', class_="itemLink product-item")[1].h3.text
        img_link = item.a['href']
        
        browser.visit(url+img_link)
        
        # Read page html
        img_soup = soup(browser.html,'html.parser').find('div',class_="downloads")
        # From img_soup find full res image link
        full_res_img_link = img_soup.find('a')['href']
        
        # add link into image url dict
        hemisphere_image_urls.append({'img_url':url+full_res_img_link,
                                    'title':img_title})

    
    return hemisphere_image_urls

if __name__ == '__main__':
    scrape_all()