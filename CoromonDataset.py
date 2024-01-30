# Final Portfolio Project - Sahand Namvar
import random

file_path = "CoromonDataset.txt";

# Read data from file and return list of string elements (lines)
with open(file_path, "r") as file:
    data = file.readlines();
 
# Extract headers and remove '\n' character
header = data[0].strip().split(",");

# Remove header from data
coromon_data = data[1:];

# Count the number of Coromons
def coromon_count(coromon_list):
    print("\n--- Number of Coromons ---");
    print(f"Total Count: {len(coromon_list)}");

# Select a random Coromon and display its information
def coromon_random(coromon_list):
    random_choice = random.choice(coromon_list);
    # return a dictionary using 'zip()' to pair each element of the header list with the corresponding element from the 'random_choice' string element (stripped & splitted).
    random_choice_info = dict(zip(header, random_choice.strip().split(",")));
    print("\n--- Random Coromon Information ---");
    for k, v in random_choice_info.items():
        print(f"{k}: {v}");

# Find different types of Coromons (unique types)
def coromon_type(coromon_list):
    unique_types = [];
    for coromon in coromon_list: # Go through each element of the list (each element is a string, i.e. a line of csv file)
        coromon_info = coromon.strip().split(","); # return that string element in a form of comma seperated list with white spaces removed
        if coromon_info[1] not in unique_types:
            unique_types.append(coromon_info[1]);
    print("\n--- Different Types of Coromons ---");
    for t in unique_types:
        print(t);

# Calculate average values of properties for each common type of Coromon accross all those that belong to that common type
def Type_average_properties(coromon_list, display=False):
    # Create empty dictionaries to store sums and counts for each property for each type of Coromon
    type_sum = {};          # Visualize --> type_sum = {"Ice": {"Health Points": 90}, {}, {}, {}, {}, {}}
    type_counter = {}       # Visualize --> type_counter = {"Ice": {"Health Points": 1}, {}, {}, {}, {}, {}}
    
    for coromon in coromon_list:
        coromon_info = coromon.strip().split(",");
        coromon_info_type = coromon_info[1]; #Type at index 1

        # For each Coromon type, initialize sum and counter dictionaries
        if coromon_info_type not in type_sum:
            type_sum[coromon_info_type] = {};
            type_counter[coromon_info_type] = {};

            # Iterate over each header (start from 3rd element) and add it as a key within each Coromon type's dictionary
            for i, property_names in enumerate(header[2:], start=2): # Starting from index 2 for properties
                type_sum[coromon_info_type][property_names] = 0;
                type_counter[coromon_info_type][property_names] = 0;
        
        # Update sums and counts for each property for each type of Coromon
        for j, property_value in enumerate(coromon_info[2:], start=2):
            property_name = header[j];
            type_sum[coromon_info_type][property_name] += int(property_value);
            type_counter[coromon_info_type][property_name] += 1;
    
    # Calculate average values for each property for each type of Coromon (same logic)
    type_property_average = {};
    for coromon_type, coromon_type_values in type_sum.items():
        type_property_average[coromon_type] = {};
        for property_name, property_value_sum in coromon_type_values.items():
            total_count = type_counter[coromon_type][property_name];
            type_property_average[coromon_type][property_name] = round((property_value_sum / total_count), 3) if total_count > 0 else 0;

    # Because this function returns an object AND contains print statements, everytime the function is called, the print statements are executed. To avoid this, we manually switch when to print.
    if display == True:
        # Display each Property Average for each Coromon type
        print("\n--- Average Values for Each Property for Each Coromon Type ---");
        for coromon_type, coromon_type_values in type_property_average.items():
            print(f"\nType: {coromon_type}");
            for property_name, property_average in coromon_type_values.items():
                print(f"{property_name}:{property_average}");
    
    return type_property_average # for use in the next functions

Type_average_properties_list = Type_average_properties(coromon_data, False)

# Find Coromon type with the HIGHEST & LOWEST average Health Points
def highest_lowest_avg_hp():
    # Store each Coromon type and its corresponding average HP value as a key/value pair {"Coromon Type" : Avg HP Value}
    HP_data = {};
    for coromon_type, coromon_type_values in Type_average_properties_list.items():
        hp = coromon_type_values["Health Points"];
        HP_data[coromon_type] = hp;
    
    # Find Max & Min Values
    avg_hp = list(HP_data.values()); # Create a new list and populate it with values from HP_data
    
    max_value = 0;
    min_value = 0;
    if avg_hp: # Check if avg_hp has elements before assignment
        max_value = max(avg_hp);
        min_value = min(avg_hp);

    # Find Max & Min Keys (types)
    max_key = None;
    min_key = None;
    for k, v in HP_data.items():
        if v == max_value:
            max_key = k;
        elif v == min_value:
            min_key = k;

    print("\n--- Coromon with Highest Average Health Points ---");
    print(f"Type: {max_key}");
    print(f"Health Point: {max_value}");

    print("\n--- Coromon with Lowest Average Health Points ---");
    print(f"Type: {min_key}");
    print(f"Health Point: {min_value}");

# Find Coromon type with the HIGHEST & LOWEST average Attack points
def highest_lowest_avg_attack():
    # Store each Coromon type and its corresponding average Attack value as a key/value pair {"Coromon Type" : Avg Attack Value}
    attack_data = {};
    for coromon_type, coromon_type_values in Type_average_properties_list.items():
        attack = coromon_type_values["Attack"];
        attack_data[coromon_type] = attack;
    
    # Find Max & Min Values
    avg_attack = list(attack_data.values()); # Create a new list and populate it with values from attack_data
    
    max_value = 0;
    min_value = 0;
    if avg_attack: # Check if avg_attack has elements before assignment
        max_value = max(avg_attack);
        min_value = min(avg_attack);

    # Find Max & Min Keys (types)
    max_key = None;
    min_key = None;
    for k, v in attack_data.items():
        if v == max_value:
            max_key = k;
        elif v == min_value:
            min_key = k;

    print("\n--- Coromon with Highest Average Attack Points ---");
    print(f"Type: {max_key}");
    print(f"Attack Point: {max_value}");

    print("\n--- Coromon with Lowest Average Attack Points ---");
    print(f"Type: {min_key}");
    print(f"Attack Point: {min_value}");

# Find Coromon type with the HIGHEST & LOWEST average Special Attack points
def highest_lowest_avg_special_attack():
    # Store each Coromon type and its corresponding average Special Attack value as a key/value pair {"Coromon Type" : Avg Special Attack Value}
    SPattack_data = {};
    for coromon_type, coromon_type_values in Type_average_properties_list.items():
        SPattack = coromon_type_values["Special Attack"];
        SPattack_data[coromon_type] = SPattack;
    
    # Find Max & Min Values
    avg_SPattack = list(SPattack_data.values()); # Create a new list and populate it with values from SPattack_data
    
    max_value = 0;
    min_value = 0;
    if avg_SPattack: # Check if avg_SPattack has elements before assignment
        max_value = max(avg_SPattack);
        min_value = min(avg_SPattack);

    # Find Max & Min Keys (types)
    max_key = None;
    min_key = None;
    for k, v in SPattack_data.items():
        if v == max_value:
            max_key = k;
        elif v == min_value:
            min_key = k;

    print("\n--- Coromon with Highest Average Special Attack Points ---");
    print(f"Type: {max_key}");
    print(f"Special Attack Point: {max_value}");

    print("\n--- Coromon with Lowest Average Special Attack Points ---");
    print(f"Type: {min_key}");
    print(f"Special Attack Point: {min_value}");

# Find Coromon type with the HIGHEST & LOWEST average Defense points
def highest_lowest_avg_defense():
    # Store each Coromon type and its corresponding average Defense value as a key/value pair {"Coromon Type" : Avg Defense Value}
    defense_data = {};
    for coromon_type, coromon_type_values in Type_average_properties_list.items():
        defense = coromon_type_values["Defense"];
        defense_data[coromon_type] = defense;
    
    # Find Max & Min Values
    avg_defense = list(defense_data.values()); # Create a new list and populate it with values from defense_data
    
    max_value = 0;
    min_value = 0;
    if avg_defense: # Check if avg_defense has elements before assignment
        max_value = max(avg_defense);
        min_value = min(avg_defense);

    # Find Max & Min Keys (types)
    max_key = None;
    min_key = None;
    for k, v in defense_data.items():
        if v == max_value:
            max_key = k;
        elif v == min_value:
            min_key = k;
    
    print("\n--- Coromon with Highest Average Defense Points ---");
    print(f"Type: {max_key}");
    print(f"Defense Point: {max_value}");

    print("\n--- Coromon with Lowest Average Defense Points ---");
    print(f"Type: {min_key}");
    print(f"Defense Point: {min_value}");

# Find Coromon type with the HIGHEST & LOWEST average Special Defense points
def highest_lowest_avg_special_defense():
    # Store each Coromon type and its corresponding average Special Defense value as a key/value pair {"Coromon Type" : Avg Special Defense Value}
    SPdefense_data = {};
    for coromon_type, coromon_type_values in Type_average_properties_list.items():
        SPdefense = coromon_type_values["Special Defense"];
        SPdefense_data[coromon_type] = SPdefense;
    
    # Find Max & Min Values
    avg_SPdefense = list(SPdefense_data.values()); # Create a new list and populate it with values from SPdefense_data
    
    max_value = 0;
    min_value = 0;
    if avg_SPdefense: # Check if avg_SPdefense has elements before assignment
        max_value = max(avg_SPdefense);
        min_value = min(avg_SPdefense);

    # Find Max & Min Keys (types)
    max_key = None;
    min_key = None;
    for k, v in SPdefense_data.items():
        if v == max_value:
            max_key = k;
        elif v == min_value:
            min_key = k;

    print("\n--- Coromon with Highest Average Special Defense Points ---");
    print(f"Type: {max_key}");
    print(f"Special Defense Point: {max_value}");

    print("\n--- Coromon with Lowest Average Special Defense Points ---");
    print(f"Type: {min_key}");
    print(f"Special Defense Point: {min_value}");

# Find Coromon type with the HIGHEST & LOWEST average Speed Points
def highest_lowest_avg_speed():
    # Store each Coromon type and its corresponding average Speed value as a key/value pair {"Coromon Type" : Avg Speed Value}
    speed_data = {};
    for coromon_type, coromon_type_values in Type_average_properties_list.items():
        speed = coromon_type_values["Speed"];
        speed_data[coromon_type] = speed;
    
    # Find Max & Min Values
    avg_speed = list(speed_data.values()); # Create a new list and populate it with values from speed_data
    
    max_value = 0;
    min_value = 0;
    if avg_speed: # Check if avg_speed has elements before assignment
        max_value = max(avg_speed);
        min_value = min(avg_speed);

    # Find Max & Min Keys (types)
    max_key = None;
    min_key = None;
    for k, v in speed_data.items():
        if v == max_value:
            max_key = k;
        elif v == min_value:
            min_key = k;

    print("\n--- Coromon with Highest Average Speed Points ---");
    print(f"Type: {max_key}");
    print(f"Speed Point: {max_value}");

    print("\n--- Coromon with Lowest Average Speed Points ---");
    print(f"Type: {min_key}");
    print(f"Speed Point: {min_value}");

# Main Menu
def main_menu():
    run = True;
    print("\n\t\t>>> Coromon Menu Option <<<");
    while run:
        print("\n 1. Display Total Number of Coromons.");
        print(" 2. Select a Random Coromon and Display its Information.");
        print(" 3. Find Different Types of Coromons (Unique Types).");
        print(" 4. Calculate Average Values of Properties for Each Common Type of Coromon Accross All Those that Belong to that Common Type.");
        print(" 5. Display Coromon Type with the HIGHEST & LOWEST Average Health Points.");
        print(" 6. Display Coromon Type with the HIGHEST & LOWEST Average Attack Points.");
        print(" 7. Display Coromon Type with the HIGHEST & LOWEST Average Special Attack Points.");
        print(" 8. Display Coromon Type with the HIGHEST & LOWEST Average Defense Points.");
        print(" 9. Display Coromon Type with the HIGHEST & LOWEST Average Special Defense points.");
        print("10. Display Coromon Type with the HIGHEST & LOWEST Average Speed Points.");
        print(" 0. Exit.");
        user_option = input("Your Input: ");
        if user_option == "0":
            run = False;
            print("\nThank You! Program Exited.");
            break;
        elif user_option == "1":
            coromon_count(coromon_data);
        elif user_option == "2":
            coromon_random(coromon_data);
        elif user_option == "3":
            coromon_type(coromon_data);
        elif user_option == "4":
            Type_average_properties_display1 = Type_average_properties(coromon_data, True); 
        elif user_option == "5":
            highest_lowest_avg_hp();  
        elif user_option == "6":
            highest_lowest_avg_attack();
        elif user_option == "7":
            highest_lowest_avg_special_attack();
        elif user_option == "8":
            highest_lowest_avg_defense();
        elif user_option == "9":
            highest_lowest_avg_special_defense();
        elif user_option == "10":
            highest_lowest_avg_speed();
        else:
            print("\nInvalid Selection.");


# Main Program
runMain = True;
while runMain:
    print("\n\t\t>>> Main Menu <<<\n");
    print("Press 1 to Display a Comprehensive Analysis Summary ->   [All-in-One View]");
    print("Press 2 to Access the Coromon Menu Options -> [Select Information to View]");
    print("Press 0 to Exit.");
    user_input = input("Your Input: ");
    if user_input == "0":
        runMain = False;
        print("\nThank You! Program Exited.");
        break;
    elif user_input == "1":
        coromon_count(coromon_data);
        coromon_random(coromon_data);
        coromon_type(coromon_data);
        Type_average_properties_display2 = Type_average_properties(coromon_data, True);        
        highest_lowest_avg_hp();    
        highest_lowest_avg_attack();
        highest_lowest_avg_special_attack();    
        highest_lowest_avg_defense();    
        highest_lowest_avg_special_defense();
        highest_lowest_avg_speed();
    elif user_input == "2":
        main_menu();
        runMain = False;
        break;
    else:
        print("\nInvalid Selection.");

# Close File
file.close();