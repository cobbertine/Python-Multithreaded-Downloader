import argparse
import get_web_files

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("url_list_file", type=str, help="Specifies a file containing a list of URLs for this program to access.")

arg_parser.add_argument("-t", metavar="total_threads", type=int, help="Specifies how many threads can run concurrently. Default: 1", default=1)

arg_parser.add_argument("-r", metavar="total_retries", type=int, help="Specifies how many times a thread should attempt to access a URL after a failure before giving up. (A common failure case is a timeout). Default: 1", default=1)

arg_parser.add_argument("-w", metavar="retry_wait_time_seconds", type=int, help="Specifies (in seconds) how long a thread should wait after a failure before trying to access a URL again. NOTE: This is only applicable if 'total_retries' is > 0. Default: 3", default=3)

arg_parser.add_argument("-c", metavar="connection_timeout_seconds", type=int, help="Specifies (in seconds) how long a thread should wait for a response from a URL before aborting. Behaviour after aborting is dependent on 'total_retries' and 'retry_wait_time_seconds'. Default: 3", default=3)

arg_parser.add_argument("-s", metavar="status_code_whitelist", type=str, help="Specifies a list of status codes separated by a comma e.g. \"200,404\" that indicate the thread has successfully accessed the URL. If all codes are allowed, do not use this option.", default="")

arg_parser.add_argument("-m", metavar="request_mode", type=str, help="Specifies if the request will be a GET or a POST. Valid options: get|post. An invalid option will use the default value. Default: get", default="get")

arg_parser.add_argument("-d", action="store_true", help="This switch will indicate to the program to disable the request's server verification feature. If the default verify=True behaviour is wanted, do not use this option.", default=False)

arg_parser.add_argument("-f", metavar="config_json_file", type=str, help="Specifies a JSON configuration file containing extra options to pass into the request function. If none of the extra options defined in the file are needed, do not use this option.", default="")

args = arg_parser.parse_args()
arg_list = [args.url_list_file, args.t, args.r, args.w, args.c, args.s, args.m, args.d, args.f]

# Create object and launch e.g.
# get_web_files_object = get_web_files.GetWebFiles(*arg_list)
# get_web_files_object.launch_threads()
# or any other class you define...

get_web_files_object = get_web_files.GetWebFiles(*arg_list)
get_web_files_object.launch_threads()
