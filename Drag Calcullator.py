import math
Sea_Level_Pressure = 101.325
Temperature_0 = 288.15
Sea_Level_Gravity_Acceleration = 9.80665
Adiabatic_Gradient = 0.0065
Ideal_Gas_Constant = 8.31447
Air_Molar_Mass = 0.0289664
Reentry_Angle = 45
Reentry_Velocity = 7000
Ship_Mass = 67824
Earth_Mass = 5.9736*math.pow(10,24)
Height = 6371000
Gravitation_Constant = 6.67408*math.pow(10,-11)
Drag_Coefficient = 0.42
Area = math.pow(2,2)*3.14

def Calculate_Temperature(Height):
    return Temperature_0 - (Adiabatic_Gradient*Height)

def Calculate_Pressure(Height):
    return 1000*Sea_Level_Pressure*math.pow((1-(2.25577*math.pow(10,-5)*(Height-6371000))),5.25588)
    #Error might be here

def Calculate_Density(Height):
    return (Calculate_Pressure(Height)*Air_Molar_Mass)/(Ideal_Gas_Constant*Calculate_Temperature(Height))
    #Or here

def Calculate_Drag(Height,Velocity,Area,Coefficient):
    return Coefficient*((Calculate_Density(Height)*math.pow(Velocity,2))/2)*Area

def Calculate_Gravitational_Force(Height, Mass, Earth_Mass):
    return (Earth_Mass*Ship_Mass*Gravitation_Constant)/math.pow(Height,2)
    
def Calculate_Resultant_Vector(Reentry_Angle, G, D):
    return math.sqrt(math.pow(G,2) + math.pow(D,2) - 2*G*D*math.cos(180-Reentry_Angle))
    
Grav = Calculate_Gravitational_Force(Height,Ship_Mass,Earth_Mass)
Drag = Calculate_Drag(Height,Reentry_Velocity,Area,Drag_Coefficient)
Res = Calculate_Resultant_Vector(Reentry_Angle,Grav,Drag)
Acc = Res/Ship_Mass
Acc2 = Drag/Ship_Mass

print(str(Drag) + " , " + str(Acc2))

print("Resultant_Force at T1: " + str(Res) + "N, Acceleration: " + str(Acc) + "m/s².")