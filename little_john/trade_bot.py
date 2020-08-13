import sys
import finnhub

class Trade_Bot:
    """turns tradebot on and off, default initialization is off 
    """
    
    def __init__(self):
        self.status = 'off'
        
    def turn_on_or_off(self):    
      """ask if you want to turn bot on or off
      """  
      if self.status == 'off':
        self.status = 'on'
      if self.status == 'on':
        self.status = 'off'  
        
if __name__ == "__main__":
    test = Trade_Bot('./trade_history.json')
    test.turn_on_or_off()
        
