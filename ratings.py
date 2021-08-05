"""Restaurant rating lister."""


log_file = open("scores.txt")

restaurant_scores_dictionary = {}

def add_to_dictionary(log_file):

    for line in log_file:
        line = line.rstrip()
        line_split = line.split(':')
        restaurant_names = line_split[0]
        restaurant_ratings = int(line_split[1])
        restaurant_scores_dictionary[restaurant_names] = restaurant_ratings

    return restaurant_scores_dictionary

add_to_dictionary(log_file)

def sorted_and_printed_restaur_ratings(restaurant_scores_dictionary):
    restaurant_ratings_info = sorted(restaurant_scores_dictionary.items())
    #i = 0
    for restaurant, rating in restaurant_ratings_info:
        #restaurant[i] = 
        print(f'{restaurant} is rated at {rating}')
        #i += 1
        #return restaurant[i]
print(sorted_and_printed_restaur_ratings(restaurant_scores_dictionary))"







