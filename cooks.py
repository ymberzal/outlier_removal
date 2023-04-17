import pandas as pd
import numpy as np
import statsmodels.api as sm

# Read input data from text file
input_file = "cook.txt"
data = pd.read_csv(input_file, sep="\t")

# Fit linear regression model
X = sm.add_constant(data["Sample_size"])
model = sm.OLS(data["P_value"], X)
results = model.fit()

# Calculate Cook's distance and DFFITS
infl = results.get_influence()
cook_d = infl.cooks_distance[0]
dffits = infl.dffits[0]

# Identify outliers based on Cook's distance or DFFITS
outlier_idx = np.where((cook_d > 4/len(data)) | (np.abs(dffits) > 2*np.sqrt(len(data))/len(data)))[0]

# Remove outliers from data
clean_data = data.drop(outlier_idx)

# Write clean data to text file
output_file = "clean_data.txt"
clean_data.to_csv(output_file, sep="\t", index=False)

