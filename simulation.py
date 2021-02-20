GlowScript 2.7 VPython
#The suspension rod is extending in the z axis with its axis vector being (0, 0, -1)
suspension_rod = cylinder(
pos=vector(0, 0, 0),
axis=vector(0, 0, (-0.1)),
radius=0.01,
color=vector(153/255, 153/255, 153/255), texture=textures.metal, vel=vector(0,0,0),
acc=vector(0,0,0), mass=0,
charge=0)
#The mass has a specific position, velocity, accleration and mass value
mass = sphere(
pos=vector((-0.00005), 0.374, 0), #The position changes according to the initial angle radius=0.05,
texture=textures.granite,
make_trail=True,
trail_type='curve',
retain=50,
interval=2,
vel=vector(0, 0, 0), #instantaneous velocity changes as accleration increases acc=vector(0, 0, 0), #instantaneous acceleration changes as force changes mass=0.40431,
charge=0)
L =
mass.pos - suspension_rod.pos
spring = helix( pos=suspension_rod.pos, axis=L,
radius=0.02,
coils=25, thickness=0.005, vel=vector(0,0,0), acc=vector(0,0,0), mass=0,
charge=0)
t=0
deltat = 1 / 240 #deltat is the time step g = 9.8 #accelration due to gravity
 32
Extended Essay Physics May 2022
k_s = 49.78 #spring constant
L_0 = 0.374 # intial length
LHat = norm(L) #unit vector in the direction of the spring
s = (mag(L)) - L_0 # extension of the spring
FGrav = vector(0, (-mass.mass * g), 0) #gravtiational force in downards direction while t <= 10:
rate(400 , wait)
FSpring = (-k_s * s) * LHat #spring force in the radial direction in accordance with the unit vector
FNet = FGrav + FSpring #net force calulated
mass.vel = mass.vel + (FNet / mass.mass) * deltat #accleration is found using the net force and the value of a is used to find the instantaneous velocity
mass.pos = mass.pos + mass.vel * deltat #the velocity is used to find the displacement or the position of the mass
L = mass.pos - spring.pos #updating the vector for the spring LHat = norm(L) #hence also updating the unit vector
s = (mag(L)) - L_0 #updating the extension
spring.axis = L
t = t + deltat
if mass.pos.x <= 0.003 and mass.pos.x >= -0.003: #checking when the spring crosses the center point
print(mass.pos.y) #printing its position