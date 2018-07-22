#!/usr/bin/env python3

import requests
import logging
import argparse

from datetime import datetime

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logging.disable(logging.CRITICAL)
api_key = 'c9b6e9cab9b6296293bd91b942f36be0'
end_point = 'https://api.openweathermap.org/data/2.5'


def get_current_weather(city, country, units='imperial'):
    raw_data = requests.get(f'{end_point}/forecast?', params={'q': f'{city},'
        + country, 'appid': api_key, 'units': units})
    raw_data.raise_for_status()
    return raw_data.json()['list'][0]


def get_forecast(city, country, units='imperial'):
    raw_data = requests.get(f'{end_point}/forecast?', params={'q': f'{city},'
        + country, 'appid': api_key, 'units': units})
    raw_data.raise_for_status
    data = raw_data.json()

    return [data['list'][8], data['list'][16], data['list'][24]]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('city', help='The name or zip code of the city to search.'
        + ' For smaller municipalies, openweathermap api returns data for the nearest'
        + ' major city.')
    parser.add_argument('country', help='Country code for the desired city.')
    parser.add_argument('-u', '--units', choices=['imperial', 'metric', 'kelvin'],
        default='imperial', help='Optional specification of units.')
    parser.add_argument('-f', '--forecast', action='store_const', 
        const=get_forecast, help='Optionally display three day weather forecast for city.')
    args = parser.parse_args()

    units = {'metric': u'\u00B0C', 'imperial': '\u00B0F', 'kelvin': 'K', None: u'\u00B0F'}
    logging.debug(args.units)
    
    weather = get_current_weather(args.city, args.country, units=args.units)
    logging.debug(weather)
    print(f'Current weather in {args.city}, {args.country}: ' 
        + weather['weather'][0]['main'])
    print(f'Temperature: {weather["main"]["temp"]}{units[args.units]}\n')

    if args.forecast:
        logging.debug(f'Getting weather forecast for {args.city}, {args.country}')
        forecast = args.forecast(args.city, args.country, args.units)
        logging.debug(forecast)

        print('Here is your three day forecast:\n')
        for i in range(len(forecast)):
            date = datetime.fromtimestamp(forecast[i]['dt'])
            logging.debug(forecast[i]['dt'])
            logging.debug(date)

            print(f'{date.month}/{date.day}/{date.year}\nWeather: {forecast[i]["weather"][0]["main"]}'
                + f'\nTemperature: {forecast[i]["main"]["temp"]}{units[args.units]}\n')
