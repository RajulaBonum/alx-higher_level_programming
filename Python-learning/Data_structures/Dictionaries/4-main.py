#!/usr/bin/python3
best_dict = __import__('4-best_dict').best_dict

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_dict(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_dict(None)
print("Best score: {}".format(best_key))
