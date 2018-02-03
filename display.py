#!/usr/bin/python

import sys
from threading import Timer
from config import get_config
from config import read_config
import cberry
import thingspeak
from thingspeak import get_thingspeak_field_feed
import json

# =============================================================================
# Measure and write every x seconds
# =============================================================================
# Resets the timer
def display():
    Timer(float(get_config("timer_wait")), display).start()
    
    channel_id = 398939
    field_id = 1
    read_api_key = "RX6KEENEBPKDVN9L"
    number_of_results = 1

    data = get_thingspeak_field_feed(channel_id, field_id, read_api_key, number_of_results)
    dict = json.loads(data)
    temperature = dict["feeds"][0]["field1"]; 
    cberry.writeText(10, 100, 5, str(temperature), cberry.BLACK, cberry.WHITE)
      
    
# =============================================================================
# Main ---
# =============================================================================
def main():
    print("Reading configuration")
    print(read_config())
    cberry.initScreen()
    display()        
    
# =============================================================================
if __name__ == "__main__":
    main()