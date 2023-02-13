
li5=["jigu","2",3,4,5]
print(li5)
def outer(dec):
    def inner(a):
        a=5
        return a
    return inner
@outer
def deco(a):
    
    return a
print(deco(4))
        