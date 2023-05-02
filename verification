# This is the code I got for verification
# Here we want to get a business, put it through a bunch of different parameters, and from there add it to the list of approved business
# I want my program to be a mixture of computer and human skills, as each has their flaws
# So there is a part that is verfied manually after the computer does the work

#Parameters: Any appropriate liscenes, ID associated with the owner, business description(like food, hair, nails, clothes, etc), A video of themselves showing and explaining their business
# I think I want to make it a live video of proof like with a client or in the food etc. , just because other people(scammers) have been taking the videos off of people's websites and uploading it as their own.

# Wants to add a background check
# The live video will be watched by someone but everything else would be check by a computer

def license(certification,name):
    if certification == "yes":
        print("Upload your certification here  ") 
        print(name)
        return True
        # https://file.dos.pa.gov/search/business  This link can be used to look up the business manually
        #currently only doing Philadelphia, so check Pennsylavania LLCs, coroporations, and also put through a search engine to see what comes up
    else:
        new_business= input("Did you want to start the processs to get a new license or certification: ").lower()
        print('yes')
        
        if new_business == "yes":
            print("Send them the correct links to get the license/certification")
        else:
            print("Your business will listed as unlicensed/uncertified")
            return False
    

def ID(name):
    # some type of program to analyze the ID, puts different parts as dictionary, dtore name as key 1 get name and photo
    # if name on ID is the same as name entered, continue
    ceo_name =("Your Name: ")
    verified = False
    if verified == False:
        # file is just a placeholder
        if file.get(1) != name:
            verified== True
        else:
            print("You could not be verifed, you must reupload your ID")

        
#create a zoom link for them to join
#the zoom link is the final step after everything else returns True
        

    # program to 


def get_business():
    
    new_business= input("Did you want to add your business to the site? ").lower()
    
    if new_business== "yes":
        business_name = input("Business Name: ")
        certification= input("Do you have any relevant certifications or licenses?: " ).lower()
        
        if license(certification,business_name) == False:
            license(certification,business_name)
       
        else:
            type=input("What type of business is it?(one word is enough): ")
            certified= "no"
            with open('business_list','w') as file:
                file.write(business_name)
                file.write(type)
                file.write(certified)
            #   file. write(verfied)
                file.close( )

    
    else:
        input("Goodbye")

get_business()





    #ask this questions at the end  because it is not relevant until after it is verified
    

    