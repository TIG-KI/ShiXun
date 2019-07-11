
'''
现在有50瓶水，3个瓶盖可以换一瓶水，问一个人最多能喝多少瓶水？
'''
sum = 50
num = 50
em = sum // 3 + sum % 3
num += num // 3

def fun(em):
    global num
    if em < 2:
        return
    elif em == 2:
        num += 1
        return
    else:
        num += em // 3
        em = em // 3 + em % 3
        fun(em)

fun(em)

print("能喝：",num," 瓶")
