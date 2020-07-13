import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Welcome to Omer\'s portal. Let\'s explore some US bikeshare data for three beautiful cities!\n\n')
    print('Hello! Welcome to Omer\'s portal. Let\'s explore some US bikeshare data!\n\n')
    print('Hello! Welcome to Omer\'s portal. Let\'s explore some US bikeshare data!\n\n')
    while True:        
        selected_city = input("Please choose one of the following beautiful cities for exploring Bikeshare data:\nNew York City, Chicago or Washington?\n").title()
        if selected_city not in CITY_DATA:
            #shows warning message for invalid input
            print("Ops,\nPlease enter one of the following offered cities.\nTry again.")
            continue
        else:
            print("\nGreat!! You have selected {}".format(selected_city))
            break
        



    while True:        
        selected_month = input("\nPlease choose one of the following months for exploring Bikeshare data:\n((January, February, March, April, May, June or type 'all' to apply no month filter))\n").title()
        if selected_month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            print("Ops,\nPlease enter one of the following offered months.\nTry again.")            
            continue
      
        else:
            print("\nGreat!! You have selected {}".format(selected_month))
            break



    while True:
        selected_day = input("\nPlease choose a beautiful day for for exploring Bikeshare data:\n((Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' to apply no day filter preference.\n").title()
        if selected_day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print("Ops!!!,\nPlease enter the following offered day of week.\nTry again.")
            continue
      
        else:
            print("\nGreat!! You have selected {}".format(selected_day))
            break


    print('-'*80)
    return selected_city, selected_month, selected_day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # create month and day from Start Time

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if not selected all
    if month != 'All':
        # use the index of the months list to get the corresponding month
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        
        df = df[df['month'] == month]


        # filter by day of week if not selected all
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    top_month = df['month'].mode()[0]
    print('The most common month:', top_month)


    top_day = df['day_of_week'].mode()[0]
    print('The most common day:', top_day)


    df['hour'] = df['Start Time'].dt.hour
    top_hour = df['hour'].mode().values[0]    
    print('The most common start hour:', top_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('The most common start station:', df['Start Station'].mode().values[0])


    print('The most common end station:', df['End Station'].mode().values[0])


    df['Trip'] = 'from '+ df['Start Station'] + ' to ' + df['End Station']
    print('The most frequent trip:', df['Trip'].mode().values[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    #display total time as a day
    total_time = sum(df['Trip Duration'])/86400
    print('Total travel time:', total_time, " days")  



    #display mean travel time as a minute
    mean_time = df['Trip Duration'].mean()/60
    print('Mean travel time:', mean_time, " minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)


    try:
        gender_types = df['Gender'].value_counts()
        print('\nCounts of genders:\n', gender_types)
    except KeyError:
        print('The Gender column does not exist for this City')


    try:
        print("\nThe earliest year of birth:", df['Birth Year'].min())
        print("\nThe most recent year of birth:", df['Birth Year'].max())
        print("\nThe most common year of birth:", df['Birth Year'].mode().values[0])
    except KeyError:
        print('The Birth Year column does not exist for this City')
    
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*80)

def raw_data(df):
    """Demonstration of raw data"""
    user_input = input('Do you want to see raw data?\nEnter y or n\n').title()
    line_number = 0

    while True:
        if user_input.lower() != 'n':
            print(df.iloc[line_number : line_number + 10])
            line_number += 10
            user_input = input('\nDo you want to see more raw data? Enter y or n.\n').title()
        else:
            break    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('See you again..')
            break


if __name__ == "__main__":
	main()
