import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'Newyorkcity': 'new_york_city.csv',
              'Washington': 'washington.csv' }
city_list = ['Chicago', 'Newyorkcity', 'Washington']
month_list = ['January', 'Febuary', 'March', 'April', 'May', 'June']
day_list = ['Monday', 'Tuesday', 'Wenesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def get_filters():
    while True:
        try:
            print(" Do you want to know more about the data?\n", "*"*50, "\nplease input a correct answer because the program will repeat itself until inserting a correct answer.","\n", "*"*50)
            city = input("would you like a data of 'Chicago' or 'Newyorkcity' or 'Washington'? ").strip().title()
            print("*" * 50)
            if city in city_list :
                choice = input('Would you like filter by "Month" or "Day" or "both" or "All" to no time filter? ').strip().title()
                print("*" * 50)
                if choice == 'Month':
                    day = "All"
                    month = input("which month? January,Febuary,March,April,May,June? ").strip().title()
                    print("*" * 50)
                    if month in month_list:
                        break
                elif choice == 'Day':
                    month = "All"
                    day=input('which day ? Monday,Tuesday,Wenesday,Thursday,Friday,Saturday,Sunday? ').strip().title()
                    print("*" * 50)
                    if day in day_list:
                        break
                elif choice == 'Both':
                    month = input("which month? January,Febuary,March,April,May,June? ").strip().title()
                    print("*" * 50)
                    day=input("which day ? Monday,Tuesday,Wenesday,Thursday,Friday,Saturday,Sunday? ").strip().title()
                    print("*" * 50)
                    if month in month_list and day in day_list:
                        break
                elif choice == 'All':
                    month = 'All'
                    day = 'All'
                    break
        except UnboundLocalError:
            print('invalid input')
            return get_filters()
    print("*" * 50)
    return city,month,day
# print(get_filters())

def load_data(city):
    df = pd.read_csv(CITY_DATA[city],parse_dates=['Start Time'])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    return df
    
def time_stats(df,month,day):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time() 


    if month == "All" and day == "All":
        print('No Time filter')
        print("the most common month :", df['month'].mode())
        print("the most common day_of_week :", df['day_week'].mode())
        print("the most common hour :", df['hour'].mode())
    elif month != "All" and day == "All":
        print(f'month filter"{month}"')
        print("the most common month is :", month)
        print(f"the most common day_of_week in  :", df[(df['month']==month)]['day_week'].mode())
        print(f"the most common hour :", df[(df['month']==month)]['hour'].mode())
    elif month == "All" and day != "All":
        print(f'day filter"{day}"')
        print("the most common month :", df['month'].mode())
        print("the most common day_of_week :", day)
        print(f"the most common hour :", df[(df['day_week']==day)]['hour'].mode())
    elif month != "All" and day != "All":
        print(f'both filter"{month}, {day}"')
        print("the most common month :", month)
        print("the most common day_of_week :", day)
        print(f"the most common hour :", df[(df['month']== month) & (df['day_week']==day)]['hour'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))


def station_stats(df,month,day):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    if month == "All" and day == "All":
        print('No Time filter')
        print('the most commonly used start station:', df['Start Station'].mode())
        print('the most commonly used end station:', df['End Station'].mode())
    elif month != "All" and day == "All":
        print(f'month filter"{month}"')
        print('the most commonly used start station:', df[(df['month']==month)]['Start Station'].mode())
        print('the most commonly used end station:', df[(df['month']==month)]['End Station'].mode())
    elif month == "All" and day != "All":
       print(f'day filter"{day}"')
       print('the most commonly used start station:', df[(df['day_week']==day)]['Start Station'].mode())
       print('the most commonly used end station:', df[(df['day_week']==day)]['End Station'].mode())
    elif month != "All" and day != "All":
      print(f'both filter"{month}, {day}"')
      print('the most commonly used start station:', df[(df['month']== month) & (df['day_week']==day)]['Start Station'].mode())
      print('the most commonly used end station:', df[(df['month']== month) & (df['day_week']==day)]['End Station'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('-'*40)

def trip_duration_stats(df, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()
    if month == "All" and day == "All":
        print('No Time filter')
        print('total_travel_time : ',df['Trip Duration'].sum(), ' seconds')
        print('mean_travel_time : ',df['Trip Duration'].mean(), ' seconds')

    elif month != "All" and day == "All":
        print(f'month filter"{month}"')
        print('total_travel_time : ',df[(df['month']==month)]['Trip Duration'].sum(), ' seconds')
        print('mean_travel_time : ',df[(df['month']==month)]['Trip Duration'].mean(), ' seconds')
    elif month == "All" and day != "All":
       print(f'day filter"{day}"')
       print('total_travel_time : ',df[(df['day_week']==day)]['Trip Duration'].sum(), ' seconds')
       print('mean_travel_time : ',df[(df['day_week']==day)]['Trip Duration'].mean(), ' seconds')
    elif month != "All" and day != "All":
       print(f'both filter"{month}, {day}"')
       print('total_travel_time : ',df[(df['month']== month) & (df['day_week']==day)]['Trip Duration'].sum(), ' seconds')
       print('mean_travel_time : ',df[(df['month']== month) & (df['day_week']==day)]['Trip Duration'].mean(), ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if month == "All" and day == "All":
        print('No Time filter')
        print("counts_of_user_types: ",'\n', df['User Type'].value_counts())
        if "Gender" in df.columns:
            print("counts_of_gender: ",'\n', df['Gender'].value_counts())
        if 'Birth Year' in df.columns:
            print("earliest_ year_of_birth: ",  df['Birth Year'].min())
            print("most_recent_year_of_birth: ", df['Birth Year'].max())
            print('most_common_year_of_birth: ' , df['Birth Year'].mode())
    elif month != "All" and day == "All":
        print(f'month filter"{month}"')
        print("counts_of_user_types: ",'\n', df[(df['month']==month)]['User Type'].value_counts())
        if "Gender" in df.columns:  
            print("counts_of_gender: ", '\n', df[(df['month']==month)]['Gender'].value_counts())
        if 'Birth Year' in df.columns:
            print("earliest_ year_of_birth: ",  df[(df['month']==month)]['Birth Year'].min())
            print("most_recent_year_of_birth: ", df[(df['month']==month)]['Birth Year'].max())
            print('most_common_year_of_birth: ' , df[(df['month']==month)]['Birth Year'].mode())
    elif month == "All" and day != "All":
        print(f'day filter"{day}"')
        print("counts_of_user_types: ",'\n', df[(df['day_week']==day)]['User Type'].value_counts())
        if "Gender" in df.columns:
            print("counts_of_gender: ", '\n', df[(df['day_week']==day)]['Gender'].value_counts())
        if 'Birth Year' in df.columns:
            print("earliest_ year_of_birth: ",  df[(df['day_week']==day)]['Birth Year'].min())
            print("most_recent_year_of_birth: ", df[(df['day_week']==day)]['Birth Year'].max())
            print('most_common_year_of_birth: ' , df[(df['day_week']==day)]['Birth Year'].mode())
    elif month != "All" and day != "All":
        print(f'both filter"{month}, {day}"')
        print("counts_of_user_types: ",'\n', df[(df['month']== month) & (df['day_week']==day)]['User Type'].value_counts())
        if "Gender" in df.columns:
            print("counts_of_gender: ", '\n',df[(df['month']== month) & (df['day_week']==day)]['Gender'].value_counts())
        if 'Birth Year' in df.columns:
            print("earliest_ year_of_birth: ",  df[(df['month']== month) & (df['day_week']==day)]['Birth Year'].min())
            print("most_recent_year_of_birth: ", df[(df['month']== month) & (df['day_week']==day)]['Birth Year'].max())
            print('most_common_year_of_birth: ' , df[(df['month']== month) & (df['day_week']==day)]['Birth Year'].mode())       

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def selected_row(df):
    a = 0
    while True:
        view_data1 = input( "do you want to see 5 lines of raw data ? Enter Yes or No ").capitalize().strip()
        print(df.iloc[a:(a+5)])
        a+=5
        view_data2 = input( "do you want to see the next 5 lines of raw data ? Enter Yes or No ").capitalize().strip()
        if view_data1 == "No"  or view_data2 == "No" :
            break
    return view_data1, view_data2
print('-'*40)
    

def main():
    while True:
        
        city, month, day = get_filters()
        df = load_data(city)
        time_stats(df, month, day)
        station_stats(df, month, day)
        trip_duration_stats(df, month, day)
        user_stats(df, month, day)
        selected_row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()