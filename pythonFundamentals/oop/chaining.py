class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    
    def display_info(self):
        print(self.first_name) 
        print(self.last_name) 
        print(self.email) 
        print(self.age)
        return self
    
    def enroll(self):
        if (self.is_rewards_member == True):
            print("user is already a member")
            return False
        else: self.is_rewards_member = True
        self.gold_card_points = 200
        print(f"congratulations {self.first_name} you're enrolled in the rewards program and have {self.gold_card_points} points to spend")
        return self
    
    def spend_points(self, amount):
        if (self.gold_card_points) < amount:
            print(f"you can't do that {self.first_name}, not enough points")
        else: 
            self.gold_card_points = (self.gold_card_points - amount)
            (print(f"{self.first_name} you just spent {amount} points and have {self.gold_card_points} points left"))
        return self

brian = User('brian', 'randall', 'brian@mail.com', '32').display_info().enroll()

james = User('james', 'jamerson', 'james@jmail.com', '72')
blake = User('blake', 'blakerson', 'blake@bmail.com', '12')
james.spend_points(50)
blake.enroll().spend_points(80)

brian.display_info()
blake.display_info()
james.display_info()

brian.enroll()
blake.spend_points(3000)
