sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
count = 0

for x in range(0,len(sentence)):
    if sentence[x:x+5] == "whale":       # 5 means w h a l e (5 letters) checking if 5 letter word equals whale
        count = count + 1
print(count)






#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
