import parse_log

if __name__=="__parse_log__":
   log_file = sys.argv[1]
   returned_errors = error_search(log_file)
   file_output(returned_errors) #Output the returned list to another log file
   sys.exit(0)

