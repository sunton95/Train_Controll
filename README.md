# Train_Controll
I have always wanted to make a project that includes communication between devices and sets up includes several different parts of hardware and software development. So when my father required his childhood interest in model railways I found a great opportunity to communicate it. This controller consists of the main control hub which uses a raspberry pi that controls several nodes. The nodes are custom-designed PCBs and the maximum amount of nodes is only limited by hardware. I think the maximum amount of railway switches that can be controlled should be in the amount of 896 but that would require a lot of hardware. 

The main part of the project was to design the PCB of the nodes. The plan was to control MOSFETs as switches with an ATMEGA328 and get power from the rail. From the märklin railway system, the power coming from the rails is between 16-24 AC voltage depending on what power suplly is used. That voltage is also used for switching the switches. The voltage is rectified and stepped down to 5 Volts for the control circuit. Some safety circuitry is not used but probably should but with the cost increasing that was skipped.

The PCB went trough three different iterations

![The first and second design](https://i.imgur.com/KDHDt2H.jpeg)

![The main hub](https://i.imgur.com/FQZg7Ew.jpg)

![Enclosure for node](https://i.imgur.com/KG89BVh.jpeg)

 # Control Hub
 The control hub is a raspberry pi with a touch screen. The ui is made in pyhon and communicates with the nodes by I2C.
 
