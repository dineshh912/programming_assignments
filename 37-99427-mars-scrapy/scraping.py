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
        "news": mars_news(browser),
        "featured_image": featured_image(browser),
        "hemisphere_images": hemisphere_images(browser),
        "facts": mars_facts(browser)
    }

    # stop browser and return data
    browser.quit()
    return data


def mars_news(browser):
    
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')

    slide_elem.find('div', class_='content_title')



    # Use the parent element to find the first a tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()
    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    news = {"news_title": news_title, "news_paragraph": news_p}

    return news


def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

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

def mars_facts(browser):

    df = pd.read_html('https://galaxyfacts-mars.com')[0]


    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # add  bootstrap 
    return df.to_html(classes = "table table-striped table-responsive")

if __name__ == '__main__':
    scrape_all()