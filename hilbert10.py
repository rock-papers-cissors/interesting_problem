import numpy as np
from scipy.linalg import solve

def hilbert10(n):
    """
    solve the problem a/(b+c)+b/(a+c)+c/(b+c)=n, a,b,c should be non-negative integer

    Args:
        n (int): 

    Returns
        (a,b,c)
    Solution:
        a=154476802108746166441951315019919837485664325
        669565431700026634898253202035277999
        b=368751317941299998271978115652254748254929799
        68971970996283137471637224634055579
        c=437361267792869725786125260237139015281653755
        8161613618621437993378423467772036
    """
    a=154476802108746166441951315019919837485664325669565431700026634898253202035277999
    b=36875131794129999827197811565225474825492979968971970996283137471637224634055579
    c=4373612677928697257861252602371390152816537558161613618621437993378423467772036

    print(a/(b+c)+b/(a+c)+c/(b+c))
    x = 0.5
    y = 1
    z = 2.5
    while True:
        x = 1/(z*2+1)
        y = 1/z
        if z == n-x-y:
            z = n-x-y
            a = 1
            b = (y+y*z)/(1-y*z)
            c = (1+b)*z
            return (a,b,c)
        z = n-x-y
        print(x,y,z)

    # 暴力解
    # for a in range(100):
    #     for b in range(100):
    #         for c in range(100):
    #             if (a+b)*(b+c)*(a+c) == 0:
    #                 continue
    #             if a%10==0 and b%10==0 and c%10==0:
    #                 print(a,b,c)
    #             if float(a)/float(b+c)+float(b)/float(a+c)+float(c)/float(a+b)==4:
    #                 return (a,b,c)

if __name__ == "__main__":
    print(hilbert10(4))
