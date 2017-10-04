
def pr():
    print('xxxxx')

def add(a,b):
    print(a+b)

funs ={
    'f1':pr,
    'f2':add
}


fun = funs['f2']
args=[4,44]
# kwargs={'a':2,'b':22}
fun(*args)