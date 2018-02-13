import urllib
import urllib2
import sys 
from trace import trace
from trace import INFO
from trace import WARN
from trace import ERROR

def post_thingspeak_channel_update(sensor_measurement, write_api_key):
    #Send an HTTP request to update information about an existing channel.
    #https://ch.mathworks.com/help/thingspeak/update-channel-feed.html
    param_dict = {"key" : write_api_key}
    for measurement in sensor_measurement:
        param_dict[measurement["field"]] = measurement["value"]
    return thingspeak_post_request("update", param_dict)

def get_thingspeak_channel_status(channel_id, read_api_key, number_of_results):
    #Send an HTTP request to view channel status updates.
    #https://ch.mathworks.com/help/thingspeak/get-status-updates.html
    param_dict = {"api_key" : read_api_key, "results" : number_of_results}
    return thingspeak_get_request("channels/" + str(channel_id) + "/status.json", param_dict)

def get_thingspeak_channel(channel_id, profile_api_key):
    #Send an HTTP request to view channel status updates.
    #https://ch.mathworks.com/help/thingspeak/view-a-channel.html
    param_dict = {"api_key" : profile_api_key}
    return thingspeak_get_request("channels/" + str(channel_id) + ".json", param_dict)

def get_thingspeak_channel_list(profile_api_key):
    #Send an HTTP request to list all channels of a user.
    #https://ch.mathworks.com/help/thingspeak/list-all-channels-of-a-user.html
    param_dict = {"api_key" : profile_api_key}
    return thingspeak_get_request("channels.json", param_dict)

def get_thingspeak_channel_feed(channel_id, read_api_key, number_of_results):
    #Send an HTTP request to view channel feed data.
    #https://ch.mathworks.com/help/thingspeak/get-a-channel-feed.html
    param_dict = {"api_key" : read_api_key, "results" : number_of_results}
    return thingspeak_get_request("channels/" + str(channel_id)  + "/feeds.json", param_dict)

def get_thingspeak_field_feed(channel_id, field_id, read_api_key, number_of_results):
    #Send an HTTP request to view channel field feed data
    #https://ch.mathworks.com/help/thingspeak/get-channel-field-feed.html
    param_dict = {"api_key" : read_api_key, "results" : number_of_results, "timezone" : "Europe/Berlin"}
    return thingspeak_get_request("channels/" + str(channel_id)  + "/fields/" + str(field_id) + ".json", param_dict)

def thingspeak_get_request(endpoint, param_dict):
    #performs a GET request on the given URL with the params in URL-encoded form
    #returns response payload or False if the response was not positive 
    url = "https://api.thingspeak.com/" + endpoint + "?" + urllib.urlencode(param_dict)
    trace("GET: " + url, INFO)
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        data = response.read()
        trace("Response: " + data, INFO)
        return data
    except urllib2.URLError as e:
        trace("Negative response from Thingspeak: " + e.reason, WARN)
    except:
        trace("Connection to Thingspeak failed", ERROR)
        trace(str(sys.exc_info()), WARN)

    return False   

def thingspeak_post_request(endpoint, param_dict):
    #performs a GET request on the given URL with the params in URL-encoded form
    #returns response payload or False if the response was not positive 
    url = "https://api.thingspeak.com/" + endpoint
    trace("POST: " + url + " Params:" + str(param_dict), INFO)
    try:
        request = urllib2.Request(url, urllib.urlencode(param_dict))
        response = urllib2.urlopen(request)
        data = response.read()
        trace("Response: " + data, INFO)
        return data
    except urllib2.URLError as e:
        trace("Negative response from Thingspeak: " + e.reason, WARN)
    except:
        trace("Connection to Thingspeak failed", ERROR)
        trace(str(sys.exc_info()), WARN)

    return False   
