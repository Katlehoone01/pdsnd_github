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
    print(' Hello! Lets explore some US bikeshare data!')

     # set the values of 'city', 'month', and 'day' to zero
    city= 0
    month = 0
    day = 0

     # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    input_city = input('Which City\'s Data Would You Like To Explore? Chicago, New York City or Washington? \n')
    city = input_city.lower()   # All variants of the user's input will formated to be case insensetive by converting it into lowercase
    valid_cities = ['chicago','new york city', 'washington'] # A list of valid city names. Will be used to check the validity of the user's input

    """
         While the value recived from the user is not a valid city name i.e. not present in the list of valid citis
         The loop will inform the user thier input is invalidprompt the user to enter a valid city name.
    """
    while city not in valid_cities:
        print("\n{} Is Not A Valid City Name. Please Enter A Valid City Name.".format(city))
        input_city = input('Chicago, New York City or Washington. \n')
        city = input_city.lower()   # All variants of the user's input will formated to be case insensetive by turining it to lowercase
        valid_cities = ['chicago', 'new york city', 'washington']

    """
          User will be propted to specify if they would like to filter their reults by month. if the user's response is 'no'
          the function will return only the city's name.
    """
    get_month = input('\nWould You Like To Filter Your Results By Month? Type \'Yes\' If You Do Or \'No\' If You Do not.  \n')
    month_filter_queue_result = get_month.lower()  # All variants of the user's input will formated to be case insensetive by converting it into lowercase.
    month_filter_queue_test = ['yes','no'] # list of valid responses to the user's input. if either one is true user will filter results by month.



    """
         The while loop will test for a valid 'yes' or 'no' answer to the users input
         and will continue to ask for a valid result until the user's input is in the list of valid responses
    """
    while month_filter_queue_result not in month_filter_queue_test:
        get_month = input('\nWould You Like To Filter Your Results By Month? Type \'Yes\' If You Do Or \'No\' If You Do not.  \n')
        month_filter_queue_result = get_month.lower()  # All variants of the user's input will formated to be case insensetive by converting it into lowercase.


    """
        conditional if statement that will take in user input result. if user's response is 'yes', the user will be
        required to specify the month they would ilked to filter their results. If the response is 'no' the program
        will ask the user if they would like to filter their results by day.

    """
    if month_filter_queue_result == 'yes': # If the user's reponse 'yes' they will proceed to specify the month they wouild like to filter by.
        input_month = input('\nPlease Specify The Month You Would Like To explore. Select Either All Or The Months Between January And June.  \n')
        month = input_month.lower()  # All variants of the user's input will formated to be case insensetive by converting it into lowercase.
        valid_months = ['january','february','march','april','may','june','all'] # list of valid month name responses to the user's input.

        if month != 'all':# if the user does not want to see the data from all months between January and June

            """
               while the response from the user is not a month in the list of valid months. The user will be
               propted to input a valid month until the input is present in the 'valid_months' list or select all.

            """
            while month not in valid_months:
               print("\n{} Is Not A Valid Month For Entry. Please Select A Month Between January And June Or Select All.".format(month))
               input_month = input('Please Select Either All Or The Months Between January And June. \n')
               month = input_month.lower()  # All variants of the user's input will formated to be case insensetive by converting it into lowercase
               valid_months = ['january','february','march','april','may','june','all',0]
               if month == 'all':
                month = 0
            print("\n Let's Explore {} Data For The Month {}".format(city, month))



        elif month == 'all':    # If the user would like to see the data from all months in the data set.
           print("\n Let's Explore {} Data For All Months Between January To June".format(city))
           month = 0
           day = 0

    elif month_filter_queue_result == 'no': # If the user's response is 'no' the program will returd the city's data and ask if the user would like to filter by day.
        month = 0

    day_filter_queue = input('\nWould You Like To Filter Your Results By Day? Type \'Yes\' If You Do Or \'No\' If You Do not.  \n')
    day_filter_queue_result = day_filter_queue.lower()  # All variants of the user's input will formated to be case insensetive by converting it into lowercase
    day_filter_queue_test = ['yes','no']

    """
        The while loop will test for a valid 'yes' or 'no' answer to the users input
        and will continue to ask for a valid result until the user's input is in the list of valid responses.
    """
    while day_filter_queue_result not in day_filter_queue_test:
        day_filter_queue = input('\nWould You Like To Filter Your Results By Day? Type \'Yes\' If You Do Or \'No\' If You Do not.  \n')
        day_filter_queue_result = day_filter_queue.lower()  # All variants of the user's input will formated to be case insensetive by converting it into lowercase


    """
        conditional if statement that will take in user input result. if user's response is 'yes', the user will be
        required to specify the day they would ilke to use to filter their results. If the response is 'no' the program
        will proceed with no further filters.

    """
    if day_filter_queue_result == 'yes': # If the user's reponse 'yes' they will proceed to specify the day they wouild like to filter by.
        input_day = input('\nWhich Day Of The Week Are You Interested In? \n')
        day = input_day.lower()  # All variants of the user's input will formated to be case insensetive by converting it into lowercase
        valid_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

        if day != 'all':
            while day not in valid_days:
                print("\n{} Is Not A Valid Day For Entry. Please Select A Valid Day Or Select All.".format(day))
                input_day = input('Which Day Of The Week Are You Interested In? \n')
                day = input_day.lower()  # All variants of the user's input will formated to be case insensetive by converting it into lowercase
                valid_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all',0]
                print("\n Exploring {} Data For {}".format(city,day))
                if day == 'all':
                    day = 0

            if month == 0:
                print("\n Exploring {} Data For All Months Between January And June, Filtered Further By The Day {}".format(city,day))


        elif day == 'all': # If the user would like to see the data from all day
            print("\n Exploring {} Data With All Days In The Week".format(city))
            day = 0

    elif day_filter_queue_result == 'no': # If the usere's response is 'no' the program will returdn the city's data with with just the month filters.
        print("\n Let Us Explore {} Data...".format(city))
        day = 0

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
    # loading the specified city data into a new pandas dataframe and assign it to the variable 'df'
    df = pd.read_csv(CITY_DATA[city])

    # convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # pull the desired month from the 'Start Time' column and create a new column named 'month'
    df['month'] = df['Start Time'].dt.month
    # pull the desired day from the 'Start Time' column and create a new column named 'day'
    df['day'] = df['Start Time'].dt.weekday_name

    # filter the data by month if a valid month name has been passed and the month name is not 'all'
    if month != 0:
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # dictionary of month names, with the month intager values as the keys
        month_names = {1:'january',2:'february',3:'march',4:'april',5:'may',6:'june'}
        # accessing the name of the specified month from the 'month_name' dictionary using the month int value for refrence
        name_of_month = month_names[month]
        print("Showing {} Data For The Month {}".format(city,name_of_month.title()))

        # filter by the month name passed and create a new dataframe
        df = df[df['month'] == month]

    elif month == 0:
              print("Showing {} Data For All Months Between January and June".format(city))
    if day != 0:
        # filter by the day passed and create a new dataframe
        df = df[df['day'] == day.title()]
        if month == 0:
            month_name = 'all'
            name_of_month = month_name
        # print the specified day
        print("Showing {} Data For The month {} Filtered Further By {} ".format(city,name_of_month,day))

    elif day == 0:
        print("Showing {} Data for All Days In The Week".format(city))

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # pull the desired month from the 'Start Time' column and create a new column named 'month'
    df['Month'] = df['Start Time'].dt.month
    # pull the desired day from the 'Start Time' column and create a new column named 'day'
    df['day'] = df['Start Time'].dt.weekday_name
    # pull the desired hour from the 'Start Time' column and create a new column named 'hour'
    df['hour'] = df['Start Time'].dt.hour


    # calculate the most occuring instance of 'df['month']'
    most_common_month = df['Month'].mode()[0]

    # dictionary of month names, with the most common month intager values as the keys
    month_names = {1:'january',2:'february',3:'march',4:'april',5:'may',6:'june'}
    # accessing the name of the specified month from the 'month_name' dictionary using the most_common_month int value for refrence
    name_of_month = month_names[most_common_month]

    # display the most common month
    print("The Most Common Month is: {}".format(name_of_month.title()) )

    # calculate the most occuring instance of 'df['day']'
    most_common_day = df['day'].mode()[0]
    # display the most common day of week
    print("The Most Common Day For Traveling Is: {}".format(most_common_day))

    # calculate the most occuring instance of 'df['hour']'
    most_common_hour = df['hour'].mode()[0]
    # display the most common start hour
    print("The most popular Start Hour Is: {}".format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # calculate the most occuring instance of 'df['Start Station']'
    most_common_start_station = df['Start Station'].mode()[0]
    # display most commonly used start station
    print("The most commonly used Start Station is:",most_common_start_station)

    # calculate the most occuring instance of 'df['End Station']'
    most_common_end_station = df['End Station'].mode()[0]
    # display most commonly used end station
    print("The most commonly used End Station is:",most_common_end_station)

    # concatenate the columns 'Start Station' and 'End Station' columns and create a new column named 'start_and_end_station'
    df['start_and_end_station'] = df['Start Station'] + " to " + df['End Station']
    # calculate the most occuring instance of 'df['start_and_end_station']'
    frequent_start_end_stations = df['start_and_end_station'].mode()[0]
    # display most frequent combination of start station and end station trip
    print("The most frequent start to end station trip combination is:", frequent_start_end_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration']
    to_minutes = total_travel_time / 60
    print("Total time traveled in minutes:",sum(to_minutes) )

    # display mean travel time
    mean_travel_time = to_minutes.mean()
    print("The avarage time traveled in minutes:", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Subscriber Types Deconstructed")
    print(user_types,'\n')

    """
     Because 'washington' does not have the gender and birth year columns it will be skipped and the gender and birth year statistics
     will be calculated for the relevant cities
    """
    if city != 'washington':
        print("Gender Types Deconstructed")
        # Display counts of gender
        gender_types = df['Gender'].value_counts()
        print(gender_types,'\n')
        print("Birth Years Deconstructed")
        # Display most common year of birth
        mode_birth_year = df['Birth Year'].mode()[0]
        print("The most common year of birth is:",mode_birth_year)
        # Display earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        print("The earliest year of birth is:",earliest_birth_year)
        # Display the most recent year of birth
        most_recent_birth_year = df['Birth Year'].max()
        print("The most recent year of birth is:",most_recent_birth_year)

    else:
        print("No Gender and birth year Statistics available.")




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_rows_of_data(df):

    """" Display some rows of data upon request """

    # ask the user if they would like to view 5 rows of individual trip data.
    view_data = input("Would You Like To View 5 Rows Of Individual Trip Data? Type Yes If You Do And No If You Don't. ")
    view_data_input = view_data.lower()
    valid_data_input_response = ['yes','no']

    # while loop to keep asking the user for a valid response in the event of an invalid response.
    while view_data_input not in valid_data_input_response:
        view_data = input("Would You Like To View 5 Rows Of Individual Trip Data? Type Yes If You Do And No If You Don't. ")
        view_data_input = view_data.lower()
        valid_data_input_response = ['yes','no']


    # a variable 'start_loc' is initialized and set to 0
    start_loc = 0
    # the response from the user is assigned to the variable 'view_display'
    view_display = view_data_input
    # in the event 'view_data_input' is 'yes', 5 lines of data are printed
    if view_data_input == 'yes':
        # while 'view_display' is not no. 5 rows of data will be printed
        while view_display != 'no':
            start_loc += 5
            print(df.iloc[start_loc-5:start_loc])
            view_display = input("Would you like to view more? ").lower
    # in the event 'view_data_input' is 'no', no lines of data are printed
    elif view_data_input == 'no':
        print("Let's continue...")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_rows_of_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
