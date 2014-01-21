s = ""

while True:
    s_new = raw_input("Enter a word (. ! or ? to end): ")
    if s_new in [".", "!", "?"]:
        s += s_new
        print s 
        break
    else:
        s = s + " " + s_new