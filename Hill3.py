import random
import numpy as np

def accept_prob(S_old, S_new, T):
    p = np.exp(-(S_old-S_new)/T)
    print(p)
    return 1 if p >= 1 else p

# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

print(1<1.00000000001)
print(accept(205,205.1,100000000))