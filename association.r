#########################################problem 1############################################
# Kitabi Duniya , a famous book store in India, which was established before Independence, 
# the growth of the company was incremental year by year, but due to online selling of books
# and wide spread Internet access its annual growth started to collapse, seeing sharp 
# downfalls, you as a Data Scientist help this heritage book store gain its popularity 
# back and increase footfall of customers and provide ways the business can improve 
# exponentially, apply Association Rule Algorithm, explain the rules, and visualize 
# the graphs for clear understanding of solution.
install.packages("readr")
library(readr)
book <- read.csv("C:\\Users\\hp\\Desktop\\association assi\\book.csv" ,colClasses = "factor")
# loading the Data
summary(book)


install.packages("arules")# Used for building association rules i.e. apriori algorithm
library(arules)
# making rules using apriori algorithm 
# Keep changing support and confidence values to obtain different rules

# Building rules using apriori algorithm
arules_book <- apriori(book , parameter = list(minlen =2 , maxlen =3 , supp =0.7))
summary(arules_book)
# to view we use inspect 
inspect(arules_book)

install.packages("arulesViz")
library(arulesViz)
# Different Ways of Visualizing Rules
windows()
plot(arules_book)


windows()
plot(arules_book, method = "grouped")

# for good visualization try plotting only few rules
windows()
plot(arules_book[1:10], method = "graph")

#intresting rules
arules_book1 <- arules_book <- apriori(book , parameter = list(minlen =2 , maxlen =3 , conf =0.7),
                                       appearance = list(rhs=c("CookBks=1") , default = "lhs"))
inspect(arules_book1)

plot(arules_book1)

windows()
plot(arules_book1, method = "grouped")
plot(arules_book1[1:10], method = "graph")

###############################Problem 2##################################################
# The Departmental Store, has gathered the data of the products it sells on a 
# Daily basis. Using Association Rules concepts, provide the insights on the 
# rules and the plots.
library(readr)
groceries <- read.csv("C:\\Users\\hp\\Desktop\\association assi\\groceries.csv" ,colClasses = "factor")
summary(groceries)
length(groceries)
dim(groceries)

library(arules)
arules_groceries <- apriori(groceries , parameter = list(minlen =2 ,maxlen =4, supp = 0.01 , conf = 0.7))
summary(arules_groceries)
inspect(arules_groceries)

library(arulesViz)
windows()
plot(arules_groceries)

windows()
plot(arules_groceries, method = "grouped")

windows()
plot(arules_groceries[1:10], method = "graph")

inspect(head(sort(arules_groceries, by = "lift")))

#############################################Probelm 3#####################################
# A film distribution company wants to target audience based on their likes and 
# dislikes, you as a Chief Data Scientist Analyze the data and come up with different 
# rules of movie list so that the business objective is achieved.
library(readr)
my_movies <- read.csv("C:\\Users\\hp\\Desktop\\association assi\\my_movies.csv" ,colClasses = "factor")
summary(my_movies)
length(my_movies)
dim(my_movies)

library(arules)
arules_my_movies <- apriori(my_movies , parameter = list(minlen =2 ,maxlen =3, supp = 0.8 , conf = 0.7 ))
summary(arules_my_movies)
inspect(arules_my_movies)

library(arulesViz)
windows()
plot(arules_my_movies)

windows()
plot(arules_my_movies, method = "grouped")

windows()
plot(arules_my_movies[1:10], method = "graph")

inspect(head(sort(arules_my_movies, by = "lift")))


##############################Problem 4#############################################
# A Mobile Phone manufacturing company wants to launch its three brand new phone into 
# the market, but before going with its traditional marketing approach this time it want 
# to analyze the data of its previous model sales in different regions and you have been 
# hired as an Data Scientist to help them out, use the Association rules concept and provide
# your insights to the company’s marketing team to improve its sales.
library(readr)
my_phone <- read.csv("C:\\Users\\hp\\Desktop\\association assi\\myphonedata.csv" ,colClasses = "factor")
summary(my_phone)
length(my_phone)
dim(my_phone)

library(arules)
arules_my_phone <- apriori(my_phone , parameter = list(minlen =2 ,maxlen =3, supp = 0.4))
summary(arules_my_phone)
inspect(arules_my_phone)

library(arulesViz)

windows();plot(arules_my_phone)


windows();plot(arules_my_phone, method = "grouped")


windows();plot(arules_my_phone[1:10], method = "graph")

inspect(head(sort(arules_my_phone, by = "lift")))

#############################################Probelm 5#####################################
# A retail store in India, has its transaction data, and it would like to know the 
# buying pattern of the consumers in its locality, you have been assigned this task 
# to provide the manager with rules on how the placement of products needs to be there 
# in shelves so that it can improve the buying patterns of consumes and increase customer 
# footfall.
library(readr)
my_retail <- read.csv("C:\\Users\\hp\\Desktop\\association assi\\transactions_retail1.csv")
summary(my_retail)
length(my_retail)
dim(my_retail)
sum(is.na(my_retail))

my_retail[is.na(my_retail)] <- " "
sum(is.na(my_retail))

dup <- duplicated(my_retail)
sum(dup)
my_retail <- my_retail[!dup,]

colnames<-(names(my_retail))
my_retail[,colnames] <- lapply(my_retail[,colnames] , factor)

library(arules)
arules_my_retail <- apriori(my_retail , parameter = list(minlen =2 , supp = 0.02 , conf = 0.8 ))
summary(arules_my_retail)
inspect(arules_my_retail)

library(arulesViz)

windows();plot(arules_my_retail)


windows();plot(arules_my_retail, method = "grouped")


windows();plot(arules_my_retail[1:10], method = "graph")

inspect(head(sort(arules_my_retail, by = "lift")))

#############################################END########################################