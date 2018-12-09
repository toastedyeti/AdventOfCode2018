

def openInput(fileName):
    out = ''
    with open(fileName) as f:
        out = f.read()
    out = [int(x) for x in out.split()]
    return out

def part1():
    pI = openInput('d8.txt')
    # NODE
        # Header -- Always two numbers 
            # quant child nodes
            # quant meta entries
        # Zero or more Child nodes
        # One or more meta entries
    # If the node has children, recursively parse the node data
    
    '''
    2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2

    <2,3> - [1,1,2]
    /    \
<0,3>   <1,1> -[99]
  |         \
[10,11,12]   <0,1> - [2]
    '''