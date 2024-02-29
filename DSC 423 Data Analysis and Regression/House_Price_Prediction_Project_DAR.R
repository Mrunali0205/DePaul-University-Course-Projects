# Load necessary libraries
library(tidyverse)
library(dplyr)
library(modeest)  # for the mfv function to find the mode
library(caret)    # For correlation
library(fastDummies)

# Importing data in R

df = read.csv("Property_Price_Train.csv", header = T)
dim(df)
head(df)

# Display basic information about the dataset
str(df)

# Display summary statistics
summary(df)

'''
# Finding NA% columnwise
na_percentages <- colMeans(is.na(df)) * 100

columns_with_high_na <- names(na_percentages[na_percentages > 60])

# Calculate the percentage of rows with NA
percentage_na_rows <- mean(apply(df, 1, function(row) any(is.na(row)))) * 100

# Removing columns which have high NA %.
df <- df[, !(names(df) %in% columns_with_high_na)]

# Calculate the percentage of rows with NA
percentage_na_rows <- mean(apply(df, 1, function(row) any(is.na(row)))) * 100

na_percentages <- colMeans(is.na(df)) * 100

columns_with_na <- names(na_percentages[na_percentages > 0])
columns_with_na

# Create a new dataframe Data_NA with selected columns
Data_NA <- df[, columns_with_na, drop = FALSE]

# Pulling out names of all numeric and categorical variables
numerical_columns <- sapply(Data_NA, is.numeric)
categorical_columns <- sapply(Data_NA, function(x) is.factor(x) | is.character(x))

# Create new dataframes for numerical and categorical columns
Numerical_Data_NA <- Data_NA[, numerical_columns, drop = FALSE]
Categorical_Data_NA <- Data_NA[, categorical_columns, drop = FALSE]


# Replace NA values with mean for all columns
Numerical_Data_NA <- Numerical_Data_NA %>% mutate_all(~ ifelse(is.na(.), mean(., na.rm = TRUE), .))

# Checking NA% now
colMeans(is.na(Numerical_Data_NA)) * 100


# Function to find the mode
find_mode <- function(x) {
  mode_result <- mfv(x,na_rm = TRUE)
  if (length(mode_result) > 0) {
    return(mode_result)
  } else {
    # If there is no mode, return NA
    return(NA)
  }
}

# Checking what mfv function does
mfv(Categorical_Data_NA$FireplaceQu, na_rm = TRUE)

# Checking if find_mode function working properly
sapply(Categorical_Data_NA, find_mode)

# Replace NA values with mode for all columns
Categorical_Data_NA <- Categorical_Data_NA %>% mutate_all(~ ifelse(is.na(.), find_mode(.), .))

# Checking NA% now
colMeans(is.na(Categorical_Data_NA)) * 100
'''

#--------------------------------------------START Preprocessing------------------------------------------

df <- df[, !colnames(df) %in% "Id"]

# Dealing wih columns with dates
#1. To get the house life, we will substract the construction year column from current year.
#2. Also we will remove other variables with dates as it does not any value in ML models.

df$House_Life <- 2023 - df$Construction_Year

# Removing other date variables

df <- subset(df, select = -c(Construction_Year, Remodel_Year, Garage_Built_Year, Month_Sold, Year_Sold))
dim(df)


# In the data, there are lot of columns which has NA values but which are not actual NaN values. These values shold be something else.
Lane_Type = No_Allay_Access
Basement_Height = No_Basement
Basement_Condition = No_Basement
Exposure_Level = No_Basement
BsmtFinType1 = No_Basement
BsmtFinType2 = No_Basement
Fireplace_Quality = No_Fireplace
Garage = No_Garage
Garage_Finish_Year = No_Garage
Garage_Qualit = No_Garage
Garage_Condition = No_Garage
Pool_Quality = No_Pool
Fence_Quality = No_Fence
Fence_Quality = None

df$Lane_Type <- ifelse(is.na(df$Lane_Type), "No_Allay_Access", df$Lane_Type)
df$Basement_Height <- ifelse(is.na(df$Basement_Height), "No_Basement", df$Basement_Height)
df$Basement_Condition <- ifelse(is.na(df$Basement_Condition), "No_Basement", df$Basement_Condition)
df$Exposure_Level <- ifelse(is.na(df$Exposure_Level), "No_Basement", df$Exposure_Level)
df$BsmtFinType1 <- ifelse(is.na(df$BsmtFinType1), "No_Basement", df$BsmtFinType1)
df$BsmtFinType2 <- ifelse(is.na(df$BsmtFinType2), "No_Basement", df$BsmtFinType2)
df$Fireplace_Quality <- ifelse(is.na(df$Fireplace_Quality), "No_Fireplace", df$Fireplace_Quality)
df$Garage <- ifelse(is.na(df$Garage), "No_Garage", df$Garage)
df$Garage_Finish_Year <- ifelse(is.na(df$Garage_Finish_Year), "No_Garage", df$Garage_Finish_Year)
df$Garage_Qualit <- ifelse(is.na(df$Garage_Qualit), "No_Garage", df$Garage_Qualit)
df$Garage_Condition <- ifelse(is.na(df$Garage_Condition), "No_Garage", df$Garage_Condition)
df$Pool_Quality <- ifelse(is.na(df$Pool_Quality), "No_Pool", df$Pool_Quality)
df$Fence_Quality <- ifelse(is.na(df$Fence_Quality), "No_Fence", df$Fence_Quality)

na_percentages <- colMeans(is.na(df)) * 100

df <- df[, !names(df) %in% "Miscellaneous_Feature"]
head(df)


# Calculate the percentage of rows with NA
percentage_na_rows <- mean(apply(df, 1, function(row) any(is.na(row)))) * 100
print(percentage_na_rows)

# Creating a function to impute NA values
imputeNA <- function(data) {
  for (col in names(data)) {
    if (is.numeric(data[[col]])) {
      # Impute NA with mean for numeric variables
      data[[col]][is.na(data[[col]])] <- mean(data[[col]], na.rm = TRUE)
    } else if (is.factor(data[[col]]) | is.character(data[[col]])) {
      # Impute NA with mode for categorical or factor variables
      mode_val <- as.character(sort(table(data[[col]]), decreasing = TRUE)[1])
      data[[col]][is.na(data[[col]])] <- mode_val
    }
    # If neither numeric nor categorical, do nothing
  }
  return(data)
}

df<-imputeNA(df)

# Calculate the percentage of rows with NA after imputaion
percentage_na_rows_1 <- mean(apply(df, 1, function(row) any(is.na(row)))) * 100
print(percentage_na_rows_1)


class(df$Garage_Size)

# ---------------- Do not run this as don't know if it is correct
df$Garage_Size <- as.factor(df$Garage_Size)
df$Fireplaces <- as.factor(df$Fireplaces)
df$Rooms_Above_Grade <- as.factor(df$Rooms_Above_Grade)
df$Kitchen_Above_Grade <- as.factor(df$Kitchen_Above_Grade)
df$Bedroom_Above_Grade <- as.factor(df$Bedroom_Above_Grade)
df$Half_Bathroom_Above_Grade <- as.factor(df$Half_Bathroom_Above_Grade)
df$Full_Bathroom_Above_Grade <- as.factor(df$Full_Bathroom_Above_Grade)
df$Underground_Half_Bathroom <- as.factor(df$Underground_Half_Bathroom)
df$Underground_Full_Bathroom <- as.factor(df$Underground_Full_Bathroom)
df$House_Condition <- as.factor(df$House_Condition)
df$Overall_Material <- as.factor(df$Overall_Material)
df$Building_Class <- as.factor(df$Building_Class)
#-----------------------------------------------------------------

df$Garage_Area[df$Garage_Area<0]

# Checking if any of the data have negative values
numeric_cols <- sapply(df, is.numeric)
neg_values <- sapply(df[, sapply(df, is.numeric)], function(x) any(x < 0))

# Need to replace these negative values for Area columns with 0 as area cannot be negative

cols_to_replace <- c("Garage_Area", "W_Deck_Area", "Open_Lobby_Area", "Enclosed_Lobby_Area")

df[, cols_to_replace] <- lapply(df[, cols_to_replace], function(x) ifelse(x < 0, 0, x))


# Checking if data has Biased columns

checkDominantClass <- function(data) {
  # Get column names with class factor or character type
  class_columns <- sapply(data, function(x) is.factor(x) | is.character(x))
  
  for (col in names(data)[class_columns]) {
    # Check if the dominant class contributes more than 95%
    class_counts <- table(data[[col]])
    dominant_class <- names(class_counts)[which.max(class_counts)]
    dominant_class_percentage <- max(class_counts) / sum(class_counts)
    
    if (dominant_class_percentage > 0.95) {
      cat(sprintf("Variable '%s' has a dominant class: %s, which contributes %.2f%% of the total.\n", col, dominant_class, dominant_class_percentage * 100))
    }
  }
}
checkDominantClass(df)


# Removing variables which has dominant class > 95%

df <- subset(df, select = -c(Road_Type, Utility_Type, Condition2, Roof_Quality, Heating_Type,Pool_Quality))
dim(df)

# ---------- Target Variable Analysis

# Plotting histogram of target variable

hist(df$Sale_Price, main = "Histogram of Sale_Price", xlab = "Sale_Price", col = "skyblue", border = "black")

sale_price_skewness <- skewness(df$Sale_Price)

cat("Skewness of Sale_Price:", sale_price_skewness, "\n")

# Finding outliers

# Calculate Z-scores
z_scores <- scale(df$Sale_Price)

# Set a threshold (e.g., 3 or -3)
threshold <- 3

# Identify outliers
outliers <- which(abs(z_scores) > threshold)

# Print the indices of outliers
cat("Indices of outliers in Sale_Price:", outliers, "\n")

# Print the values of outliers
cat("Values of outliers in Sale_Price:", df$Sale_Price[outliers], "\n")


# Remove rows with outliers
df <- df[-outliers, ]

# Print information about removed rows
cat("Number of rows removed:", length(outliers), "\n")

hist(df$Sale_Price, main = "Histogram of Sale_Price", xlab = "Sale_Price", col = "skyblue", border = "black")

skewness(df$Sale_Price)

# Identify numeric and categorical columns
numeric_cols <- sapply(df, is.numeric)
categorical_cols <- sapply(df, function(x) is.factor(x) | is.character(x))

# Create df_numeric and df_categorical
df_numeric <- df[, numeric_cols]
df_categorical <- df[, categorical_cols]

# Checking skewness of all numeric variables

apply(df_numeric, 2, skewness)[apply(df_numeric, 2, skewness)>2]
cols_with_high_skewness <- names(apply(df_numeric, 2, skewness)[apply(df_numeric, 2, skewness)>2])

# Perform log transformation for selected columns
df_numeric[, cols_with_high_skewness] <- log1p(df_numeric[, cols_with_high_skewness])

# Print the transformed dataframe
apply(df_numeric, 2, skewness)


##------------------------------------------ EDA ----------------------------------------------------



## ----------------------------------- Feature Selection ---------------------------------------------

# Checking correlation 
correlation_matrix <- cor(df_numeric)

# Find columns with correlation > 0.85
highly_correlated_cols <- findCorrelation(correlation_matrix, cutoff = 0.8)

# Remove highly correlated columns
df_numeric <- df_numeric[, -highly_correlated_cols]

df_numeric <- df_numeric[, -Id]

df_numeric <- df_numeric[, !colnames(df_numeric) %in% "Id"]


#  Combining Data ---------

New_df <- cbind(df_numeric, df_categorical)

# Creating dummy variables

cols_categorical <- colnames(df_categorical)

# Create dummy variables for categorical columns
df_combined_dummies <- dummy_cols(New_df, select_columns = cols_categorical)

dim(df_combined_dummies)

# ------------------------------------ Splitting Data -------------------------------------------------

# Creating a train/test partition
set.seed(456) 
splitIndex <- createDataPartition(df_combined_dummies$Sale_Price, p = 0.8, list = FALSE)
df_train <- df_combined_dummies[splitIndex, ]
df_test <- df_combined_dummies[-splitIndex, ]

dim(df_train)
dim(df_test)

model_m1 <- lm(Sale_Price ~ ., data=df_train)

predictions <- predict(model_m1, newdata = df_test)

summary(model_m1)

for (col in names(df_train)) {
  if (is.factor(df_train[[col]]) && is.factor(df_test[[col]])) {
    levels_train <- levels(df_train[[col]])
    df_test[[col]] <- factor(df_test[[col]], levels = levels_train)
  }
}
