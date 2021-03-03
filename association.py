#######################################Problem1#######################################
# Kitabi Duniya , a famous book store in India, which was established before Independence, 
# the growth of the company was incremental year by year, but due to online selling of books
# and wide spread Internet access its annual growth started to collapse, seeing sharp 
# downfalls, you as a Data Scientist help this heritage book store gain its popularity 
# back and increase footfall of customers and provide ways the business can improve 
# exponentially, apply Association Rule Algorithm, explain the rules, and visualize 
# the graphs for clear understanding of solution.

import pandas as pd
from mlxtend.frequent_patterns import association_rules , apriori
import matplotlib.pyplot as plt

books = pd.read_csv("C:/Users/hp/Desktop/association assi/book.csv")
    
a_books = apriori(books, min_support = 0.075, max_len = 4, use_colnames = True)

a_books.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = a_books.support[0:11], color ='rgbyk')
plt.xticks(list(range(0, 11)), a_books.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(a_books, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

def to_list(i):
    return (sorted(list(i)))


new_rules = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

new_rules = new_rules.apply(sorted)

rules_sets = list(new_rules)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)
#################################Problem 2##########################################
# The Departmental Store, has gathered the data of the products it sells on a 
# Daily basis. Using Association Rules concepts, provide the insights on the 
# rules and the plots.

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

groceries = []
with open("C:/Users/hp/Desktop/association assi/groceries.csv") as f:
    groceries = f.read()

# splitting the data into separate transactions using separator as "\n"
groceries = groceries.split("\n")

groceries_list = []
for i in groceries:
    groceries_list.append(i.split(","))

all_groceries_list = [i for item in groceries_list for i in item]

from collections import Counter # ,OrderedDict

item_frequencies = Counter(all_groceries_list)

# after sorting
item_frequencies = sorted(item_frequencies.items(), key = lambda x:x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))

# barplot of top 10 
import matplotlib.pyplot as plt

plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), items[0:11])
plt.xlabel("items")
plt.ylabel("Count")
plt.show()

# Creating Data Frame for the transactions data
groceries_series = pd.DataFrame(pd.Series(groceries_list))
groceries_series = groceries_series.iloc[:9835, :] # removing the last empty transaction

groceries_series.columns = ["transactions"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name
X = groceries_series['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')

frequent_itemsets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

def to_list(i):
    return (sorted(list(i)))


new_rules = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

new_rules = new_rules.apply(sorted)

rules_sets = list(new_rules)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)
##############################Problem 3#########################################
# A film distribution company wants to target audience based on their likes and 
# dislikes, you as a Chief Data Scientist Analyze the data and come up with different 
# rules of movie list so that the business objective is achieved.

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

my_movies = pd.read_csv("C:/Users/hp/Desktop/association assi/my_movies.csv")
my_movies = my_movies.iloc[:,5:]


a_movies = apriori(my_movies, min_support = 0.002 , max_len = 4, use_colnames = True)


# Most Frequent item sets based on support 
a_movies.sort_values('support', ascending = False, inplace = True)


plt.bar(x = list(range(0, 11)), height = a_movies.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), a_movies.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(a_movies, metric = "lift", min_threshold = 1)

rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

def to_list(i):
    return (sorted(list(i)))


new_rules = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

new_rules = new_rules.apply(sorted)

rules_sets = list(new_rules)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)


##########################################Problem 4###############################
# A Mobile Phone manufacturing company wants to launch its three brand new phone into 
# the market, but before going with its traditional marketing approach this time it want 
# to analyze the data of its previous model sales in different regions and you have been 
# hired as an Data Scientist to help them out, use the Association rules concept and provide
# your insights to the company’s marketing team to improve its sales.

import pandas as pd
from mlxtend.frequent_patterns import apriori , association_rules
import matplotlib.pyplot as plt
my_phone = pd.read_csv("C:/Users/hp/Desktop/association assi/myphonedata.csv")
my_phone = my_phone.iloc[:,3:]

a_phone = apriori(my_phone , min_support = 0.02 , max_len = 4 , use_colnames = True)


# Most Frequent item sets based on support 
a_phone.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = a_phone.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), a_phone.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(a_phone, metric = "lift", min_threshold = 1)

rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

def to_list(i):
    return (sorted(list(i)))


new_rules = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

new_rules = new_rules.apply(sorted)

rules_sets = list(new_rules)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)

##########################Problem 5######################################################
# A retail store in India, has its transaction data, and it would like to know the 
# buying pattern of the consumers in its locality, you have been assigned this task 
# to provide the manager with rules on how the placement of products needs to be there 
# in shelves so that it can improve the buying patterns of consumes and increase customer 
# footfall.

import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import association_rules,apriori

retails = []
with open("C:/Users/hp/Desktop/association assi/transactions_retail1.csv") as f:
    retails = f.read()

retails = retails.split("\n")

retails = retails[:100]

retails_list = []
for i in retails:
    retails_list.append(i.split(","))


all_retails_list = [i for item in retails_list for i in item]

new_all_retails_list =[]
for i in all_retails_list:
    if i != "NA":
        new_all_retails_list.append(i)
        
from collections import Counter # ,OrderedDict 

item_frequencies = Counter(new_all_retails_list)

# after sorting
item_frequencies = sorted(item_frequencies.items(), key = lambda x:x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))

# barplot of top 10 
plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), items[0:11])
plt.xlabel("items")
plt.ylabel("Count")
plt.show()

# Creating Data Frame for the transactions data
retail_series = pd.DataFrame(pd.Series(retails_list))

retail_series.columns = ["transactions"]

X = retail_series['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')
X = X.drop(['NA'] , axis =1)

frequent_itemsets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

def to_list(i):
    return (sorted(list(i)))

new_rules = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

new_rules = new_rules.apply(sorted)

rules_sets = list(new_rules)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)

################################END#####################################################




        
