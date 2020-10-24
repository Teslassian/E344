Temperature = [34 36 38 40 42];
Voltage = [0.047 1.177 2.414 3.664 4.89];  
set(0,'DefaultLineLineWidth',3)
plot(Voltage,Temperature,'.b',  'MarkerSize',20)
p = polyfit(Voltage,Temperature,1)
f = polyval(p,Voltage);
hold on
plot(Voltage,f,'--', 'Color',[0,0.7,0.9])
xlabel('Voltage')
ylabel('Temperature')