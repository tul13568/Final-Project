with open('business_list.txt', 'r') as file:
    pass
    file= file.read().splitlines()
# I want to name the site New Tea
# It is a platform for small business that allows them to compete with eachother and not the more mainstream, bigger corporations
# I would want it to also be a platform that allows small business whether it be justifying reviews, etc. 
# This is the code, I am going to call it the search engine

def main():
    search= input("What are you looking for: ")
    for i in file:
        if search in file:
            return i 
        else:
            print("no results found")


