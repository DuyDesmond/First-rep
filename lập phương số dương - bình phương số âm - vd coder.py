m=int(input())
n=int(input())
k=int(input())

# lập phương số dương - bình phương số âm

def bp_lp(x):
    if x < 0:
        x = x ** 2
    else:
        x = x ** 3      
    return x

print(bp_lp(m),bp_lp(n),bp_lp(k))
    