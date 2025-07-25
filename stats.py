#Returns number of words in text
def word_count(text):
    words = text.split()
    return len(words)

#Counts the number of occurences of each character in the text
def character_count(text):
    lowercase_text = text.lower() #makes text lower case
    unique_characters = set(lowercase_text) #creates a set of unique characters found in the text
    dictionary = dict.fromkeys(unique_characters) #creates a dictionary with each unique character as a key
    all_characters = list(lowercase_text) #makes a list from the lowercase text
    for key in dictionary: #for every character in the text, replace value in dictionary with count of character in text
        count = 0
        for character in all_characters:
            if character == key:
                count += 1
            dictionary[key] = count
    return dictionary

#To be used by .sort() to sort the items in a list from highest to lowest value
def sort_on(items):
    return items["num"]

#Turns the dictionary into a list of dictionaries sorted from highest to lowest value
def sort_dict(unsorted_dict):
    list = []
    for item in unsorted_dict:
        dictionary = {"char": item, "num": unsorted_dict[item]}
        list.append(dictionary)
        list.sort(reverse=True, key=sort_on)
    return list
