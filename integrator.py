y = 0 #Result
y_prev = 0 #Previous result
t = 0 #Time
t_prev = 0 #Previous time
Ts = 1/1000000 #1MHz
k=10 #Function gain

xs = (x * Ts for x in range(0, int(10/Ts)))

for i in xs:
    t = i
    y = y_prev + k*Ts*t_prev
    t_prev = t
    y_prev = y
print("Forward Euler method: " + str(y))

for i in xs:
    t = i
    y = y_prev + k*Ts*t
    t_prev = t
    y_prev = y
print("Backward Euler method: " + str(y))

for i in xs:
    t = i
    y = y_prev + k*Ts*(t + t_prev)/2
    t_prev = t
    y_prev = y
print("Bilinear method: " + str(y))