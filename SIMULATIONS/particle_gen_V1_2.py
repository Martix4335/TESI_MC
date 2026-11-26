import numpy as np

#########################
### General Variables ###
#########################

x_sim_max=16  #cm
y_sim_max=11 #cm
x_max=15 #cm
y_max=10 #cm
h=70.5 #simulation plane's height in cm
h1=69.5 #hight of the first scintillator in cm
h2=0 #hight of the second scintillator in cm
size=14080

##################
### Functions  ###
##################

def pdf_azimuth(theta):
    """
    Probability distribution function of azimuthal angle

    Parameters
    ----------
    theta : float\n\t Given azimuthal angle

    Returns
    -------
    y : float\n\t Value of the PDF at given angle theta
    """
    
    y=3*(np.sin(theta))*(np.cos(theta))**2
    return y

def Phi(size):
    """
    Generates an array of random generated values of equatorial angles phi 
    given a uniform distribution

    Parameters
    ----------
    size : int\n\t Array size

    Returns
    -------
    Phi: ndarray\n\t Array of random generated values of phi
    """
    
    
    Phi=np.random.uniform(0, 2*np.pi,size)
    return Phi

def Theta(size):
    """
    Generates an array of random generated values of azimuthal angles theta 
    given a known probability distribution function, using rejection sampling
    sampling method

    Parameters
    ----------
    size : int\n\t Array size

    Returns
    -------
    Theta: ndarray\n\t Array of random generated values of theta
    """
    theta_array = []
    while len(theta_array)<size:
        theta=np.random.uniform(0,np.pi/2)
        u=np.random.uniform(0,4/np.pi)
        v=pdf_azimuth(theta)
        if u<=v:
            theta_array.append(theta)
        Theta=np.array(theta_array)
    return Theta
        
def particle_gen(x_sim_max,y_sim_max,h,size):
    
    """
    Generates particle's position and dirction on limited horizontal plane

    Parameters
    ----------
    x_max : float\n\t Simualtion area's half lenght\n
    y_max : float\n\t Simualtion area's half width\n
    h : float\n\t Simulation surface height\n
    size : int\n\t Array size

    Returns
    -------
    pos : ndarray\n\t Particle's position on simulation surface\n
    dir_vec : ndarray\n\t Particle's direction vector
    """
    
    x=np.random.uniform(-x_sim_max,x_sim_max,size)
    y=np.random.uniform(-y_sim_max,y_sim_max,size)
    z=h*np.ones(size)
    phi=Phi(size)
    theta=Theta(size)
    
    pos=np.array([x,y,z])
    dir_vec=-np.array([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)])

    return pos,dir_vec

####################
### Main Program ###
####################

pos, dir_vec = particle_gen(x_sim_max, y_sim_max, h, size) #generate positions and directions of particles

#Calculate scalar t* for travel lenght for the particle to arrive at the hight of the scintillators 
t1=(h-h1)/dir_vec[2] 
t2=(h-h2)/dir_vec[2]

#Checks if particle is inside the area of the scintillators, then gives trigger on a scintillator 
trigger1=np.logical_and(np.abs(pos[0]+dir_vec[0]*t2)<x_max, np.abs(pos[1]+dir_vec[1]*t1)<y_max)
trigger2=np.logical_and(np.abs(pos[0]+dir_vec[0]*t2)<x_max, np.abs(pos[1]+dir_vec[1]*t2)<y_max)

#Checks trigger on both scintillators
trigger=np.logical_and(trigger1, trigger2)

generated= np.size(trigger,0)
count=int(np.sum(trigger))

print("Generated: {0}\nCounted: {1}".format(generated,count))