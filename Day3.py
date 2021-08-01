def Gift(l):
    gift_presented_to = l
    gift_presented_to[2],gift_presented_to[3],gift_presented_to[4] =gift_presented_to[4],gift_presented_to[2],gift_presented_to[3]
    return gift_presented_to
print(Gift([2,1,5,3,4]))
