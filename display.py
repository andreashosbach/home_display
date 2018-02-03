#!/usr/bin/python

from threading import Timer
from config import get_config
from config import read_config
import cberry
from thingspeak import get_thingspeak_field_feed
import json

def display():
# Resets the timer
    Timer(float(get_config("timer_wait")), display).start()
    
    for field in get_config("display"):
        x = field["x"]
        y = field["y"]
        font = field["font"]
        text = field["label"]
        
        data_name = field["value"]

        data = get_config("data")
        field_id = data[data_name]["field_id"] 
        channel_name = data[data_name]["channel"]
        
        channels = get_config("channels")
        channel = channels[channel_name]
        channel_id = channel["channel_id"]
        read_api_key = channel["read_api_key"]
        
        number_of_results = 1

        raw_value = get_thingspeak_field_feed(channel_id, field_id, read_api_key, number_of_results)
        dict_value = json.loads(raw_value)
        value = dict_value["feeds"][0]["field" + str(field_id)]; 
        
        if(data[type] == "FLOAT"):
            value = float(value)
            
        text = text % (value)
        cberry.writeText(x, y, font, text, cberry.BLACK, cberry.WHITE)
    
def main():
# Main 
    print("Reading configuration")
    print(read_config())
    cberry.initScreen()
    display()        
    
# =============================================================================
if __name__ == "__main__":
    main()