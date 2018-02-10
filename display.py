#!/usr/bin/python

from threading import Timer
from config import get_config
from config import read_config
import cberry
from thingspeak import get_thingspeak_field_feed
import json
from datetime import datetime
from trace import trace
from trace import INFO
import sys

#Add: Weather data from https://openweathermap.org/api

def draw_background():
    
    cberry.setPenColor(cberry.BLACK)
    cberry.fillSquare(0, 0 * 48, 320, 48)
    cberry.fillSquare(0, 1 * 48, 320, 48)
    cberry.fillSquare(0, 2 * 48, 320, 48)
    cberry.fillSquare(0, 3 * 48, 320, 48)
    cberry.fillSquare(0, 4 * 48, 320, 48)

    cberry.writeText(5, 0 * 48 + 5, 3, "Out", cberry.WHITE, cberry.BLACK)
    cberry.writeText(5, 1 * 48 + 5, 3, "In", cberry.WHITE, cberry.BLACK)
    cberry.writeText(5, 2 * 48 + 5, 3, "Boiler", cberry.WHITE, cberry.BLACK)
    cberry.writeText(5, 4 * 48 + 5, 6, "Date", cberry.WHITE, cberry.BLACK)

    cberry.fillSquare(0, 3 * 48, 106, 48)
    cberry.fillSquare(106, 3 * 48, 106, 48)
    cberry.fillSquare(212, 3 * 48, 108, 48)

    cberry.writeText(5,   4 * 48 + 5, 3, "Heating", cberry.WHITE, cberry.BLACK)
    cberry.writeText(111, 4 * 48 + 5, 3, "Boiler", cberry.WHITE, cberry.BLACK)
    
def display():
# Resets the timer
    Timer(float(get_config("timer_wait")), display).start()
    
    draw_background()
   
    
def get_data(key):
    value = ""
    time = None
    
    data = get_config("data")[key]

    if(data["source"] == "THINGSPEAK"):
        field_id = data["field_id"] 
        channel_id = data["channel_id"]
        read_api_key = data["read_api_key"]
        number_of_results = 1
        
        raw_value = get_thingspeak_field_feed(channel_id, field_id, read_api_key, number_of_results)
        dict_value = json.loads(raw_value)

        value = dict_value["feeds"][0]["field" + str(field_id)];
            
        time_raw = dict_value["feeds"][0]["created_at"]
        time_raw = time[:time.find("+")]
        time = datetime.strptime(time_raw, "%Y-%m-%dT%H:%M:%S")
 
    elif(data["source"] == "TIME"):
        time_format = data["format"]
        value = datetime.now().strftime(time_format)
        time = value
    else:
        value = "Unknown source"
        time = None
            
    if(data[type] == "FLOAT"):
        value = float(value)
    if(data[type] == "STRING"):
        value = str(value)
        
    return (value, time)
    
def main():
# Main 
    print("Reading configuration")
    
    config_file_name = "display.config"
    if len(sys.argv) == 2:
        config_file_name = sys.argv[1]
        
    print(read_config(config_file_name))
    cberry.initScreen()
    display()        
    
# =============================================================================
if __name__ == "__main__":
    main()