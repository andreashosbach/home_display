config = {}
sensors = []

def read_config(config_file_name):
    # Read configuration file
    # Entry format: sensor_name=id
    global config
    global sensors
    
    general_config_file = open(config_file_name)
    config = eval(general_config_file.read())
    if config.has_key("sensors"):
        sensors = config["sensors"]
    else:
        print("No sensor config")
    return config

def has_config(key):
    # Check if a config value for a key exists
    return key in config.keys()
    
def get_config(key):
    # Get config value for a key
    return config[key]

def get_sensors():
    # Get configured sensors
    return sensors

