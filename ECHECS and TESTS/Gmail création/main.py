from Gmail_creator.gmail_controls import Gmail
from Gmail_creator import basic_functions as basic_functions
from selenium_stealth import stealth



def create_new_mail() :
    with Gmail(likehooman=True) as bot :
        stealth(bot,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
        bot.land_first_page()
        bot.click_on_sing_in()
        username,last_name, password = basic_functions.creating_pass_and_user_name()
        bot.fill_form(last_name, username, password)
        bot.click_next()
        #bot.check_antibot()
        print(username,last_name, password)
        #basic_functions.add_account_to_database(name, password) 
        #basic_functions.substract_last_account()

create_new_mail()
with Gmail() as bot :
    bot.land_first_page()
    