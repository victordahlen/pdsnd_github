import time
import pandas as pd


#lists of available days and months for the filter inputs
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print(months, days, CITY_DATA)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n Hello! Let\'s explore some US bikeshare data! \n')

    while True:

        city = input('\n Please select the city you want to look at by typing "chicago", "new york city" or "washington": ')
        if city.lower() in CITY_DATA.keys():
            break
        else:
            print('{} is not a valid city!'.format(city))


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\n Please select the month you want to look at by typing month names between "january" and "june" or look at all months by typing "all": ')
        if month.lower() in months:
            break
        elif month.lower() == 'all':
            break
        else:
            print('{} is not a valid month!'.format(month))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\n Please select the day of the week you want to look at by typing the day name betweens "monday" and "sunday" or "all" for all days: ')
        if day.lower() in days:
            break
        elif day.lower() == 'all':
            break
        else:
            print('{} is not a valid day! \n'.format(day))

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        df = df.loc[df['month'] == month.title()]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is {}. \n'.format(df.month.mode()[0]))

    # display the most common day of week
    print('The most common day of week is {}. \n'.format(df.day_of_week.mode()[0]))

    # display the most common start hour
    print('The most common start hour is {}. \n'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(4)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is {}. \n'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most commonly used end station is {}. \n'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station are {}. \n'.format((df['Start Station'] + ' ' + df['End Station']).mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(4)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time is {}. \n'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('The mean travel time is {}. \n'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(4)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Number of different users: \n', df['User Type'].value_counts())

    # Display counts of gender - Try Except for when gender info not available
    try:
        print('Distribution of gender \n', df['Gender'].value_counts())
    except:
        print('There is no gender information for {}. \n'.format(city))

    # Display earliest, most recent, and most common year of birth - Try except for when birth year not available
    try:
        print("""The earliest year of birth is {}. \n
        The most recent year of birth is {}. \n
        The most common year of birth is {}. """.format(df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0]))
    except:
        print('There is no birth year information for {}'.format(city))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Asks user if interested in seeing raw data and displays raw data 5 rows at a time"""
    see_raw_data = input('Do you want to inspect the raw data? Enter "y", otherwise enter another letter/character : ')
    if see_raw_data == 'y':
        i = 0
        while True:
            if i > df.shape[0]:
                print('No more data to show!')
                break

            print(df.iloc[i:i+5])
            i +=5
            next_rows = input('Do you want to inspect the next five rows? Enter y, otherwise type another letter/character : ')
            if next_rows.lower() != 'y':
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
