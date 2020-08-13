import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from little_john.view_trades import View_trades
from little_john.manual_trade import Manual_trade
import little_john.add_to_target_list as Target_List
from little_john.broker import Broker
from little_john.trade_bot import Trade_Bot
import json

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
    while run:
        Instance_Broker = Broker()
        os.system('clear' if os.name == 'nt' else 'clear')
        display_text(f'{Instance_Broker.balance}', f'{Instance_Trade_Bot.status}')
        ipt = input('> ')
        if ipt == 'quit':
            os.system('clear' if os.name == 'nt' else 'clear')
            sys.exit('thanks for using the app')
        elif ipt == '1':
            os.system('clear' if os.name == 'nt' else 'clear')
            view = View_trades('logs/trades.json')
            view.display()
        elif ipt == '2':
            # search_stocks.menu()
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
            # view_account.menu()
            True
        elif ipt == '6':
            Target_List.sub_menu()
            True
        else:
            print('Select correct option')


def display_text(balance, bot):
    print(f'\nHello, you have {balance} invested.')
    print(f'Bot is {bot}')
    print('menu')
    print('1. View current trades')
    print('2. Search for stocks')
    print('3. Make stock trade')
    print('4. Turn on(off) auto trading bot')
    print('5. View account balance and trading history')
    print('6. Add company to targeted company list')
    print('quit')
    print('What would you like to do?, Select number or type "quit" to exit app')


start()
