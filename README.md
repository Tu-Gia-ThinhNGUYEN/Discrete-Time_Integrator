# 1. Overview
This is reference to demonstrate calculating integrator in discrete-time. In this repository, the Forward Euler, Backward Euler, and Bilinear are methods used to calculate discrete-time integrator.

If you find this repository helpful, please give it a star. Thank you very much!

# 2. Methodologies
## 2.1. The problem
Assuming that our system have a integral part as bellow:

$$y=\int_{0}^{10}Ktdt$$

Where K is input gain. And this function after Laplace transform is:

$$G(s)=\frac{y(s)}{t(s)}=K\frac{1}{s}$$

## 2.2. Forward Euler
This method will replace $s$ in above transfer function into:

$$s=\frac{z-1}{T_{s}}$$

Where $T_{s}$ is sampling time. So the transfer function can be rewriten:

$$\frac{y(z)}{t(z)}=\frac{K.T_{s}}{z-1}$$

$$\Leftrightarrow y(z-1)=K.T_{s}t$$

Call $y(z)=y$ and $t(z)=t$, we have coressponding equation as:

$$\Rightarrow y=y.z^{-1}+K.T_{s}.t.z^{-1}$$

Where $y.z^{-1}$ is previous result (called is $y_{prev}$) and $t.z^{-1}$ is previous time (called is $t_{prev}$). Thus, the above equation can be expressed as:

$$\Rightarrow y=y_{prev}+K.T_{s}.t_{prev}$$

Bellow is Python code to demonstrate above equation, with the $T_{s}=1us$ (1MHz frequency) and considering time from 0 to 10s:

```
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
```
The result will be:
```
Forward Euler method: 499.99985000001016
```
## 2.3. Backward Euler
This method will replace $s$ in above transfer function into:

$$s=\frac{z-1}{z.T_{s}}$$

Where $T_{s}$ is sampling time. So the transfer function can be rewriten:

$$\frac{y(z)}{t(z)}=\frac{K.T_{s}.z}{z-1}$$

$$\Leftrightarrow y(z-1)=K.T_{s}.t.z$$

Call $y(z)=y$ and $t(z)=t$, we have coressponding equation as:

$$\Rightarrow y=y.z^{-1}+K.T_{s}.t$$

Where $y.z^{-1}$ is previous result (called is $y_{prev}$). Thus, the above equation can be expressed as:

$$\Rightarrow y=y_{prev}+K.T_{s}.t$$

Bellow is Python code to demonstrate above equation, with the $T_{s}=1us$ (1MHz frequency) and considering time from 0 to 10s:

```
y = 0 #Result
y_prev = 0 #Previous result
t = 0 #Time
t_prev = 0 #Previous time
Ts = 1/1000000 #1MHz
k=10 #Function gain

xs = (x * Ts for x in range(0, int(10/Ts)))

for i in xs:
    t = i
    y = y_prev + k*Ts*t
    t_prev = t
    y_prev = y
print("Backward Euler method: " + str(y))
```
The result will be:
```
Backward Euler method: 499.99985000001016
```
## 2.4. Bilinear
This method will replace $s$ in above transfer function into:

$$s=\frac{(z-1).2}{(z+1).T_{s}}$$

Where $T_{s}$ is sampling time. So the transfer function can be rewriten:

$$\frac{y(z)}{t(z)}=\frac{K.T_{s}.(z+1)}{2.(z-1)}$$

Call $y(z)=y$ and $t(z)=t$, we have coressponding equation as:

$$\Leftrightarrow y.(z-1)=\frac{K.T_{s}.t.(z+1)}{2}$$

$$\Rightarrow y=y.z^{-1}+\frac{K.T_{s}.(t+t.z^{-1})}{2}$$

Where $y.z^{-1}$ is previous result (called is $y_{prev}$) and $t.z^{-1}$ is previous time (called is $t_{prev}$). Thus, the above equation can be expressed as:

$$\Rightarrow y=y_{prev}+\frac{K.T_{s}.(t+t_{prev})}{2}$$

Bellow is Python code to demonstrate above equation, with the $T_{s}=1us$ (1MHz frequency) and considering time from 0 to 10s:

```
y = 0 #Result
y_prev = 0 #Previous result
t = 0 #Time
t_prev = 0 #Previous time
Ts = 1/1000000 #1MHz
k=10 #Function gain

xs = (x * Ts for x in range(0, int(10/Ts)))

for i in xs:
    t = i
    y = y_prev + k*Ts*(t + t_prev)/2
    t_prev = t
    y_prev = y
print("Bilinear method: " + str(y))
```
The result will be:
```
Bilinear method: 499.99985000001016
```

# 3. Conclusion
In this repository I introduced 3 methods to calculate discrete-time integrator.

 Again if you find this repository helpful, please give it a star. Thank you for reading!
