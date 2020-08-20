import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import threading
import pyfiglet
from termcolor import colored, cprint
from little_john.view_trades import View_trades
from little_john.manual_trade import Manual_trade
import little_john.add_to_target_list as Target_List
from little_john.broker import Broker
from little_john.trade_bot import Trade_Bot
from little_john.search_stocks import SearchStocks
from little_john.trade_history import View_Trade_History
import json


def start():
    Instance_Trade_Bot = Trade_Bot()
    os.system('clear' if os.name == 'nt' else 'clear')
    run = True
    messages = Instance_Trade_Bot.message
    while run:
        Instance_Broker = Broker()
        os.system('clear' if os.name == 'nt' else 'clear')

        display_text(Instance_Broker.balance,
                    Instance_Trade_Bot.status, messages='None')
        ipt = input('> ').lower()
        if ipt == 'quit':
            os.system('clear' if os.name == 'nt' else 'clear')
            sys.exit('Thanks for using the app')
        elif ipt == '1':
            os.system('clear' if os.name == 'nt' else 'clear')
            view = View_trades()
            view.display()
        elif ipt == '2':
            search = SearchStocks()
            search.menu()
            True
        elif ipt == '3':
            os.system('clear' if os.name == 'nt' else 'clear')
            trade = Manual_trade()
            trade.menu()
            # display_text(f'{Instance_Broker.balance}', f'{Instance_Trade_Bot.status}')
        elif ipt == '4':
            Instance_Trade_Bot.turn_on_or_off()
            Instance_Trade_Bot.plan_b()
            True
        elif ipt == '5':
            hist = View_Trade_History('logs/trade_history.json')
            hist.display_history()
            True
        elif ipt == '6':
            Target_List.sub_menu()
            True
        else:
            print('Select correct option')


def display_text(balance, bot, messages):
    title = pyfiglet.figlet_format('LITTLE JOHN')
    print(title)
    balance = round(balance, 2)
    balance = colored(balance, 'green')
    print(f'Hello, you have ${balance} available.')
    if bot == 'on':
        bot = colored(bot, 'green')
    else:
        bot = colored(bot, 'red')
    print(f'R2D2 is currently {bot}')
    # blank line, once bot triggers something. My message.
    cprint('MENU', 'blue', attrs=['bold', 'underline'])
    print('1. View current trades')
    print('2. Search for stocks')
    print('3. Make stock trades')
    print('4. Turn R2D2 prediction bot on(off)')
    print('5. View trading history')
    print('6. Add company to targeted company list')
    print('quit\n')
    print('What would you like to do?, Select number or type "quit" to exit app\n')


thread = threading.Thread(
    target=start(), args=(), daemon=True)
thread.start()
thread.join()
