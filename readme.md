# Home Display

Display data pulled from thingspeak to a cberry monitor.

## Getting Started

You will need a thingspeak account. 
Add the read keys and field id's to the config in the display.config


### Prerequisites

You will need a rasperry pi with a cberry display.


### Installing

- clone the repository.
- change to the home_display direcory
- start with: sudo python display.py > display.log &


To have it start when the raspberry is powered on, create a script home_display.sh with the following content in /etc/init.d (do this as user root, with: sudo nano home_display.sh):
 
 ...
 #! /bin/sh
 cd [source directory]/home_display
 python display-py > display.log
 ...
 
make the script executable with: sudo chmod 755 home_display.sh
add this script to the start with:  sudo update-rc.d home_display.sh defaults
 
You can add this in a script in /et6c/init.d 

## Running the tests

There are currently no tests :P


## Deployment

Clone and run...

## Built With


## Contributing


## Versioning


## Authors

* **Andreas Hosbach** - [AndreasHosbach](https://github.com/AndreasHosbach)

See also the list of [contributors](https://github.com/AndreasHosbach/home_display/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who wrote tutorials about raspberry pi.
