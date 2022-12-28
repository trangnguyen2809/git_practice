'''
    File name: test.py
    Author: Adel Abu Hashim
    Date created: 3/10/2020
    Date last modified: 3/18/2020
    Python Version: 3.6
'''

import time
import pandas as pd
import numpy as np
from tabulate import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


MONTH_DATA = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'all': -1
}


DAY_DATA = {
    'monday': 'MONDAY',
    'tuesday': 'TUESDAY',
    'wednesday': 'WEDNESDAY',
    'thursday': 'THURSDAY',
    'friday': 'FRIDAY',
    'saturday': 'SATURDAY',
    'sunday': 'SUNDAY',
    'all': 'ALL'
}


def verify_value(datas, message):
    while True:
        value = str(input(message)).lower()
        if value not in datas:
            print("Invalid input! Please try again!")
            continue
        print("Your choice is: {}".format(value))
        return value


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = CITY_DATA.keys()
    message = 'Please choose a city in (chicago, new york city, washington):'
    city = verify_value(cities, message)

    # TO DO: get user input for month (all, january, february, ... , june)
    months = MONTH_DATA.keys()
    message = 'Please choose a month in (all, january, ... , june):'
    month = verify_value(months, message)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = DAY_DATA.keys()
    message = 'Please choose a day in (all, monday, ... sunday):'
    day = verify_value(days, message)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df["Start Time"].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = MONTH_DATA[month]
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df["Start Time"].dt.weekday_name == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print(f'Most common month is: {most_common_month}')

    # TO DO: display the most common day of week
    most_common_day_of_week = df['weekday'].value_counts().idxmax()
    print(f'Most common day of week is: {most_common_day_of_week}')

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print(f'Most common start hour is: {most_common_start_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print(f'Most common start station is: {most_common_start_station}')

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print(f'Most common end station is: {most_common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_trip = df[['Start Station', 'End Station']].agg(' - '.join, axis=1).value_counts().idxmax()
    print(f'Most frequent combination of start station and end station trip is: {most_frequent_trip}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f'Total travel_time: {total_travel_time}')

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print(f'Mean travel_time: {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print(f'Counts of user types: {count_user_types}')

    # TO DO: Display counts of gender
    try:
        count_user_gender = df['Gender'].value_counts()
        print(f'Counts of user gender: {count_user_gender}')
    except KeyError:
        print("Don't exist [Gender] column!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print(f'\nEarliest year of birth is: {earliest_year_of_birth}')
        most_recent_year_of_birth = int(df['Birth Year'].max())
        print(f'Most recent year of birth is: {most_recent_year_of_birth}')
        most_common_year_of_birth = int(df['Birth Year'].value_counts().idxmax())
        print(f'Most common year of birth is: {most_common_year_of_birth}')
    except:
        print("Don't exist [Birth Year] column!")   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # Show 5 raw data
        # I'm refer to here: https://knowledge.udacity.com/questions/26261
        i = 0
        while True:
            raw_data = input('\nWould you see 5 raw data? Please enter yes or no.\n')
            if raw_data.lower() != 'yes':
                break
            print(tabulate(df.iloc[np.arange(0+i,5+i)], headers ="keys"))
            i+=5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
