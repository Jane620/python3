
list1  = [1,2,3,4]

def myreduce(function,sequence):
    first = sequence[0]
    for next in sequence[1:]:
        print(sequence)
        first = function(sequence,next)
    return first

print(myreduce(sum,list1))
