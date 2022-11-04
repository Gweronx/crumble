from sys import argv
def main(name):
    f=open(name)
    vs={}
    rt=[]
    re=[]
    ch=""
    for line in f:
        tokens=line.replace("\t","").replace("    ","").replace("\n","").split()
        if tokens[0]=="chunk":
            ch=tokens[1]
        elif tokens[0]==":":
            pass
        elif ch=="variables":
            vs.update({tokens[0]:tokens[1].replace("//"," ").replace('"','')})
        elif ch=="program":
            if tokens[0]=="out":
                print(vs[tokens[1]])
            elif tokens[0]=="equ":
                if vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                else:rt.insert(0,"False")
            elif tokens[0]=="not":
                if not vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                else:rt.insert(0,"False")
            elif tokens[0]=="srt":
                vs.update({tokens[1]:rt[int(tokens[2])-1]})
            elif tokens[0]=="add":
                rt.insert(0,int(int(vs[tokens[1]])+int(vs[tokens[2]])))
            elif tokens[0]=="sub":
                rt.insert(0,int(int(vs[tokens[1]])-int(vs[tokens[2]])))
            elif tokens[0]=="mul":
                rt.insert(0,int(int(vs[tokens[1]])*int(vs[tokens[2]])))
            elif tokens[0]=="div":
                rt.insert(0,int(int(vs[tokens[1]])/int(vs[tokens[2]])))
            elif tokens[0]=="crt":
                if vs[tokens[1]]=='True':
                    tokens=rv[tokens[2]].replace("\t","").replace("    ","").replace("\n","").split()
                    if tokens[0]=="out":
                        print(vs[tokens[1]])
                    elif tokens[0]=="equ":
                        if vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                        else:rt.insert(0,"False")
                    elif tokens[0]=="not":
                        if not vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                        else:rt.insert(0,"False")
                    elif tokens[0]=="srt":
                        vs.update({tokens[1]:rt[int(tokens[2])-1]})
                    elif tokens[0]=="add":
                        rt.insert(0,int(int(vs[tokens[1]])+int(vs[tokens[2]])))
                    elif tokens[0]=="sub":
                        rt.insert(0,int(int(vs[tokens[1]])-int(vs[tokens[2]])))
                    elif tokens[0]=="mul":
                        rt.insert(0,int(int(vs[tokens[1]])*int(vs[tokens[2]])))
                    elif tokens[0]=="div":
                        rt.insert(0,int(int(vs[tokens[1]])/int(vs[tokens[2]])))
                else:pass
            elif tokens[0]=="cfr":
                tokens=rv[tokens[1]].replace("\t","").replace("    ","").replace("\n","").split()
                if tokens[0]=="out":
                    print(vs[tokens[1]])
                elif tokens[0]=="equ":
                    if vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                    else:rt.insert(0,"False")
                elif tokens[0]=="not":
                    if not vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                        else:rt.insert(0,"False")
                    elif tokens[0]=="srt":
                        vs.update({tokens[1]:rt[int(tokens[2])-1]})
                    elif tokens[0]=="add":
                        rt.insert(0,int(int(vs[tokens[1]])+int(vs[tokens[2]])))
                    elif tokens[0]=="sub":
                        rt.insert(0,int(int(vs[tokens[1]])-int(vs[tokens[2]])))
                    elif tokens[0]=="mul":
                        rt.insert(0,int(int(vs[tokens[1]])*int(vs[tokens[2]])))
                    elif tokens[0]=="div":
                        rt.insert(0,int(int(vs[tokens[1]])/int(vs[tokens[2]])))
        elif ch=="reserve":
            if not tokens[0]=="chunk":
                re.insert(line)
            else:pass
main(argv[1])
