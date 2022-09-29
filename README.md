# checkPhoneNumber
Simple app in Python, you can check from what country is this phone number

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Result](#result)

## General info
This project is simple app, you can check from what country is phone number and mobile operator. 
	
## Technologies
Project is created with:
* Python 3.10.7
Wroted in Visual Studio Code
Using API from OpenCage
	
## Setup
To run this project, you need instal PIP:
* folium
* phonenumbers

And need API from OpenCage

```
from http import server
import folium
import phonenumbers
from phoneNumber import number
from phonenumbers import geocoder

#Key = " here you must add API key from https://opencagedata.com" 
#Key = ""
```

## Result
In terminal you can see from what country is phone number, who is mobile operator and you can get HTML file with map. Some phone numbers can be from region or city other are general from country. 