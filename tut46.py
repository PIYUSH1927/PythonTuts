from tut41 import function
args=(3,8)
function(*args)


#here 1 , 6, 9 come from tut41 by import even if we dont want them , so now if we want to remove that 1,6,9 we have to
#write    if__name__=="__main_":    before  args= (1,6,9)   line in tut41 .