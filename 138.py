if head is None:
    return None

dict_1 = {}
dict_2 = {}

p_1 = head
p_2 = None    
idx = 0
while p_1 is not None:
    idx += 1
    dict_1[p_1] = idx
    if p_2 == None:
        p_2 = RandomListNode(p_1.label)
        p = p_2
    else:
        p.next = RandomListNode(p_1.label)
        p = p.next
    dict_2[idx] = p
    p_1= p_1.next
    
p_1 = head 
p = p_2     
idx = 0
while p_1 is not None:
    idx += 1
    if p_1.random is None:
        p.random = None
    else:
        p.random = dict_2[dict_1[p_1.random]]
    p_1 = p_1.next
    p = p.next

return p_2