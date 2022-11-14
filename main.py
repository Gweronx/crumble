from sys import argv
def repl():
    vs={}
    rt=[]
    re=[]
    ch=""
    mlc=0
    while True:
        try:
            txt=input(": ").replace("\t","").replace("    ","").replace("\n","")
            tokens=txt.split()
            if len(tokens)==0:pass
            elif txt.startswith("(*"):
                mlc=1
            elif txt.endswith("*)"):
                mlc=0
            elif tokens[0]=="chunk":
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
                elif tokens[0]=="pfi":
                    rt.insert(0,input(tokens[1].replace("//"," ").replace('"','')))
                elif tokens[0]=="run":
                    main(tokens[1])
                elif tokens[0]=="wtf":
                    nf=open(tokens[1],"w")
                    nf.write(vs[tokens[2]])
                    nf.close()
                elif tokens[0]=="rff":
                    nf=open(tokens[1])
                    print(nf.read())
                    nf.close()
                elif tokens[0]=="atf":
                    nf=open(tokens[1],"a")
                    nf.write(vs[tokens[2]])
                    nf.close()
                elif tokens[0]=="for":
                    for i in range(int(tokens[1])):
                        tokens=re[int(tokens[2])-1].replace("\t","").replace("    ","").replace("\n","").split()
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
                        elif tokens[0]=="pfi":
                            rt.insert(0,input(tokens[1].replace("//"," ").replace('"','')))
                        elif tokens[0]=="run":
                            main(tokens[1]+".cr")
                        elif tokens[0]=="wtf":
                            nf=open(tokens[1],"w")
                            nf.write(vs[tokens[2]])
                            nf.close()
                        elif tokens[0]=="rff":
                            nf=open(tokens[1])
                            print(nf.read())
                            nf.close()
                        elif tokens[0]=="atf":
                            nf=open(tokens[1],"a")
                            nf.write(vs[tokens[2]])
                            nf.close()
                        else:pass
                # Num 1
                elif tokens[0]=="crt":
                    if vs[tokens[1]]=='True':
                        tokens=re[int(tokens[2])-1].replace("\t","").replace("    ","").replace("\n","").split()
                        if tokens[0]=="out":
                            print(vs[tokens[1]])
                        elif tokens[0]=="equ":
                            if vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                            else:rt.insert(0,"False")
                        elif tokens[0]=="not":
                            if not vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                            else:rt.insert(0,"False")
                        elif tokens[0]=="add":
                            rt.insert(0,int(int(vs[tokens[1]])+int(vs[tokens[2]])))
                        elif tokens[0]=="sub":
                            rt.insert(0,int(int(vs[tokens[1]])-int(vs[tokens[2]])))
                        elif tokens[0]=="mul":
                            rt.insert(0,int(int(vs[tokens[1]])*int(vs[tokens[2]])))
                        elif tokens[0]=="div":
                            rt.insert(0,int(int(vs[tokens[1]])/int(vs[tokens[2]])))
                        elif tokens[0]=="pfi":
                            rt.insert(0,input(tokens[1].replace("//"," ").replace('"','')))
                        elif tokens[0]=="run":
                            main(tokens[1]+".cr")
                        elif tokens[0]=="wtf":
                            nf=open(tokens[1],"w")
                            nf.write(vs[tokens[2]])
                            nf.close()
                        elif tokens[0]=="rff":
                            nf=open(tokens[1])
                            print(nf.read())
                            nf.close()
                        elif tokens[0]=="atf":
                            nf=open(tokens[1],"a")
                            nf.write(vs[tokens[2]])
                            nf.close()
                        else:pass
                else:pass 
            elif ch=="reserve":
                if not tokens[0]=="chunk":
                    re.insert(0,txt)
                else:pass
            elif mlc==1:
                pass
            else:
                print(f"Command-Error:\n  {txt}\nWhat do you mean by \"{txt.split()[0]}\"?")
        except KeyError as e:
            print(f"Variable-Error:\n  {txt}\n{e} is not a variable.")
        except IndexError as e:
            print(f"List-Error:\n  {txt}\n{txt.split()[2]} is out of the return/reserve lists range.")
def error(line,number,filename):
    print(f"Command-Error on line {str(number)} in <{filename}>:\n  {line}\nWhat do you mean by \"{line.split()[0]}\"?")
def main(name):
    f=open(name)
    vs={"name":f.name,}
    rt=[]
    re=[]
    ln=1
    ch=""
    mlc=0
    try:
        for line in f:
            line=line.replace("\t","").replace("    ","").replace("\n","")
            tokens=line.split()
            if len(tokens)==0: pass
            elif line.startswith("(*"):
                mlc=1
            elif line.endswith("*)"):
                mlc=0
            elif tokens[0]=="chunk":
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
                elif tokens[0]=="pfi":
                    rt.insert(0,input(tokens[1].replace("//"," ").replace('"','')))
                elif tokens[0]=="run":
                    main(tokens[1])
                elif tokens[0]=="wtf":
                    nf=open(tokens[1],"w")
                    nf.write(vs[tokens[2]])
                    nf.close()
                elif tokens[0]=="rff":
                    nf=open(tokens[1])
                    print(nf.read())
                    nf.close()
                elif tokens[0]=="atf":
                    nf=open(tokens[1],"a")
                    nf.write(vs[tokens[2]])
                    nf.close()
                elif tokens[0]=="for":
                    for i in range(int(tokens[1])):
                        tokens=re[int(tokens[2])-1].replace("\t","").replace("    ","").replace("\n","").split()
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
                        elif tokens[0]=="pfi":
                            rt.insert(0,input(tokens[1].replace("//"," ").replace('"','')))
                        elif tokens[0]=="run":
                            main(tokens[1]+".cr")
                        elif tokens[0]=="wtf":
                            nf=open(tokens[1],"w")
                            nf.write(vs[tokens[2]])
                            nf.close()
                        elif tokens[0]=="rff":
                            nf=open(tokens[1])
                            print(nf.read())
                            nf.close()
                        elif tokens[0]=="atf":
                            nf=open(tokens[1],"a")
                            nf.write(vs[tokens[2]])
                            nf.close()
                        else:pass
                # Num 1
                elif tokens[0]=="crt":
                    if vs[tokens[1]]=='True':
                        tokens=re[int(tokens[2])-1].replace("\t","").replace("    ","").replace("\n","").split()
                        if tokens[0]=="out":
                            print(vs[tokens[1]])
                        elif tokens[0]=="equ":
                            if vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                            else:rt.insert(0,"False")
                        elif tokens[0]=="not":
                            if not vs[tokens[1]]==vs[tokens[2]]:rt.insert(0,"True")
                            else:rt.insert(0,"False")
                        elif tokens[0]=="add":
                            rt.insert(0,int(int(vs[tokens[1]])+int(vs[tokens[2]])))
                        elif tokens[0]=="sub":
                            rt.insert(0,int(int(vs[tokens[1]])-int(vs[tokens[2]])))
                        elif tokens[0]=="mul":
                            rt.insert(0,int(int(vs[tokens[1]])*int(vs[tokens[2]])))
                        elif tokens[0]=="div":
                            rt.insert(0,int(int(vs[tokens[1]])/int(vs[tokens[2]])))
                        elif tokens[0]=="pfi":
                            rt.insert(0,input(tokens[1].replace("//"," ").replace('"','')))
                        elif tokens[0]=="run":
                            main(tokens[1]+".cr")
                        elif tokens[0]=="wtf":
                            nf=open(tokens[1],"w")
                            nf.write(vs[tokens[2]])
                            nf.close()
                        elif tokens[0]=="rff":
                            nf=open(tokens[1])
                            print(nf.read())
                            nf.close()
                        elif tokens[0]=="atf":
                            nf=open(tokens[1],"a")
                            nf.write(vs[tokens[2]])
                            nf.close()
                        else:pass
                else:pass 
            elif ch=="reserve":
                if not tokens[0]=="chunk":
                    re.insert(0,line)
                else:pass
            elif mlc==1:
                pass
            else:
                error(line,ln,f.name)
            ln+=1
    except KeyError as e:
        print(f"Variable-Error on line {str(ln)} in <{f.name}>:\n  {line}\n{e} is not a variable.")
    except IndexError as e:
        print(f"List-Error on line {str(ln)} in <{f.name}>:\n  {line}\n{line.split()[2]} is out of the return/reserve lists range.")
    else:print(f"<{f.name}> executed succesfully.")
    repl()
if not argv[1]=="repl":
    main(argv[1])
else:
    repl()
