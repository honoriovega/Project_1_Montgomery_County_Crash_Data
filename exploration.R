# Team Members : Honorio Vega, Jaime Velasquez
# Date: 03/13/2018
# CST383 - Data Science - Dr. Bruns

#https://docs.google.com/document/d/e/2PACX-1vTS7PeYktuRQ3cHLZD6iFstYzMoaHoLWqQ2MJcvBcq5fZkbCw3wuQpPrv8fIvlc-4UZQBDzDuAvKIng/pub

# Read data from the disk
dat = read.csv('Crash_Reporting_-_Drivers_Data.csv')

# Link to data documentation : https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Drivers-Data/mmzv-x632

# print the data
print(dat)

# TODO: What the data means
# TODO : how to clean the data

summary(dat)


#Do some initial exploration of the data.  How many rows and columns?  What are the types of the columns (ints, strings, factors, …?). 
#Don’t forget the ‘summary’ and ‘str’ commands.
#Do data preprocessing.  Is there any missing, NA, or corrupted data?  Identify and treat them appropriately.
#Do data exploration and visualization.  Look at each of the columns.  Which are interesting?  What kinds of single and multiple-variable visualizations can you do?  Think histograms, bar plots, scatter plots, etc.
#While you’re exploring the data, make a note of questions that come to mind that you’d like to answer. 
nrow(dat) #65841
length(dat) #32


for(element in dat[0,]) {
  print(typeof(element))
}
allNAindat = dat[is.na(dat),]
print(length(allNAindat))

# impute imissing data or remove
# if numeric impute, otherwise drop

