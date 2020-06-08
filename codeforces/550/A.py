s = input()
if(s.count("AB")):
    tmp = s.replace("AB"," ",1)
    if(tmp.count("BA")):
        print("YES")
    else:
        if(s.count("BA")):
            tmp = s.replace("BA"," ",1)
            if(tmp.count("AB")):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
else:
    print("NO")