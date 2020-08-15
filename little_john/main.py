import json
from little_john.trade_history import View_Trade_History
from little_john.search_stocks import SearchStocks
from little_john.trade_bot import Trade_Bot
from little_john.broker import Broker
import little_john.add_to_target_list as Target_List
from little_john.manual_trade import Manual_trade
from little_john.view_trades import View_trades
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

"""
>> python Little_John/main.py

Hello, you have {balance} invested.
Bot is {on | off}

Menu
View current trades
Search for stocks
Make stock trade
Turn on(off) auto trading bot
View account balance and trading history
.
 What would you like to do?
> <select number>

"""


def start():
    Instance_Trade_Bot = Trade_Bot()
    os.system('clear' if os.name == 'nt' else 'clear')
    run = True
    messages = Instance_Trade_Bot.message
    while run:
        Instance_Broker = Broker()
        os.system('clear' if os.name == 'nt' else 'clear')

        display_text(f'{Instance_Broker.balance}',
                     f'{Instance_Trade_Bot.status}', messages='None')
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
    print(f'\nHello, you have {balance} invested.')
    print(f'Bot is {bot}')
    # blank line, once bot triggers something. My message.
    print(f'Messages: {messages}')
    print('MENU')
    print('1. View current trades')
    print('2. Search for stocks')
    print('3. Make stock trade')
    print('4. Turn on(off) auto trading bot')
    print('5. View account balance and trading history')
    print('6. Add company to targeted company list')
    print('quit')
    print('What would you like to do?, Select number or type "quit" to exit app')


start()
