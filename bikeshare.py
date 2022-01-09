
import time
import pandas as pd
import numpy as np

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter City name: ")
    # get user input for month (all, january, february, ... , june)
    city = city.lower()
    while(city not in ['chicago', 'new york city', 'washington']):
        city = input("Enter City name: ")
    month = input("Enter Month name: ")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day name of week: ")
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
    #convert date into pandas datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # fetch month name and day from time
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day'] = df['Start Time'].dt.day_name().str.lower()
    
    #filter the data base on condition
    day = day.lower()
    month = month.lower()
    if(month != 'all') and (day != 'all'):
        df = df.loc[(df['month'] == month ) & (df['day'] == day)]
    elif (month == 'all') and (day != 'all'):
        df = df.loc[df['day'] == day]
    elif (month != 'all') and (day == 'all'):
        df = df.loc[df['month'] == month]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(f"The most common month is {df['month'].value_counts().index[0]}")

    # display the most common day of week
    print(f"The most common day of week is {df['day'].value_counts().index[0]}")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(f"The most common Start hour is {df['hour'].value_counts().index[0]}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(f"The most common used start station is {df['Start Station'].value_counts().index[0]}.")

    # display most commonly used end station
    print(f"The most common used end station is {df['End Station'].value_counts().index[0]}.")

    # display most frequent combination of start station and end station trip
    df['Start_End_Station'] = df['Start Station']+" "+ df['End Station']
    print(f"The most frequent combination of start station and end station trip is {df['Start_End_Station'].value_counts().index[0]}.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f"The total travel time is {df['Trip Duration'].sum()} seconds.")

    # display mean travel time
    print(f"The average travel time is {df['Trip Duration'].mean()} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(pd.DataFrame(df['User Type'].value_counts().rename('Count')))

    # Display counts of gender
    print(pd.DataFrame(df['Gender'].value_counts().rename('Count')))

    # Display earliest, most recent, and most common year of birth
    print(f"Earliest year of birth is {int(df['Birth Year'].min())}")
    print(f"Most Recent year of birth is {int(df['Birth Year'].max())}")
    print(f"Most Common year of birth is {int(df['Birth Year'].value_counts().index[0])}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input("\n Would you like to view 5 rows of individual trip data? Enter yes or no \n")
    start_loc = 0
    while (view_data.lower() == 'yes'):
        print(df.iloc[0:start_loc+5])
        start_loc +=5
        view_data = input("\n Do you wish to continue? Enter yes or no \n")
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        else:
            print('washington has no user data.')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
