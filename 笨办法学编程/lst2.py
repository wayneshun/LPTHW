lst = [1,2,3,4,5]

t = lst[0]
lst.remove(t)
lst.insert(len(lst),t)
print lst