# https://www.instagram.com/reel/C6oQJq1RTr3/?utm_source=ig_web_copy_link

import time,random
from  playwright.sync_api import sync_playwright
import mysql.connector
def short_random_delay():
    delay = random.randint(2,5)
    time.sleep(delay)

def medium_random_delay():
    delay = random.randint(6,15)
    time.sleep(delay)

def large_random_delay():
    delay = random.randint(15,25)
    time.sleep(delay)
def wait_element_not_visisble(page,element,states,times):
    try:
        page.wait_for_selector(element, state=states, timeout=times)
    except:
        pass

def save_profile_notification(page):
    try:
        short_random_delay()
        wait_element_not_visisble(page,'div._ac8f','visible',200)
        page.locator('div._ac8f').click()
        medium_random_delay()
    except:
        pass

def notification_off_check(page):
    try:

        page.wait_for_selector('div ._a9-z button')
        elements = page.locator('div ._a9-z button')
        last_element = elements.nth(-1)  # Target the last element
        medium_random_delay()
        last_element.click()
        short_random_delay()
    except:
        pass


def post_url(page, url):
    page.goto(url)
    short_random_delay()
    comment_()
    short_random_delay()

    # for comment in comment_section:
    #     print(comment.inner_text())
def comment_(keywords='mata'):
    try:
        page.wait_for_selector('div[class="x78zum5 xdt5ytf x1iyjqo2"]')
    except:
        pass
    while True:
        try:
            elements = page.query_selector_all(
                'div[class="x78zum5 xdt5ytf x1iyjqo2"] div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"]')
            if elements:
                last_element = elements[-1]
                page.evaluate('element => element.scrollIntoView()', last_element)
                short_random_delay()
                for comment in elements:
                    try:
                        comment_text = comment.inner_text().lower()
                        if keywords and keywords.lower() in comment_text:
                            print(f"Keyword '{keywords}' found: {comment_text}")
                        else:
                            print(comment_text)
                        create_table_and_insert_comment(comment.inner_text())
                    except:
                        pass

                short_random_delay()
                time.sleep(2)
                new_elements = page.query_selector_all(
                    'div[class="x78zum5 xdt5ytf x1iyjqo2"] div[class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"]')
                if len(elements) == len(new_elements):
                    break
            else:
                print("No elements found")
                break
        except:
            break
            pass



def create_table_and_insert_comment(comment):
    conn= mysql.connector.connect(host='127.0.0.1', database='instagram', user='root', password='root')
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                comment TEXT
            )
        ''')
        sql = "INSERT INTO comments (comment) VALUES (%s)"
        val = (comment,)
        cursor.execute(sql, val)
        conn.commit()
        print("Comment inserted successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()





def goto_profile_page(profile,comment_no):
    a=0
    page.goto(profile)
    try:
        page.wait_for_selector('div[class="x1q0g3np x2lah0s"]')
    except:
        pass
    short_random_delay()
    time.sleep(2)
    for i in range(comment_no):
        try:
            if a==0:
                a=1
                posts = page.query_selector('div[class="_ac7v xzboxd6 xras4av xgc1b0m"] div[class="_aagu"]')
                posts.click()
                short_random_delay()
                time.sleep(2)
                page.reload()
                short_random_delay()
                short_random_delay()
                comment_()
                short_random_delay()
            else:
                page.query_selector_all('div[class="_ac7v xzboxd6 xras4av xgc1b0m"] div[class="_aagu"]')[i].click()
                short_random_delay()
                time.sleep(3)
                comment_()
                short_random_delay()
        except:
            pass




def login_user(page,email, password):
    username = page.locator("input[name='username']")
    username.highlight()
    username.type(email,delay=100)
    short_random_delay()
    username = page.locator("input[name='password']")
    username.highlight()
    username.type(password,delay=100)
    short_random_delay()
    username = page.locator("button[type='submit']")
    username.click()
    wait_element_not_visisble(page, 'div[data-visualcompletion="loading-state"]','hidden',2000)
    medium_random_delay()
    save_profile_notification(page)
    short_random_delay()
    short_random_delay()
    notification_off_check(page)
    short_random_delay()
    short_random_delay()
with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False,slow_mo=700,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    # create a new page in a pristine context.
    page = context.new_page()
    short_random_delay()
    page.goto('https://www.instagram.com')
    short_random_delay()
    try:
        page.wait_for_selector("input[name='username']")
    except:
        pass
    short_random_delay()
    login_user(page, '70_077503','Kami@123')
    short_random_delay()
    # post_url(page, 'https://www.instagram.com/p/C60TQIIvAGx/')
    short_random_delay()
    goto_profile_page('https://www.instagram.com/ahsaan12223/', 3)
    short_random_delay()
    page.close()



