import time
import pandas as pd
import numpy as np

data_of_cities = { 'chicago': 'chicago.csv',
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
    print('Hi there! Wanna explore some US bikeshare data!')
    # get user input for city (Chicago, New York city, or Washington). HINT: Use a while loop to handle invalid inputs
    city = input("which city do you want to display it\'s data? Chicago, New York city, or Washington?").lower()
    while city not in (["chicago","new york city","washington"]):
        print("sorry, you provided invalid city name.  your input should be: 'chicago' or 'new york city' or 'washington' ")


    time_filter = input("Do you want to filter the data by month, day, both or none?").lower()
    while time_filter not in (["month", "day", "both", "none"]) :
        print ("sorry, your input should be: 'month' or 'day' or 'both' or 'none'")

    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    if time_filter == 'month' or time_filter == 'both':
        month = input("For Which month do you want the data? ('January', 'February', 'March', 'April', 'May', 'June', or 'all')? ").lower()
        while month not in (['january', 'february', 'march', 'april', 'may', 'june','all']):
            print("sorry,You provided invalid month. your input should be: 'January' or 'February' or 'March' or 'April' or 'May' or 'June' or 'all' ")      
    else:
        month = 'all'


    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','all']
    if time_filter == 'day' or time_filter == 'both':
        day = input("For Which day do you want the data?  ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all'? ").lower()
        while day not in(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','all']):
                print("sorry,You provided invalid day. yor input should be:'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday' or 'Sunday' or 'all' ")
    else:
        day = 'all'

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

    df = pd.read_csv(data_of_cities(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
        """Displays statistics on the most frequent times of travel."""
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        most_common_month = df['month'].mode()[0]
        print(f'The most common month is: {months[most_common_month-1]}')
        most_common_day = df['day_of_week'].mode()[0]
        print(f'The most common day of week is: {most_common_day}')
        df['hour'] = df['Start Time'].dt.hour
        most_common_start_hour = df['hour'].mode()[0]
        print(f'The most common start hour is: {most_common_start_hour}')
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    # display the most common month


    # display the most common day of week


    # display the most common start hour



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]

    print('The most commonly used start Station:', most_start_station)

    # display most commonly used end station
    most_end_station = df['End Station'].mode()[0]

    print('the most commonly used end Station:', most_end_station)

    # display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    most_common_trip = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', most_common_trip)
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        print("\n")
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)
        print("\n")
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        print("\n")
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        print("\n")
    else: print("opps, There is no available data.")
        

    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
