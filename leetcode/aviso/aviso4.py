string="co?3d5er45,3"
negative=True if string[0]=="-" else False
string=[str for str in string if str.isdigit()]
if len(string)<=3:
    print(-1)
else:
    string[1],string[0]=string[0],string[1]
    string[-1],string[-2]=string[-2],string[-1]
    print("".join(string))