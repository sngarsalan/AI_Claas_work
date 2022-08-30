def make_album(**artist_info):
    """Make Album Drecitory"""
    info={}
    for k,v in artist_info.items():
        info[k]=v
    print(info)
    return info

def build_profile(first,last,**user_info):
    """Profile Builder """
    profile={}
    profile["First Name"]=first
    profile["Last Name"]=last
    
    for k,v in user_info.items():
    
        profile[k]=v 
    
    print(user_info)
    return profile

def promotrStudents(list_of_st):
    """Promot Stuedents"""
    promotSt=[]
    for st in range(len(list_of_st)):
        promotSt.append(list_of_st.pop())
    print(list_of_st)
    print (promotSt)
