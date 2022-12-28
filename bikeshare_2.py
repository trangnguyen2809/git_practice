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


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). 

    # get user input for month (all, january, february, ... , june
    
    # get user input for day of week (all, monday, tuesday, ... sunday

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
    #load intended file into data frame
    df = pd.read_csv('{}.csv'.format(city))
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum() / 3600.0
    print("total travel time in hours is: ", total_duration)

    # display mean travel time
    mean_duration = df['Trip Duration'].mean() / 3600.0
    print("mean travel time in hours is: ", mean_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('press enter to see row data, press no to skip')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
