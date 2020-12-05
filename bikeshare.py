import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
a=1

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! Not to worry. Inputs are not case sensitive, so type away.')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # I consulted with https://www.tutorialspoint.com/python/python_while_loop.htm and Udacity Q&A platform
    while a==1:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city not in cities:
            print('That is not a valid city, please try again.\n')
        else:
           break

    # TO DO: get user input for month (all, january, february, ... , june)
    while a==1:
       month = input('What month would you like to see? Options: All, January, February, March, April, May, June. \n').lower()
       if month not in months:
            print('That is not a valid month. Please try again. \n')
       else:
          break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while a==1:
        day = input('What day would you like to see? Options: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday \n').lower()
        if day not in days:
            print("That is not a valid month. Please try again.\n")
        else:
            break
    print('\n')
    print('-'*60)
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
    # I consulted with class notes and the practice solutions of the Bikeshare module
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
       df = df[df['month'] == month]

    if day != 'all':
       df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating the most frequent times of travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    month = df['Start Time'].dt.month
    day = df['Start Time'].dt.day_name()
    hour = df['Start Time'].dt.hour

    # TO DO: display the most common month
    num_mode_month = df['month'].mode()[0]
    str_num_mode_month=str(num_mode_month)
    datetime_convertor = datetime.datetime.strptime(str_num_mode_month, "%m")
    name_mode_month = datetime_convertor.strftime("%B")
    print('The most common month is', name_mode_month)
    #I consulted https://www.kite.com/python/answers/how-to-convert-between-month-name-and-month-number-in-python, class notes and the practice solutions of the Bikeshare module

    # TO DO: display the most common day of week
    mode_day = df['day'].mode()[0]
    print('The most common day of the week is',mode_day)

    # TO DO: display the most common start hour
    mode_hour = df['hour'].mode()[0]
    format_hour=str(mode_hour)
    print('The most common start hour is {}:00 hours'.format(format_hour))

    # TO DO extra: display the latest start hour of a trip
    max_hour=df['hour'].max()
    format_max_hour=str(max_hour)
    print('The latest start hour for a trip is {}:00 hours'.format(format_max_hour))

    # TO DO extra: display the earliest start hour of a trip
    min_hour=df['hour'].min()
    format_min_hour=str(min_hour)
    print('The earliest start hour for a trip is {}:00 hours'.format(format_min_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    time.sleep(2) #a break of 2 seconds to facilitate reading

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating the most popular stations and trip between stations...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start_station = df['Start Station'].mode()[0]
    print('The most common start station is {}'.format(mode_start_station))

    # TO DO: display most commonly used end station
    mode_end_station = df['End Station'].mode()[0]
    print('The most common end station is {}'.format(mode_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' going towards ' + df['End Station']
    mode_combo = df['Station Combination'].mode()[0]
    print('The most frequent combination of start and end station trip is', mode_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    time.sleep(2) #wait for 2 seconds

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration. All have been reformatted from seconds to minutes or hours """

    print('\nCalculating trip duration data for the particular city, month(s) and day(s) you have selected ...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tratime = df['Trip Duration'].sum()
    total_tratime_hours= total_tratime//3600
    print('The total traveled time is {} hours'.format(total_tratime_hours))

    # TO DO: display mean travel time
    mean_tratime = df['Trip Duration'].mean()
    mean_tratime_mins= mean_tratime//60
    print('The mean traveled time is {} minutes'.format(mean_tratime_mins))

    ## This is extra TO DO: display the longest time per trip for this city, month, day selection
    max_tratime = df['Trip Duration'].max()
    max_tratime_mins = max_tratime//60
    print('The longest trip time is {} minutes'.format(max_tratime_mins))

    ## This is extra TO DO: display the shortest time per trip for this city, month, day selection
    min_tratime = df['Trip Duration'].min()
    print('The shortest trip time is {} seconds'.format(min_tratime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    time.sleep(2) #wait for 2 seconds


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating some user statistics...\n')
    start_time = time.time()
    try:

    # TO DO: Display counts of user types
        user_type = df['User Type'].value_counts()
        print('Number of users by type:\n', user_type)
        print('\n')

    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('Number of users by gender:\n', gender)
        print('\n')
        time.sleep(1) #wait for 1 seconds

    # TO DO: Display earliest, most recent, and most common year of birth. Reformatted to take away the decimal
        oldest = df['Birth Year'].min()
        format_oldest=int(oldest)
        print('The oldest user was born in', format_oldest)
        if format_oldest<1940:
            print('    This user is older than 80 years. Unlikely. We will have to check on that data and clean it up in a future project.')

        youngest = df['Birth Year'].max()
        format_youngest=int(youngest)
        print('The youngest user was born in', format_youngest)
        if format_youngest>2010:
            print('    This user is younger than 10 years. Unlikely. We will have to check on that data and clean it up in a future project.')

        mode_year = df['Birth Year'].mode()
        format_mode_year=int(mode_year)
        print('The year of birth with the most users is', format_mode_year)

    except KeyError:
         print("Unfortunately, we can't give information on gender or age of users for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n').lower()
    start_loc = 0
    if view_data == 'yes':
        while a==1:
          print(df.iloc[start_loc:start_loc+5])
          view_display = input('Do you wish to continue?:').lower()
          if view_display =='yes':
             start_loc += 5
          else:
            print('Ok. Goodbye.\n')
            break
    else:
        print('Ok. Goodbye.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
