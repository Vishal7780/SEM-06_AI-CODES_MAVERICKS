# IInstalling packages that are required
if (!require("pacman")) install.packages("pacman")


pacman::p_load(pacman, bnlearn, bnclassify) 

if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")
BiocManager::install("graph")
BiocManager::install("Rgraphviz")

# Reading the data
data <- read.table("2020_bn_nb_data.txt", header = TRUE, col.names = c("EC100", "EC160", "IT101","IT161","MA101","PH100","PH160","HS101", "QP"))

# Now we have to convert character variables to factor variables
data[sapply(data, is.character)] <- lapply(data[sapply(data, is.character)], as.factor)

# Convert the data frame into a Bayesian network object
bn<- hc(data[,-9],score = 'k2')
# plotting the bayesian network
plot(bn)
bn

# fit the Bayesian network to the data
fitted_bn <- bn.fit(bn, data[,-9]) 
fitted_bn$EC100
fitted_bn$EC160
fitted_bn$IT101
fitted_bn$IT161
fitted_bn$MA101
fitted_bn$PH100
fitted_bn$HS101



#b.)  What grade will a student get in PH100 if he earns DD in EC100, CC in IT101 and CD in MA101:

# Predict the grade in PH100 based on evidence provided
prediction.PH100 <- data.frame(cpdist(fitted_bn, nodes = c("PH100"), evidence = (EC100 == "DD" & IT101 == "CC" & MA101 == "CD")))

# plot(prediction.PH100)
my_table <- table(prediction.PH100)
my_table
barp <- barplot(my_table, col = hsv(seq(0, 1, length.out = 8), 1, 1), ylim = c(0, 120))
text(barp, my_table + 6, labels = my_table)

# Set the seed for reproducibility
set.seed(101)

# Initialize an empty vector to store accuracy results
accuracy_results <- c()


for (i in 1:20) {
  
  # Split the data into training and testing sets using the sample function
  sample <- sample.int(n = nrow(data), size = floor(.7*nrow(data)), replace = F)
  data.train <-data[sample,]
  data.test<- data[-sample,]
  
  nb.grades <- nb(class = "QP",dataset= data.train)
  
  
  nb.grades<-lp(nb.grades, data.train, smooth=0)
 
  p<-predict(nb.grades, data.test)
  #Compute the confusion matrix using the table function
  cm<-table(predicted=p, true=data.test$QP)
  cm
  
  accuracy <- bnclassify:::accuracy(p, data.test$QP)
  
  # Store the accuracy in the vector
  accuracy_results <- c(accuracy_results, accuracy)
  
}

plot(nb.grades)

# Report the mean accuracy of the classifier (when courses are independent of each other)
mean(accuracy_results)

accuracy_results2 <- c()

for (i in 1:20) {
  
  
  tn <- tan_cl("QP", data.train)
  
  tn <- lp(tn, data.train, smooth = 1)
  
  p <- predict(tn, data.test)
  
  cm1<-table(predicted=p, true=data.test$QP)
  cm1

  accuracy2 <- bnclassify:::accuracy(p, data.test$QP)
  accuracy_results2 <- c(accuracy_results, accuracy2)
}

plot(tn)

mean(accuracy_results2)


