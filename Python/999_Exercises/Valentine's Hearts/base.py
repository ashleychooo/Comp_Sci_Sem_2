people_list = ["Your Mom", "Your Dad", "Your sister", "Your Friend", "Your grandfather"]
comp_list = ["is cool", "is kind", "is nice", "is smart", "is amazing", "is wonderful"]

import random
num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people] + " " + comp_list[num_comp])