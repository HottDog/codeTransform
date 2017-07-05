import re
def rrr(m):
    return "T("+m.group(0)+")"
def rrr2(m):
    if m.group(2) != None :
        s=re.search("(?<=(\[\[))(.+)(?=(\]\]))",m.group(2),0)
        print(s)
        print("T(\""+s.group()+"\")")
        return "T(\""+s.group()+"\")"
    else:
        return m.group(0)
def pr(mm):
    count =0 ;
    for m_read in mm :
        print("找出所有的符合字串：",m_read.group(0))
        # if m_read.group(count) != None :
        #     print("找出所有的符合字串：",m_read.group(count))
def pr_all(mm):
    for m_read in mm:
        count =1
        while(count<10):
            if m_read.group(count)!=None:
                print("group",count,":",m_read.group(count))
def pl():
    print("------------------------------------")
