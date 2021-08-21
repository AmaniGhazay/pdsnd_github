import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = input('What city would you like to look at? ').lower()
    while city not in CITY_DATA:
        city = input("Please enter a valid city: ").lower()
    # get user input for month (all, january, february, ... , june)
   
    month = input('Please choose all or one month from this months January, February, March, April, May or June: ').lower()
    while month not in MONTH_DATA:
        month = input("Please enter a valid month: ").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please choose all or one day from this days Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday: ').lower()
    while day not in DAY_DATA:
        day = input("Please enter a valid day: ").lower()

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

   

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    common_month=df['month'].mode()[0]
    print('MOst common month :',common_month)

    # TO DO: display the most common day of week
    df['day']=df['Start Time'].dt.day
    common_day=df['day'].mode()[0]
    print('Most common day:',common_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('Most common start hour:',common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    

    
    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('Most common Start station:',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('Most common end station:',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_trip=(df['Start Station'] + "||" + df['End Station']).mode()[0]
    print('Most common trip:',common_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time:',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time:',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df:
      
       print("The count of user gender from the given fitered data is:" ,df['Gender'].value_counts()) 
        
    # TO DO: Display earliest, most recent, and most common year of birth     
    if 'Birth Year' in df:
       earliest_birth=int(df['Birth Year'].min())
       recent_birth=int(df['Birth Year'].max())
       common_birth=int(df['Birth Year'].mode()[0])
       print('Earlist Birth:',earliest_birth)
       print('Recent Birth:',recent_birth)
       print('Common year of birth:',common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n').lower()
        
        while True:
           
                if view_raw_data != 'yes':
                   break
                
                display_raw_data(df)
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
