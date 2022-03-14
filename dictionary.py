import csv

with open('dictionary.csv', 'r') as csv_file:
    
    csv_reader = csv.reader(csv_file)

    search_word = input("Enter word to search: ")
    
    for line in csv_reader:
        
        if search_word in line:
            
            print(search_word)

            print(line)

        else:
            print("Not found")
        
        
