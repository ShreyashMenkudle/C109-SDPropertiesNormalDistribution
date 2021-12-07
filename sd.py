import statistics
import pandas as pd
import csv

df = pd.read_csv("data.csv")
height_list = df["Height(Inches)"].to_list()


mean = statistics.mean(height_list)
median = statistics.median(height_list)
mode = statistics.mode(height_list)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(mean,median,mode))
sd = statistics.stdev(height_list)                       
height_first_std_deviation_start, height_first_std_deviation_end = mean-sd, mean+sd
height_second_std_deviation_start, height_second_std_deviation_end = mean-(2*sd), mean+(2*sd)
height_third_std_deviation_start, height_third_std_deviation_end = mean-(3*sd), mean+(3*sd)

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))