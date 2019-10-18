"""this code show that input name and age from user.
     Print out a message addressed to them that tells them 
     the year that they will turn 100 years old."""
     
class input_user():
    def name(self):
        self.user_name=input("Please enter you Name : ")
        return self.user_name
    def age(self):
        try:
            self.user_age=int(input("Enter your age : "))
            
            #check year user will turn 100 year
            if self.user_age <= 100:
                self.gap=(2019-self.user_age )+100
                return 'hi'+',\nyou will 100 year old in '+str(self.gap)
            else:
                return "you are awesome"
        except:
            return "please enter valid age"

user=input_user()
print(user.age(),'\n')

        

