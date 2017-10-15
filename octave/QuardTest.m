
x = [1:100];
y = sin(x.*1/20*pi);
z = sin(x.*1/20*pi+pi/2);

plot(x,y);
hold on;
plot(x,z);
plot(x,y+z);


