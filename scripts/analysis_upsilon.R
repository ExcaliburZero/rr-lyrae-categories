#
# Load in SMC data
#
data <- read.table("~/Documents/ogle/ogle3/smc/phot/ogle3_smc_I_upsilon.dat", sep="\t", header = TRUE)
categories <- read.table("~/Documents/ogle/ogle3/smc/ident_simple.dat", sep="\t", header = TRUE)

data$category <- categories$category

# Remove outliers
data <- data[data$period_uncertainty < 0.002, ]

require('ggplot2')

# plot.variable <- function(variable) {
#   ggplot(data, aes_string("category", variable)) +
#     geom_violin() +
#     coord_flip() +
#     ggtitle(paste("RR Lyrae",  variable, "(SMC OGLE III)"))
# }
# 
# for (variable in colnames(data)[1:24]) {
#   ggsave(
#       filename = paste("/home/chris/Code/rr-lyrae-categories/graphs/ogle3_smc_violin_" , variable, ".png", sep="")
#     , plot = plot.variable(variable)
#   )
# }

# ggplot(data, aes(period)) +
#   facet_wrap(~category) +
#   stat_density(geom = "line") + 
#   xlim(0,1) +
#   ggtitle("RR Lyrae Period Population Density by Category (SMC OGLE III)") +
#   xlab("Period (days)") +
#   ylab("Population Density")

require('randomForest')

# data.variables <- subset(data, select = -category)
data.variables <- subset(data, select = c(+period, +r21, +r31, +amplitude, +period_uncertainty))
data.labels <- data$category

set.seed(1234)
rf <- randomForest(data.variables, data.labels, importance = TRUE)
rf
varImpPlot(rf)

#
# Load in LMC data
#
dataLmc <- read.table("~/Documents/ogle/ogle3/lmc/phot/ogle3_lmc_I_upsilon.dat", sep="\t", header = TRUE)
categoriesLmc <- read.table("~/Documents/ogle/ogle3/lmc/ident_simple.dat", sep="\t", header = TRUE)

dataLmc$category <- categoriesLmc$category

# Remove outliers
dataLmc <- dataLmc[dataLmc$period_uncertainty < 0.001 & dataLmc$amplitude < 1 & dataLmc$period > 0.1 & dataLmc$period < 0.9, ]

predictions <- predict(rf, dataLmc)
table(predictions)

results <- data.frame(guess=predictions, actual=dataLmc$category)

resultsAB <- results[results$actual == "RRab" & results$guess != "RRab",]
resultsC <- results[results$actual == "RRc" & results$guess != "RRc",]
resultsD <- results[results$actual == "RRd" & results$guess != "RRd",]
resultsE <- results[results$actual == "RRe" & results$guess != "RRe",]

# ggplot(resultsAB, aes(guess)) +
#   geom_bar(stat="count") +
#   ggtitle("RRab Misclassifications")
# ggplot(resultsC, aes(guess)) +
#   geom_bar(stat="count") +
#   ggtitle("RRc Misclassifications")
# ggplot(resultsD, aes(guess)) +
#   geom_bar(stat="count") +
#   ggtitle("RRd Misclassifications")
# ggplot(resultsE, aes(guess)) +
#   geom_bar(stat="count") +
#   ggtitle("RRe Misclassifications")

correct <- results[results$actual == results$guess, "guess"]
table(correct)

numberCorrect <- length(correct)
total <- nrow(dataLmc)
numberCorrect / total

table(results)

# plot.variable <- function(variable) {
#   ggplot(dataLmc, aes_string("category", variable)) +
#     geom_violin() +
#     coord_flip() +
#     ggtitle(paste("RR Lyrae",  variable, "(LMC OGLE III)"))
# }
# 
# for (variable in colnames(dataLmc)[1:24]) {
#   ggsave(
#       filename = paste("/home/chris/Code/rr-lyrae-categories/graphs/ogle3_lmc_violin_" , variable, ".png", sep="")
#     , plot = plot.variable(variable)
#   )
# }