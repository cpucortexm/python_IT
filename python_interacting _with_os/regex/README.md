# Script to Read a csv file and replace the domain abc with xyz.

## Steps:
1. read the csv contents as a list (say user_data_list)
2. prepare two new lists containing old domain and new domain
3. Iterate through the user_data_list from (1) and if the column for email matches the old domain, replace it with new domain. Finally results in updated user_data_list with new domain
4. At this stage we are ready with the updated user_data_list and now it needs to be written to a new csv file