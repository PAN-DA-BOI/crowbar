

#array = [1,2,3,
#		 4,5,6,
#		 7,8,9,
#		 *,0,.,
#		 ↑,|,↓
#		 ]
         
#1 = r1,c1
#2 = r1,c2
#3 = r1,c3

#4 = r2,c1
#5 = r2,c2
#6 = r2,c3

#7 = r3,c1
#8 = r3,c2
#9 = r3,c3

#0 = r4,c1
#* = r4,c2
#. = r4,c3

#↑ = r5,c1
#| = r5,c2
#↓ = r5,c3

c1 = gpio.19
c2 = gpio.20
c3 = gpio.21

r1 = gpio.5
r2 = gpio.6
r3 = gpio.12
r4 = gpio.13
r5 = gpio.16


if c1 == high:
    if r1 == high:
        sendkey('1')
    elif r2 == high:
        sendkey('4')
    elif r3 == high:
        sendkey('7')
    elif r4 == high:
        sendkey('0')
    elif r5 == high:
        sendkey('↑')
if c2 == high:
    if r1 == high:
        sendkey('2')
    elif r2 == high
        sendkey('5')
    elif r3 == high:
        sendkey('8')
    elif r4 == high:
        sendkey('*')
    elif r5 == high:
        sendkey = enter
if c3 == high:
    if r1 == high:
        sendkey('3')
    elif r2 == high:
        sendkey('6')
    elif r3 == high:
        sendkey('9')
    elif r4 == high:
        sendkey('.')
    elif r5 == high:
        sendkey('↓')