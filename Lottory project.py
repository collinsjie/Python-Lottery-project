import random

def menu():
    # Ask player for numbers he or her want to play
    user_numbers = get_player_numbers()
    # Calculate lottery numbers
    lottery_numbers = create_lottery_numbers()

    # print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    #print out the results of the lottery
    print('you match {}. You won ${}!'.format(matched_numbers, 100 ** len(matched_numbers)))

# user can pick 6 numbers
def get_player_numbers():
    number_csv = input('Enter your 6 numbers, separated by commas:')
    # create a set of integer from number_csv
    number_list = number_csv.split(',') #[1,2,3,]
    integer_set = {int(number) for number in number_list}
    return integer_set

# lottery calculated 6 random number (between 0 and 20)
def create_lottery_numbers():
    values = set() # You can't initialise like so:[]
    while len(values) < 6: # range in [0,1,2,3,4,5]
        values.add(random.randint(1,20))
    return values
menu()
    


