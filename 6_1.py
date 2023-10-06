
qlist = []

def enqueue(qlist, data):
    qlist.append(data)
    
def dequeue(qlist):
        data = qlist[0]
        del qlist[0]
        return data
    
enqueue(qlist, 1)
print(qlist)

enqueue(qlist, 2)
print(qlist)

enqueue(qlist, 3)
print(qlist)

dequeue(qlist)
print(qlist)

dequeue(qlist)
print(qlist)