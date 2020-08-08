import sys
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
    run = True
    while run:
        display_text('$100', 'off')
        ipt = input('> ')
        if ipt == 'quit':
            sys.exit('thanks for using the app')
        elif ipt == 1:
            view_trades.menu()
        elif ipt == 2:
            search_stocks.menu()
        elif ipt == 3:
            make_trade.menu()
        elif ipt == 4:
            autobot.toggle()
        elif ipt == 5:
            view_account.menu()
        else:
            print('Select correct option')


def display_text(balance, bot):
    print(f'Hello, you have {balance} invested.')
    print(f'Bot is {bot}')
    print('menu')
    print('1. View current trades')
    print('2. Search for stocks')
    print('3. Make stock trade')
    print('4. Turn on(off) auto trading bot')
    print('5. View account balance and trading history')
    print('quit')
    print('What would you like to do?, Select number')


start()
