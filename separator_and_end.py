# https://practice.geeksforgeeks.org/problems/sep-and-end-in-print/1/?track=fork-python&batchId=119

"""
In this task, you'll be required to write message seperated by and ending with '$'. Write Geeks$for$Geeks$
"""

#Function using 'end' and 'sep' parameters to print desired output
# string1 = "Geeks"
# string2 = "For"
def print_func(string1, string2):
    print ( string1 , string2 , string1 , sep = '$', end = '$')
# Use string1 & string2 with sep and end parameter to print desired output


#{ 
#Driver Code Starts.
def main():
    string1 = "Geeks"
    string2 = "For"
    print_func(string1, string2)
    print()


if __name__ == "__main__":
    main()
#} Driver Code Ends
