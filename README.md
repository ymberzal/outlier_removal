# outlier_removal
The script calculates both Cook's distance and DFFITS, but it only uses one of them to identify outliers, depending on which criterion is more stringent.

Specifically, the script uses the following criteria to identify outliers:

    Cook's distance: any data point with a Cook's distance greater than 4/n, where n is the number of data points.
    DFFITS: any data point with an absolute DFFITS value greater than 2*sqrt(n)/n.

The script then removes any data points that meet either of these criteria.

By default, the script first checks for outliers using Cook's distance, and only uses DFFITS if there are no outliers identified using Cook's distance. 

Usage: python3 cooks.py
The input file must contain three columns : SNP_ID	P_value	Sample_size
The input columns must be separated by tab.

