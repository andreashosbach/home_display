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


def draw_field(number, text, data, format_string):
    y = number * 48

    value, time = get_data(data)

    cberry.setPenColor(cberry.WHITE)
    cberry.fillSquare(0, y, 320, 48)
    
    cberry.writeText(5, y + 1, 4, text, cberry.WHITE, cberry.BLACK)
    if value == False:
        cberry.setPenColor(cberry.RED)
    else:
        cberry.setPenColor(cberry.BLACK)
    
    if time != None:
#        cberry.writeText(5, y + 30, 4, time.strftime("%d.%m. %H:%M"), cberry.WHITE, cberry.BLACK)
        time_diff = datetime.now() - time
        if time_diff.total_seconds() > 1800: # 30 min
            cberry.setPenColor(cberry.RED)
        elif time_diff.total_seconds() > 600: # 5 min 
            cberry.setPenColor(cberry.YELLOW)
        else:
            cberry.setPenColor(cberry.GREEN)
    
    cberry.fillCircle(300, y + 24 - 4, 8)
        
    cberry.writeText(120, y + 2, 6, format_string % value, cberry.WHITE, cberry.BLACK)

    cberry.setPenColor(cberry.BLACK)
    cberry.drawSquare(0, y, 320, 48)

def draw():

    draw_field(0, "Out", "out_temp", "%05.2f C")
    draw_field(1, "In", "in_temp", "%05.2f C")
    draw_field(2, "Boiler", "boiler_temp", "%05.2f C")
    draw_field(4, "Time", "time", "%s")

    # Field 4
    cberry.setPenColor(cberry.WHITE)
    cberry.drawSquare(0, 3 * 48, 320, 48)

    cberry.setPenColor(cberry.BLACK)
    cberry.drawSquare(0, 3 * 48, 106, 48)
    cberry.drawSquare(106, 3 * 48, 106, 48)
    cberry.drawSquare(212, 3 * 48, 108, 48)

    cberry.writeText(5,   3 * 48 + 5, 4, "Heat", cberry.WHITE, cberry.BLACK)
    cberry.writeText(111, 3 * 48 + 5, 4, "Boiler", cberry.WHITE, cberry.BLACK)

    cberry.drawSquare(0, 3 * 48, 320, 48)


def display():
# Resets the timer
    Timer(float(get_config("timer_wait")), display).start()
    
    draw()
   
    
def get_data(key):
    value = False
    time = None
    
    data = get_config("data")[key]

    if(data["source"] == "THINGSPEAK"):
        field_id = data["field_id"] 
        channel_id = data["channel_id"]
        read_api_key = data["read_api_key"]
        number_of_results = 1
        
        raw_value = get_thingspeak_field_feed(channel_id, field_id, read_api_key, number_of_results)
        if raw_value != False:
            dict_value = json.loads(raw_value)

            value = dict_value["feeds"][0]["field" + str(field_id)];
            
            time_raw = dict_value["feeds"][0]["created_at"]
            time_raw = time_raw[:time_raw.find("+")]
            time = datetime.strptime(time_raw, "%Y-%m-%dT%H:%M:%S")
 
    elif(data["source"] == "TIME"):
        time_format = data["format"]
        value = datetime.now().strftime(time_format)
        time = None
    else:
        value = False
        time = None

    if value != None:            
        if(data["type"] == "FLOAT"):
            value = float(value)
        if(data["type"] == "STRING"):
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