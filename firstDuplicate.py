def firstDuplicate(a):

    aset = set()
    for i in a:
        if i in aset:
            ret = i
    
        else:   
            aset.add(i)
    if ret is None:
        return -1
    else:
        return ret
