1.5 mm shielding material 
9x9 cm2
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   1)   Z=100 cm                                           
INDICES=( 0, 0, 0, 1, 0)
Z-SHIFT=( 1.000000000000000E+02,   0)       
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   2)   Z=100.150 cm (1.50 mm thick layer)                          
INDICES=( 0, 0, 0, 1, 0)
Z-SHIFT=( 1.001500000000000E+02,   0)      
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   3)   Y=-4.5 cm                                    
INDICES=( 0, 0, 0, 0, 0)
     AY=( 1.000000000000000E+00,   0)       
     A0=( 0.450000000000000E+01,   0)       
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   4)   Y=+4.5 cm                                    
INDICES=( 0, 0, 0, 0, 0)
     AY=( 1.000000000000000E+00,   0)       
     A0=(-0.450000000000000E+01,   0)       
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   5)   X=-4.5 cm                                    
INDICES=( 0, 0, 0, 0, 0)
     AX=( 1.000000000000000E+00,   0)       
     A0=( 0.450000000000000E+01,   0)       
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (   6)   X=4.5 cm                                      
INDICES=( 0, 0, 0, 0, 0)
     AX=( 1.000000000000000E+00,   0)       
     A0=(-0.450000000000000E+01,   0)       
0000000000000000000000000000000000000000000000000000000000000000
BODY    (   1)   Layer 1 (material)                                     
MATERIAL(   1)
SURFACE (   1), SIDE POINTER=( 1)
SURFACE (   2), SIDE POINTER=(-1)
SURFACE (   3), SIDE POINTER=( 1)
SURFACE (   4), SIDE POINTER=(-1)
SURFACE (   5), SIDE POINTER=( 1)
SURFACE (   6), SIDE POINTER=(-1)
c
c                                              
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  13)   Z = 101 cm                                        
INDICES=( 0, 0, 0, 1, 0)
Z-SHIFT=( 1.010000000000000E+02,   0)       
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  14)   Z = 102 cm (detector 1 cm thick)                                        
INDICES=( 0, 0, 0, 1, 0)
Z-SHIFT=( 1.020000000000000E+02,   0)    
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  15)   X=-2 cm                                  
INDICES=( 0, 0, 0, 0, 0)
     AX=( 1.000000000000000E+00,   0)       
     A0=( 0.200000000000000E+01,   0)          
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  16)   X=2 cm                                  
INDICES=( 0, 0, 0, 0, 0)
     AX=( 1.000000000000000E+00,   0)       
     A0=(-0.200000000000000E+01,   0)          
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  17)   Y=-2 cm                                 
INDICES=( 0, 0, 0, 0, 0)
     AY=( 1.000000000000000E+00,   0)       
     A0=( 0.200000000000000E+01,   0)    
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  18)   Y=2 cm                                     
INDICES=( 0, 0, 0, 0, 0)
     AY=( 1.000000000000000E+00,   0)       
     A0=(-0.200000000000000E+01,   0)          
0000000000000000000000000000000000000000000000000000000000000000
BODY    (   2)  Air Detector, at 101 cm from the source, 1 cm from the textile shield                          
MATERIAL(   2)
SURFACE (  13), SIDE POINTER=( 1)
SURFACE (  14), SIDE POINTER=(-1)
SURFACE (  15), SIDE POINTER=( 1)
SURFACE (  16), SIDE POINTER=(-1)
SURFACE (  17), SIDE POINTER=( 1)
SURFACE (  18), SIDE POINTER=(-1)
c                                                                       
c    
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  39)   sphere diameter=400 
INDICES=( 1, 1, 1, 0,-1)
X-SCALE=( 2.000000000000000E+02,   0)
Y-SCALE=( 2.000000000000000E+02,   0)
Z-SCALE=( 2.000000000000000E+02,   0)
0000000000000000000000000000000000000000000000000000000000000000
BODY    (   3)  enclosure (air)
MATERIAL(   3)
BODY    (   1)
BODY    (   2)
SURFACE (  39), SIDE POINTER=(-1)                                                                                                 
0000000000000000000000000000000000000000000000000000000000000000
END      0000000000000000000000000000000000000000000000000000000