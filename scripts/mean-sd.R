#!/usr/bin/Rscript

# Get input file path
args <- commandArgs(trailingOnly = TRUE)
input_file <- args[1]

# Process data from input file
periodsList <- read.table(input_file)
periodsVector <- unlist(periodsList)
cat(mean(periodsVector), "\n", sep = '')
cat(sd(periodsVector), "\n", sep = '')
