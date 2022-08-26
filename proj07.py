##########################################################################
#    Computer Project #7
#    Algorithm
#        5 functions defined.        
#        Main function to call all defined functions wherever needed.
#        Calls function and returns value based on user input.
##########################################################################

import csv
from operator import itemgetter

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy", \
        "Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''

def open_file():
    ''' 
    Tries to open file based on user input and returns file pointer.
    Value: Takes no value.
    Returns: File pointer.
    '''
    file1 = input("Enter a file: ")
    #Appropriate file or else ask for user input again.
    while (file1 != "main_data.csv" and file1 != "small_data.csv" \
           and file1 != "smaller_data.csv" and file1 != "smallest_data.csv"):
        print("File not found. Please try again.")
        file1 = input("Enter a file: ")
    fp = open(file1)
    return fp

def read_file(fp):
    '''
    Opens file and creates lists according to data.
    Value: File Pointer.
    Returns: List of strings, List of list of ints
    '''
    country_names = []
    list_of_regime_lists = []
    political_regime = []
    reader= csv.reader(fp)  #reder object
    next(reader, None)    #skips first line
    for line in reader:
        country = line[1]
        regime = int(line[4])
        if country not in country_names:
            if len(political_regime) != 0:    #ignored empty list
                list_of_regime_lists.append(political_regime)
            political_regime = []
            political_regime.append(regime)
            country_names.append(country)
        else:
            political_regime.append(regime)
    list_of_regime_lists.append(political_regime)
    return country_names, list_of_regime_lists

    
def history_of_country(country,country_names,list_of_regime_lists):
    ''' 
    Finds out the most dominant regime in a country.
    Value: Str, List of str, List of list of ints
    Returns: Str
    '''
    index = country_names.index(country)
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    
    for i in list_of_regime_lists[index]:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        elif i == 2:
            count_2 += 1
        elif i == 3:
            count_3 += 1
    final_list = [count_0, count_1, count_2, count_3]    #making a list
    final_list.sort(reverse= True)  #Decreasng order
    num = final_list[0]    #Highest value
    if num == count_0:
        return REGIME[0] 
    elif num == count_1:
        return REGIME[1]     
    elif num == count_2:
        return REGIME[2]
    elif num == count_3:
        return REGIME[3]

def historical_allies(regime,country_names,list_of_regime_lists):
    ''' 
    Finds countries which are historical allies based on regime.
    Values: Str, List of str, List of list of ints
    Returns: Sorted list of str.
    '''
    closed_autocracy = []
    electoral_autocracy = []
    electoral_democracy = []
    liberal_democray = []
    
    for i in country_names:
        if history_of_country(i, country_names, \
                              list_of_regime_lists) == REGIME[0]:
            closed_autocracy.append(i)
        elif history_of_country(i, country_names,\
                                list_of_regime_lists) == REGIME[1]:
            electoral_autocracy.append(i)
        elif history_of_country(i, country_names,\
                                list_of_regime_lists) == REGIME[2]:
            electoral_democracy.append(i)
        else:
            liberal_democray.append(i)
    
    closed_autocracy.sort()    #sorting all lists
    electoral_autocracy.sort()
    electoral_democracy.sort()
    liberal_democray.sort()
    
    if regime == REGIME[0]:
        return closed_autocracy
    elif regime == REGIME[1]:
        return electoral_autocracy
    elif regime == REGIME[2]:
        return electoral_democracy
    else:
        return liberal_democray
            
    
def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    ''' 
    Finds the top countries with the most coups.
    Values: Int, List of str, List of list of ints
    Returns: Sorted list of tuples.
    '''
    final_list = []
    for i in range(len(country_names)):
        country = country_names[i]
        count = 0
        for j in range(len(list_of_regime_lists[i])-1):
            if list_of_regime_lists[i][j] != list_of_regime_lists[i][j+1]:
                count += 1
        tuple1 = (country, count)    #making a tuple 
        final_list.append(tuple1)    #appending to main list
    ans = sorted(final_list, key = itemgetter(1), reverse = True)
    return ans[:top]    #only top values 
    
def main():
    # by convention "main" doesn't need a docstring
    fp = open_file()
    country_names, list_of_regime_lists = read_file(fp)
    ans = True
    while ans:
        print(MENU)
        option = input("Input an option (Q to quit): ")
        #If user wants to quit
        if option == "Q" or option == "q":
            print("The end.")
            ans = False
            
        elif option == "1":
            val1 = True
            while val1:
                try:
                    country = input("Enter a country: ")
                    val = history_of_country(country,country_names,\
                                             list_of_regime_lists)
                    val1 = False
                except:
                    print("Invalid country. Please try again.")
            if val[0] in "AEIOU":
                print("\nHistorically {} has mostly been an {}"\
                      .format(country, val))
            else:
                print("\nHistorically {} has mostly been a {}".\
                      format(country, val))
                
        elif option == "2":
            val2 = True
            while val2:
                try:
                    regime = input("Enter a regime: ")
                    val5 = True
                    while val5:
                        if regime not in REGIME:
                            print("Invalid regime. Please try again.")
                            regime = input("Enter a regime: ")
                        else:
                            val5 = False
                    val = historical_allies(regime,country_names,\
                                            list_of_regime_lists)
                    val2 = False
                except:
                    print("Invalid regime. Please try again.")
            print("\nHistorically these countries are allies of type:", regime)
            print()
            answer = ""
            for i in val:
                answer += i
                answer += ", "
            print(answer[:-2])    #ignores last comma and space
            
            
        elif option == "3":
            val3 = True
            while val3:
                val4 = True
                top = (input("Enter how many to display: "))
                while val4:
                    try: 
                        top = int(top)
                        val4 = False
                        if top > 0:
                            print("\n{: >25} {: >8}".format("Country",\
                                                            "Changes"))
                            final = top_coup_detat_count(top, country_names,\
                                                         list_of_regime_lists)
                            for value in final:
                                print("{: >25} {: >8}".format(value[0],\
                                                              value[1]))
                                val3 = False
                        else:
                            print("Invalid number. Please try again.")
                    except:
                        print("Invalid number. Please try again.")
                        top = (input("Enter how many to display: "))
        
        else:
            print("Invalid choice. Please try again.")
                    
        

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main() 
