import playwright
from playwright.sync_api import sync_playwright
import time
import itertools
import keyboard
import sys
import colorama
from colorama import init, Fore
import threading

def exit_good():
    ''' 
    exit good
    '''
    if keyboard.is_pressed('esc'):
        print('Exiting')
        sys.exit(0)

def push_namelist(inputn):
    names = [name.strip() for name in inputn.split(',')]  # Make list names
    return names

def spawn_player(pin, player_num, names):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # want to see process: headless=False, otherwise: headless=True
        name_cycle = itertools.cycle(names)  # make cyclus from (packet)
        pagef = browser.new_page()
        for i in range(player_num):
            try:
                time.sleep(0.2)
                exit_good()
                page = browser.new_page()
                page.goto('https://lessonup.app/', wait_until='domcontentloaded')  # go to lessonup

                page.wait_for_selector('#pincodeInput') 
                page.fill("#pincodeInput", pin)  # enter pin
                print(Fore.GREEN+"entered pin")

                page.wait_for_selector("#player-name")
                player_name = next(name_cycle)  # get name
                page.fill("#player-name", player_name)  # enter name
                print(Fore.GREEN+"entered player name")


                page.wait_for_selector('div[data-role="submit-name-button"]')
                page.click('div[data-role="submit-name-button"]')  # enter name button click
                print(Fore.RED+"cracked!!!")

                print(Fore.YELLOW+f"Logged in player {player_name}")
                exit_good()
            except Exception as e:
                print(Fore.MAGENTA+f"Error logging in player {i+1}: {e}")
            finally:
                page.close()
        browser.close()

def main():
    name = input("What should the name of the bots be (type 'none' to get a cool name or 'packet' to choose a name packet): ")
    
    if name == 'packet':
        packet = input("Choose a packet: hitler, rickroll, famous, ascii\n")
        if packet == 'hitler':
            names = 'adolf hitler, adolf titler, adolf zitler, adolf nigler, adolf shitler, adolf dickler, adolf titler(tassive mits)'
            names = push_namelist(names)
        elif packet == 'rickroll':
            names = "We're no strangers to love, You know the rules , and so do I , A full commitment's what I'm thinking of, You wouldn't get this from any other guy, I just wanna tell you how I'm feeling , Gotta make you understand , Never gonna give you up , Never gonna let you down , Never gonna run around and desert you , Never gonna make you cry , Never gonna say goodbye , Never gonna tell a lie and hurt you , We've known each other for so long , Your heart's been aching but you're too shy to say it , Inside we both know what's been going on , We know the game and we're gonna play it , And if you ask me how I'm feeling , Don't tell me you're too blind to see , Never gonna give you up , Never gonna let you down , Never gonna run around and desert you , Never gonna make you cry , Never gonna say goodbye , Never gonna tell a lie and hurt you , Never gonna give you up , Never gonna let you down , Never gonna run around and desert you , Never gonna make you cry , Never gonna say goodbye , Never gonna tell a lie and hurt you (Oooh, give you up) , (Oooh, give you up) , (Oooh) Never gonna give ,  never gonna give , (Give you up) , (Oooh) Never gonna give , never gonna give,(Give you up) , We've known each other for so long , Your heart's been aching but you're too shy to say it , Inside we both know what's been going on , We know the game and we're gonna play it , I just wanna tell you how I'm feeling , Gotta make you understand , Never gonna give you up , Never gonna let you down , Never gonna run around and desert you , Never gonna make you cry , Never gonna say goodbye , Never gonna tell a lie and hurt you , Never gonna give you up , Never gonna let you down , Never gonna run around and desert you , Never gonna say goodbye , Never gonna tell a lie and hurt you , Never gonna give you up , Never gonna let you down , Never gonna run around and desert you , Never gonna make you cry , Never gonna say goodbye , Never gonna tell a lie and hurt you"
            names = push_namelist(names)
        elif packet == "famous":
            names = "chopped-chin , ninja , Karen , NPC , fem-boy , baddie , simp , sigma , shrek , caseoh , kai cenat , andrew tate , mr beast , quandale dingle , duke dennis , amir , lebron , "
            names = push_namelist(names)
        elif packet == "ascii":
            names = "卍 , 𓅭 ,  𓆉 ,  ✈✈🏢🏢 , 😁⃤ "
        else:
            print(Fore.MAGENTA+"Unknown packet. Exiting.")
            return

    elif name == "none":
        names = ["‎","‎ "]   # invisible caracter if you type none
    else:
        names = [name]  # use name if you type something else

    pin = input(Fore.BLUE+"What is the pin? ")
    much = input("specefic bots? 'enter' for 999999, just press enter")
    if much == '':
        much = 999999
    else:
        much = int(much)
    for i in range(2):
        thread_spawner1 = threading.Thread(target=spawn_player, args=(pin, much, names))
        time.sleep(0.3)
        thread_spawner2 = threading.Thread(target=spawn_player, args=(pin, much, names))
        time.sleep(0.3)
        thread_spawner3 = threading.Thread(target=spawn_player, args=(pin, much, names))
        time.sleep(0.3)
        thread_spawner4 = threading.Thread(target=spawn_player, args=(pin, much, names))
        time.sleep(0.3)
        thread_spawner5 = threading.Thread(target=spawn_player, args=(pin, much, names))
        time.sleep(0.3)
        thread_spawner6 = threading.Thread(target=spawn_player, args=(pin, much, names))
        time.sleep(0.3)
        thread_spawner7 = threading.Thread(target=spawn_player, args=(pin, much, names))
        time.sleep(0.3)
        thread_spawner8 = threading.Thread(target=spawn_player, args=(pin, much, names))
        time.sleep(0.3)
        thread_spawner1.start()
        time.sleep(0.5)
        print("started")
        thread_spawner2.start()
        time.sleep(0.5)
        print("started")
        thread_spawner3.start()
        time.sleep(0.5)
        print("started")
        thread_spawner4.start()
        time.sleep(0.5)
        print("started")
        thread_spawner5.start()
        time.sleep(0.5)
        print("started")
        thread_spawner6.start()
        time.sleep(0.5)
        print("started")
        thread_spawner7.start()
        time.sleep(0.5)
        print("started")
        thread_spawner8.start()
        time.sleep(0.5)
        print("started bot 8")

if __name__ == "__main__":
    main()