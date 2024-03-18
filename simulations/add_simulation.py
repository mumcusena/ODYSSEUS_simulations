import os
import random
import re
import shutil

# number of the simulations to be added
NUM_SIMULATION = 100
current_path = os.getcwd()

for i in range(1):
    random_energy_level = "120kV/x120kV_1" if random.randint(1, 2) == 1 else "100kV/RQR8_100_1"

    simulations_path = os.path.join(current_path, "simulations/{}".format(random_energy_level))

    random_simulation_number = random.randint(1, 84)
    simulation_list = os.listdir(simulations_path)

    lucky_simulation = simulation_list[random_simulation_number]
    # print(lucky_simulation)

    dummy = lucky_simulation.split("_")
    dummy_string = []
    for i in range(len(dummy)) :
        if i == (len(dummy)-2):
            dummy_string.append("oneL140")
            continue
        dummy_string.append(dummy[i])

    test = '_'.join(dummy_string)

    if(test in os.listdir(simulations_path)):
        continue
    
    parts = lucky_simulation.split("_")
    if(len(parts) == 6):
        poly_ratio = parts[3]
        element = parts[5]
    else: 
        poly_ratio = parts[2]
        element = parts[4]

    simulation_140 = "{}_{}_oneL140_{}".format(random_energy_level[6:] ,poly_ratio, element)
    simulation_150 = "{}_{}_oneL150_{}".format(random_energy_level[6:] ,poly_ratio, element)
    simulation_200 = "{}_{}_oneL200_{}".format(random_energy_level[6:] ,poly_ratio, element)
    simulation_250 = "{}_{}_oneL250_{}".format(random_energy_level[6:] ,poly_ratio, element)
    os.mkdir(os.path.join(simulations_path, simulation_140))
    os.mkdir(os.path.join(simulations_path, simulation_150))
    os.mkdir(os.path.join(simulations_path, simulation_200))
    os.mkdir(os.path.join(simulations_path, simulation_250))

    spc_file = random_energy_level[:-2]
    spc_file = spc_file[6:]
    print(spc_file)

    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "Aire.mat")), os.path.join(simulations_path, simulation_140))
    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "penEasy.x")), os.path.join(simulations_path, simulation_140))
    shutil.copy(os.path.join(simulations_path, "{}/{}.spc".format(lucky_simulation, spc_file)), os.path.join(simulations_path, simulation_140))
    os.chdir(os.path.join(simulations_path, simulation_140))
    with open('penEasy.in', 'w') as fp:
                        fp.write("# >>>> CONFIG FILE FOR penEasy >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n#\n# CASE DESCRIPTION:\n#   Sample config file adapted to the example described in the README\n#   file. Before editing this file, read carefully the instructions\n#   provided here after the data sections and in the README file.\n#\n# LAST UPDATE:\n#   2015-05-26 by JS\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# GENERAL INSTRUCTIONS\n#\n# * Lines starting with a '#' (in column 1) and blank lines are\n#   comments. Comments are NOT allowed inside data sections.\n#\n# * Do not change the order in which sections appear, neither the order\n#   of data fields in each section.\n#\n# * Each data section has a version number of the form yyyy-mm-dd that is\n#   written in the corresponding section title. Should an incorrect\n#   version be introduced an error message would be issued and the\n#   execution halted.\n#\n# * Character strings (e.g. file names) are introduced in free-format\n#   style, that is, leading and trailing blanks are allowed. Their\n#   maximum extension (except when noted) is 80 characters and they must\n#   not contain blanks. Thus, for instance, 'stainless steel' should be\n#   introduced as 'stainlessSteel' or 'stainless_Steel'.\n#\n# * Most syntax errors can be easily identified by looking for error\n#   messages or inconsistencies within the last lines of penEasy output.\n#   It is always a good idea to check the output to make sure that the\n#   information written after processing each section coincides with what\n#   is expected from the input.\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION CONFIG\n#\n# * Details on the simulation configuration are provided with their\n#   documentation (see ~/documentation/*).\n\n[SECTION CONFIG v.2013-03-18]\n 4.0e9             NUMBER OF HISTORIES (1.0e15 MAX)\n 20000             ALLOTTED TIME (s) (+ FOR REAL TIME; - FOR CPU TIME)\n 100.0             UPDATE INTERVAL (s)\n 1  1              INITIAL RANDOM SEEDS\n -                 SEEDS FILE; MUST ENTER SEEDS=0,0 TO APPLY\n -                 RESTART FILE; MUST ENTER SEEDS=-1,-1 TO APPLY\n penEasy.dmp       OUTPUT DUMP FILE; ENTER '-' FOR 'NO DUMP'\n 1200.0            INTERVAL BETWEEN DUMPS (s)\n[END OF CONFIG SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SOURCE SECTIONS\n#\n# * Details on the features and configuration of each source model are\n#   provided with their documentation (see ~/documentation/*).\n#   Notice that there must be one and only one active (status ON) source model.\n\n[SECTION SOURCE BOX ISOTROPIC GAUSS SPECTRUM v.2014-12-21]\n ON                              STATUS (ON or OFF)\n 2                               PARTICLE TYPE (1=ELECTRON, 2=PHOTON, 3=POSITRON)\n  SUBSECTION FOR PHOTON POLARIZATION:\n 0                               ACTIVATE PHOTON POLARIZATION PHYSICS (0=NO, 1=YES)\n 0.0 0.0 0.0                     STOKES PARAMETERS (UNUSED IF ACTIVATE POLARIZATION=0)\n  SUBSECTION FOR PARTICLE POSITION:\n 0.0  0.0  0.0                   COORDINATES (cm) OF BOX CENTER\n 0.0  0.0  0.0                   BOX SIDES (cm)\n 0.0  0.0                        FWHMs (cm) OF GAUSSIAN X,Y DISTRIBUTIONS\n 0.0  0.0  0.0                   EULER ANGLES [OMEGA,THETA,PHI](deg) FOR BOX ROTATION Rz(PHI).Ry(THETA).Rz(OMEGA).r\n 0.0  0.0  0.0                   TRANSLATION [DX,DY,DZ](cm) OF BOX CENTER POSITION\n 0                               SOURCE MATERIAL (0=DON'T CARE, >0 FOR LOCAL SOURCE, <0 FOR IN-FIELD BEAM)\n  SUBSECTION FOR PARTICLE DIRECTION:\n 0.0  0.0  1.0                   DIRECTION VECTOR; NO NEED TO NORMALIZE\n 0.0 2.57                        DIRECTION POLAR ANGLE INTERVAL [THETA0,THETA1], BOTH VALUES IN [0,180]deg\n 0.0 360.0                       DIRECTION AZIMUTHAL ANGLE INTERVAL PHI0 IN [0,360)deg AND DeltaPHI IN [0,360]deg\n 1                               APPLY ALSO TO DIRECTION THE ROTATION USED FOR BOX POSITION (0=NO, 1=YES)\n  SUBSECTION FOR PARTICLE ENERGY:\n {}.spc                    ENERGY SPECTRUM FILE NAME; ENTER '-' TO ENTER SPECTRUM IN NEXT LINES\n 0.0                             FWHM(eV) OF GAUSSIAN ENERGY DISTRIB. [NOTE FWHM=SIGMA*sqrt(8*ln(2))]\n[END OF BIGS SECTION]\n\n[SECTION SOURCE PHASE SPACE FILE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0                               PSF FORMAT (0=STANDARD penEasy ASCII, 1=IAEA BINARY)\n particles.psf                   PSF FILENAME, REMOVE EXTENSION IF PSF FORMAT=1\n 1                               SPLITTING FACTOR\n 0.0  0.0  0.0                   EULER ANGLES [Rz,Ry,Rz](deg) TO ROTATE POSITION AND DIRECTION\n 0.0  0.0  0.0                   TRANSLATION [DX,DY,DZ](cm) OF POSITION\n 1                               VALIDATE BEFORE SIMULATION (1=YES, MAY TAKE A WHILE; 0=NO)\n 0.000e0                         MAX PSF ENERGY (eV) (UNUSED IF VALIDATE=1 OR IAEA FORMAT; ADD 1023 keV FOR e+)\n[END OF SPSF SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION PENGEOM+PENVOX\n#\n# * Enter either: (i) a file name in the QUADRICS FILE field and a dash '-' in\n#   the VOXELS FILE field if you want to define only a quadric geometry model;\n#   (ii) a file name in the VOXELS FILE field and a dash '-' in the QUADRICS\n#   FILE field if you want to define only a voxelized geometry model; or (iii)\n#   both a quadrics and a voxelized file names in the corresponding fields if\n#   you want to define a combination of overlapping quadrics and voxelized models.\n#\n# * The TRANSPARENT QUADRIC MAT and GRANULARITY field are used only if both a\n#   quadric and a voxel geometries are defined. Otherwise they are irrelevant.\n#\n# * Details on the use and configuration of these geometry models are provided\n#   in the documentation (please refer to ~/documentation/*).\n\n[SECTION PENGEOM+PENVOX v.2009-06-15]\n {}.geo                     QUADRICS FILE NAME, USE '-' IF NONE\n -                               VOXELS FILE NAME, USE '-' IF NONE\n 1                               TRANSPARENT QUADRIC MAT (USED ONLY IF QUAD&VOX)\n 10                              GRANULARITY TO SCAN VOXELS (USED ONLY IF QUAD&VOX)\n[END OF GEO SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION PENELOPE\n#\n# * Write one line of data per defined material. Each line starts with\n#   the material index (MAT#), which should be an integer starting from 1.\n#   Set MAT# to zero in the last line to denote the end of the list.\n#\n# * Use 20 characters at most to introduce the material data file name.\n#   Blanks or special characters are not allowed in file names. Thus,\n#   instead of \"stainless steel.mat\" use \"stainlessSteel.mat\".\n#\n# * If, for a certain material, the transport parameters after the file\n#   name are left empty, then they are set automatically as follows:\n#     - Eabs for charged particles are set to 1% of the\n#       initial source energy (E), with the limiting values of 50 eV\n#       (min) and 1 MeV (max).\n#     - Eabs for photons is set to 0.1% E with the limiting values of 50\n#       eV and 1 MeV.\n#     - C1 and C2 are both set to 0.1.\n#     - WCC is set to min(Eabs(e-),1% E)\n#     - WCR is set to min(Eabs(phot),0.1% E).\n#     - DSMAX is set to infinity.\n#\n# * Do not remove the line containing the table header \"MAT# FILE...\".\n\n[SECTION PENELOPE v.2009-10-01]\n MAT# FILE___(max 20 char) EABS(e-)  EABS(ph)  EABS(e+)  C1    C2    WCC      WCR      DSMAX   COMMENTS\n  1   {}.mat           100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e30  material\n  2   Aire.mat            100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e-1  air detector\n  3   Aire.mat            100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e30  air enclosure\n  0 (SET MAT=0 TO END LIST)\n[END OF PEN SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR THE TALLY SECTIONS\n#\n# * Details on the features and configuration of each tally are provided\n#   with their documentation (see ~/documentation/*.txt).\n#\n# * The required RELATIVE UNCERTAINTY that is specified for each tally\n#   (except for those that do not have an associated uncertainty, e.g. a\n#   phase-space file) is used as a condition to stop the simulation. Only\n#   when the requested relative uncertainties of *all* the tallies have\n#   been attained the uncertainty condition is considered fulfilled.\n#   Recall that the simulation can also be halted because the allotted\n#   time or the number of histories requested have been reached. Setting\n#   the RELATIVE UNCERTAINTY of all tallies to zero will prevent the\n#   execution from stopping for this cause.\n#\n# * Note for advanced users: when a certain tally scores nothing (i.e.\n#   zero) the corresponding REPORT routine reports 0% uncertainty but, at\n#   the same time, it reports that the requested uncertainty has not been\n#   reached, irrespective of the value introduced in the config file.\n#   This is to prevent the simulation from being stopped by a deceptive\n#   impression of accuracy in highly inefficient simulations, where the\n#   score and its standard deviation after a short period of time can be\n#   null.\n\n[SECTION TALLY VOXEL DOSE v.2014-12-27]\n OFF                             STATUS (ON or OFF)\n 0  0                            ROI MIN,MAX X-INDEX (0 0 FOR ALL VOXELS)\n 0  0                            ROI MIN,MAX Y-INDEX (0 0 FOR ALL VOXELS)\n 0  0                            ROI MIN,MAX Z-INDEX (0 0 FOR ALL VOXELS)\n 0                               PRINT VOXELS MASS IN REPORT (1=YES,0=NO)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO,-1=NO&BINARYFORMAT)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF VDD SECTION]\n\n[SECTION TALLY SPATIAL DOSE DISTRIB v.2009-06-15]\n OFF                              STATUS (ON or OFF)\n 0.0  0.0   0                    XMIN,XMAX(cm),NXBIN (0 FOR DX=infty)\n 0.0  0.0   0                    YMIN,YMAX(cm),NYBIN (0 FOR DY=infty)\n 0.0  7.0   40                   ZMIN,ZMAX(cm),NZBIN (0 FOR DZ=infty)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO,-1=NO&BINARYFORMAT)\n 1.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF SDD SECTION]\n\n[SECTION TALLY CYLINDRICAL DOSE DISTRIB v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0.0  8.0  80                    RMIN,RMAX(cm),NRBIN (>0)\n 0.0  7.0  40                    ZMIN,ZMAX(cm),NZBIN (0 FOR DZ=infty)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF CDD SECTION]\n\n[SECTION TALLY SPHERICAL DOSE DISTRIB v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0.0  1.0  50                    RMIN,RMAX(cm),NRBIN (>0)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF SPD SECTION]\n\n[SECTION TALLY ENERGY DEPOSITION v.2012-06-01]\n ON                              STATUS (ON or OFF)\n 3                               DETECTION MATERIAL\n 2.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF EDP SECTION]\n\n[SECTION TALLY PULSE HEIGHT SPECTRUM v.2012-06-01]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0.0  1.0e9  100                 EMIN,EMAX(eV), No. OF E BINS\n 0.0  0.0                        A(eV^2),B(eV) FOR GAUSSIAN CONVOLUTION FWHM[eV]=sqrt(A+B*E[eV])\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PHS SECTION]\n\n[SECTION TALLY PIXELATED IMAGING DETECTOR v.2015-02-06]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0                               FILTER PHOTON INTERACTION (0=NOFILTER, -1=UNSCATTERED, 1=RAYLEIGH, 2=COMPTON, 3=SECONDARIES, 9=MULTISCATTERED)\n 0   100                         X-PIXEL SIZE(cm), No. X-PIXELS (ENTER 0 IN EITHER FIELD FOR AUTO)\n 0   100                         Y-PIXEL SIZE(cm), No. Y-PIXELS (ENTER 0 IN EITHER FIELD FOR AUTO)\n 1                               DETECTION MODE (1=ENERGY INTEGRATING, 2=PHOTON COUNTING, 3=PHOTON ENERGY DISCRIMINATING aka SPECTRUM)\n 1.0e3                           ENERGY DEPOSITION THRESHOLD (eV) FOR MODE=2 (IGNORED FOR OTHER MODES)\n 0.0  1.0e9  100                 EMIN,EMAX(eV), No. OF E BINS FOR MODE=3 (IGNORED FOR OTHER MODES)\n 0.0  0.0                        ENERGY RESOLUTION, ENTER A(eV^2),B(eV) FOR A GAUSSIAN WITH FWHM[eV]=sqrt(A+B*E[eV])\n 1                               REPORT FORMAT (1=COLUMNAR, 2=MATRIX, 3=BINARY)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PID SECTION]\n\n[SECTION TALLY FLUENCE TRACK LENGTH v.2012-06-01]\n ON                              STATUS (ON or OFF)\n 3                               DETECTION MATERIAL\n 10.0e3  80.0e3  70              EMIN,EMAX(eV), No. OF E BINS, APPEND 'LOG' FOR A LOG SCALE\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF FTL SECTION]\n\n[SECTION TALLY PHASE SPACE FILE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0                               PSF FORMAT (0=STANDARD penEasy ASCII, 1=IAEA BINARY)\n 1                               DETECTION MATERIAL (MUST BE A PERFECT ABSORBENT, EABS=+infty)\n output.psf                      PSF FILENAME, REMOVE EXTENSION IF FORMAT=1\n[END OF PSF SECTION]\n\n[SECTION TALLY PARTICLE CURRENT SPECTRUM v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0.0 1.0e9   100                 EMIN,EMAX(eV), No. OF E BINS\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PCS SECTION]\n\n[SECTION TALLY PARTICLE TRACK STRUCTURE v.2009-06-15]\n OFF                              STATUS (ON or OFF)\n 100                             NUMBER OF HISTORIES TO DISPLAY (~100 RECOMMENDED)\n[END OF PTS SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR VARIANCE-REDUCTION SECTIONS\n#\n# * Details on the features and configuration of each VR technique are provided\n#   with their documentation (see ~/documentation/*.txt).\n\n[SECTION INTERACTION FORCING v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1.0                             DON'T APPLY BELOW THIS STATISTICAL WEIGHT\n MAT  KPAR  ICOL  FORCING  (SET MAT=-1 TO END LIST)\n -1   0     0     1.0\n[END OF VRIF SECTION]\n\n[SECTION SPLITTING v.2015-05-30]\n OFF                             STATUS (ON or OFF)\n 1.0                             WGHTMIN, DO NOT SPLIT BELOW THIS STATISTICAL WEIGHT\n 1                               SPLITTING MATERIAL\n 1                               SPLITTING MODE (1=SIMPLE; 2=ROTATIONAL; 3=XY)\n 1                               SPLITTING FACTOR, IGNORED FOR MODE=3\n 0.0  0.0  0.0                   EULER ANGLES [Rz,Ry,Rz](deg), IGNORED FOR MODE=1\n 0.0  0.0  0.0                   SHIFT (cm), IGNORED FOR MODE=1\n 0                               SIGN OF W ('+', '-' OR '0'=BOTH), IGNORED FOR MODE=1\n 0.0  360.0                      AZIMUTHAL INTERVAL PHI0 IN [0,360)deg AND DeltaPHI IN (0,360]deg, USED ONLY IF MODE=2\n[END OF VRS SECTION]\n\n[SECTION RUSSIAN ROULETTE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1.0                             WGHTMAX, DO NOT PLAY ABOVE THIS STATISTICAL WEIGHT\n 1                               RUSSIAN ROULETTE MATERIAL\n 1.0                             SURVIVAL PROBABILITY\n[END OF VRRR SECTION]\n\n\n# >>>> END OF FILE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" \
                                 .format("{}.spc".format(spc_file), "oneL140", element))
    
    with open('oneL140.geo', 'w') as f:
            f.write("""0.3 mm shielding material 
                9x9 cm2
                0000000000000000000000000000000000000000000000000000000000000000
                SURFACE (   1)   Z=100 cm                                           
                INDICES=( 0, 0, 0, 1, 0)
                Z-SHIFT=( 1.000000000000000E+02,   0)       
                0000000000000000000000000000000000000000000000000000000000000000
                SURFACE (   2)   Z=100.140 cm (1.40 mm thick layer)                          
                INDICES=( 0, 0, 0, 1, 0)
                Z-SHIFT=( 1.001400000000000E+02,   0)      
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
                END      0000000000000000000000000000000000000000000000000000000""")

    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "Aire.mat")), os.path.join(simulations_path, simulation_150))
    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "penEasy.x")), os.path.join(simulations_path, simulation_150))
    shutil.copy(os.path.join(simulations_path, "{}/{}.spc".format(lucky_simulation, spc_file)), os.path.join(simulations_path, simulation_150))
    with open('penEasy.in', 'w') as fp:
                        fp.write("# >>>> CONFIG FILE FOR penEasy >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n#\n# CASE DESCRIPTION:\n#   Sample config file adapted to the example described in the README\n#   file. Before editing this file, read carefully the instructions\n#   provided here after the data sections and in the README file.\n#\n# LAST UPDATE:\n#   2015-05-26 by JS\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# GENERAL INSTRUCTIONS\n#\n# * Lines starting with a '#' (in column 1) and blank lines are\n#   comments. Comments are NOT allowed inside data sections.\n#\n# * Do not change the order in which sections appear, neither the order\n#   of data fields in each section.\n#\n# * Each data section has a version number of the form yyyy-mm-dd that is\n#   written in the corresponding section title. Should an incorrect\n#   version be introduced an error message would be issued and the\n#   execution halted.\n#\n# * Character strings (e.g. file names) are introduced in free-format\n#   style, that is, leading and trailing blanks are allowed. Their\n#   maximum extension (except when noted) is 80 characters and they must\n#   not contain blanks. Thus, for instance, 'stainless steel' should be\n#   introduced as 'stainlessSteel' or 'stainless_Steel'.\n#\n# * Most syntax errors can be easily identified by looking for error\n#   messages or inconsistencies within the last lines of penEasy output.\n#   It is always a good idea to check the output to make sure that the\n#   information written after processing each section coincides with what\n#   is expected from the input.\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION CONFIG\n#\n# * Details on the simulation configuration are provided with their\n#   documentation (see ~/documentation/*).\n\n[SECTION CONFIG v.2013-03-18]\n 4.0e9             NUMBER OF HISTORIES (1.0e15 MAX)\n 20000             ALLOTTED TIME (s) (+ FOR REAL TIME; - FOR CPU TIME)\n 100.0             UPDATE INTERVAL (s)\n 1  1              INITIAL RANDOM SEEDS\n -                 SEEDS FILE; MUST ENTER SEEDS=0,0 TO APPLY\n -                 RESTART FILE; MUST ENTER SEEDS=-1,-1 TO APPLY\n penEasy.dmp       OUTPUT DUMP FILE; ENTER '-' FOR 'NO DUMP'\n 1200.0            INTERVAL BETWEEN DUMPS (s)\n[END OF CONFIG SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SOURCE SECTIONS\n#\n# * Details on the features and configuration of each source model are\n#   provided with their documentation (see ~/documentation/*).\n#   Notice that there must be one and only one active (status ON) source model.\n\n[SECTION SOURCE BOX ISOTROPIC GAUSS SPECTRUM v.2014-12-21]\n ON                              STATUS (ON or OFF)\n 2                               PARTICLE TYPE (1=ELECTRON, 2=PHOTON, 3=POSITRON)\n  SUBSECTION FOR PHOTON POLARIZATION:\n 0                               ACTIVATE PHOTON POLARIZATION PHYSICS (0=NO, 1=YES)\n 0.0 0.0 0.0                     STOKES PARAMETERS (UNUSED IF ACTIVATE POLARIZATION=0)\n  SUBSECTION FOR PARTICLE POSITION:\n 0.0  0.0  0.0                   COORDINATES (cm) OF BOX CENTER\n 0.0  0.0  0.0                   BOX SIDES (cm)\n 0.0  0.0                        FWHMs (cm) OF GAUSSIAN X,Y DISTRIBUTIONS\n 0.0  0.0  0.0                   EULER ANGLES [OMEGA,THETA,PHI](deg) FOR BOX ROTATION Rz(PHI).Ry(THETA).Rz(OMEGA).r\n 0.0  0.0  0.0                   TRANSLATION [DX,DY,DZ](cm) OF BOX CENTER POSITION\n 0                               SOURCE MATERIAL (0=DON'T CARE, >0 FOR LOCAL SOURCE, <0 FOR IN-FIELD BEAM)\n  SUBSECTION FOR PARTICLE DIRECTION:\n 0.0  0.0  1.0                   DIRECTION VECTOR; NO NEED TO NORMALIZE\n 0.0 2.57                        DIRECTION POLAR ANGLE INTERVAL [THETA0,THETA1], BOTH VALUES IN [0,180]deg\n 0.0 360.0                       DIRECTION AZIMUTHAL ANGLE INTERVAL PHI0 IN [0,360)deg AND DeltaPHI IN [0,360]deg\n 1                               APPLY ALSO TO DIRECTION THE ROTATION USED FOR BOX POSITION (0=NO, 1=YES)\n  SUBSECTION FOR PARTICLE ENERGY:\n {}.spc                    ENERGY SPECTRUM FILE NAME; ENTER '-' TO ENTER SPECTRUM IN NEXT LINES\n 0.0                             FWHM(eV) OF GAUSSIAN ENERGY DISTRIB. [NOTE FWHM=SIGMA*sqrt(8*ln(2))]\n[END OF BIGS SECTION]\n\n[SECTION SOURCE PHASE SPACE FILE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0                               PSF FORMAT (0=STANDARD penEasy ASCII, 1=IAEA BINARY)\n particles.psf                   PSF FILENAME, REMOVE EXTENSION IF PSF FORMAT=1\n 1                               SPLITTING FACTOR\n 0.0  0.0  0.0                   EULER ANGLES [Rz,Ry,Rz](deg) TO ROTATE POSITION AND DIRECTION\n 0.0  0.0  0.0                   TRANSLATION [DX,DY,DZ](cm) OF POSITION\n 1                               VALIDATE BEFORE SIMULATION (1=YES, MAY TAKE A WHILE; 0=NO)\n 0.000e0                         MAX PSF ENERGY (eV) (UNUSED IF VALIDATE=1 OR IAEA FORMAT; ADD 1023 keV FOR e+)\n[END OF SPSF SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION PENGEOM+PENVOX\n#\n# * Enter either: (i) a file name in the QUADRICS FILE field and a dash '-' in\n#   the VOXELS FILE field if you want to define only a quadric geometry model;\n#   (ii) a file name in the VOXELS FILE field and a dash '-' in the QUADRICS\n#   FILE field if you want to define only a voxelized geometry model; or (iii)\n#   both a quadrics and a voxelized file names in the corresponding fields if\n#   you want to define a combination of overlapping quadrics and voxelized models.\n#\n# * The TRANSPARENT QUADRIC MAT and GRANULARITY field are used only if both a\n#   quadric and a voxel geometries are defined. Otherwise they are irrelevant.\n#\n# * Details on the use and configuration of these geometry models are provided\n#   in the documentation (please refer to ~/documentation/*).\n\n[SECTION PENGEOM+PENVOX v.2009-06-15]\n {}.geo                     QUADRICS FILE NAME, USE '-' IF NONE\n -                               VOXELS FILE NAME, USE '-' IF NONE\n 1                               TRANSPARENT QUADRIC MAT (USED ONLY IF QUAD&VOX)\n 10                              GRANULARITY TO SCAN VOXELS (USED ONLY IF QUAD&VOX)\n[END OF GEO SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION PENELOPE\n#\n# * Write one line of data per defined material. Each line starts with\n#   the material index (MAT#), which should be an integer starting from 1.\n#   Set MAT# to zero in the last line to denote the end of the list.\n#\n# * Use 20 characters at most to introduce the material data file name.\n#   Blanks or special characters are not allowed in file names. Thus,\n#   instead of \"stainless steel.mat\" use \"stainlessSteel.mat\".\n#\n# * If, for a certain material, the transport parameters after the file\n#   name are left empty, then they are set automatically as follows:\n#     - Eabs for charged particles are set to 1% of the\n#       initial source energy (E), with the limiting values of 50 eV\n#       (min) and 1 MeV (max).\n#     - Eabs for photons is set to 0.1% E with the limiting values of 50\n#       eV and 1 MeV.\n#     - C1 and C2 are both set to 0.1.\n#     - WCC is set to min(Eabs(e-),1% E)\n#     - WCR is set to min(Eabs(phot),0.1% E).\n#     - DSMAX is set to infinity.\n#\n# * Do not remove the line containing the table header \"MAT# FILE...\".\n\n[SECTION PENELOPE v.2009-10-01]\n MAT# FILE___(max 20 char) EABS(e-)  EABS(ph)  EABS(e+)  C1    C2    WCC      WCR      DSMAX   COMMENTS\n  1   {}.mat           100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e30  material\n  2   Aire.mat            100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e-1  air detector\n  3   Aire.mat            100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e30  air enclosure\n  0 (SET MAT=0 TO END LIST)\n[END OF PEN SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR THE TALLY SECTIONS\n#\n# * Details on the features and configuration of each tally are provided\n#   with their documentation (see ~/documentation/*.txt).\n#\n# * The required RELATIVE UNCERTAINTY that is specified for each tally\n#   (except for those that do not have an associated uncertainty, e.g. a\n#   phase-space file) is used as a condition to stop the simulation. Only\n#   when the requested relative uncertainties of *all* the tallies have\n#   been attained the uncertainty condition is considered fulfilled.\n#   Recall that the simulation can also be halted because the allotted\n#   time or the number of histories requested have been reached. Setting\n#   the RELATIVE UNCERTAINTY of all tallies to zero will prevent the\n#   execution from stopping for this cause.\n#\n# * Note for advanced users: when a certain tally scores nothing (i.e.\n#   zero) the corresponding REPORT routine reports 0% uncertainty but, at\n#   the same time, it reports that the requested uncertainty has not been\n#   reached, irrespective of the value introduced in the config file.\n#   This is to prevent the simulation from being stopped by a deceptive\n#   impression of accuracy in highly inefficient simulations, where the\n#   score and its standard deviation after a short period of time can be\n#   null.\n\n[SECTION TALLY VOXEL DOSE v.2014-12-27]\n OFF                             STATUS (ON or OFF)\n 0  0                            ROI MIN,MAX X-INDEX (0 0 FOR ALL VOXELS)\n 0  0                            ROI MIN,MAX Y-INDEX (0 0 FOR ALL VOXELS)\n 0  0                            ROI MIN,MAX Z-INDEX (0 0 FOR ALL VOXELS)\n 0                               PRINT VOXELS MASS IN REPORT (1=YES,0=NO)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO,-1=NO&BINARYFORMAT)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF VDD SECTION]\n\n[SECTION TALLY SPATIAL DOSE DISTRIB v.2009-06-15]\n OFF                              STATUS (ON or OFF)\n 0.0  0.0   0                    XMIN,XMAX(cm),NXBIN (0 FOR DX=infty)\n 0.0  0.0   0                    YMIN,YMAX(cm),NYBIN (0 FOR DY=infty)\n 0.0  7.0   40                   ZMIN,ZMAX(cm),NZBIN (0 FOR DZ=infty)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO,-1=NO&BINARYFORMAT)\n 1.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF SDD SECTION]\n\n[SECTION TALLY CYLINDRICAL DOSE DISTRIB v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0.0  8.0  80                    RMIN,RMAX(cm),NRBIN (>0)\n 0.0  7.0  40                    ZMIN,ZMAX(cm),NZBIN (0 FOR DZ=infty)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF CDD SECTION]\n\n[SECTION TALLY SPHERICAL DOSE DISTRIB v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0.0  1.0  50                    RMIN,RMAX(cm),NRBIN (>0)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF SPD SECTION]\n\n[SECTION TALLY ENERGY DEPOSITION v.2012-06-01]\n ON                              STATUS (ON or OFF)\n 3                               DETECTION MATERIAL\n 2.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF EDP SECTION]\n\n[SECTION TALLY PULSE HEIGHT SPECTRUM v.2012-06-01]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0.0  1.0e9  100                 EMIN,EMAX(eV), No. OF E BINS\n 0.0  0.0                        A(eV^2),B(eV) FOR GAUSSIAN CONVOLUTION FWHM[eV]=sqrt(A+B*E[eV])\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PHS SECTION]\n\n[SECTION TALLY PIXELATED IMAGING DETECTOR v.2015-02-06]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0                               FILTER PHOTON INTERACTION (0=NOFILTER, -1=UNSCATTERED, 1=RAYLEIGH, 2=COMPTON, 3=SECONDARIES, 9=MULTISCATTERED)\n 0   100                         X-PIXEL SIZE(cm), No. X-PIXELS (ENTER 0 IN EITHER FIELD FOR AUTO)\n 0   100                         Y-PIXEL SIZE(cm), No. Y-PIXELS (ENTER 0 IN EITHER FIELD FOR AUTO)\n 1                               DETECTION MODE (1=ENERGY INTEGRATING, 2=PHOTON COUNTING, 3=PHOTON ENERGY DISCRIMINATING aka SPECTRUM)\n 1.0e3                           ENERGY DEPOSITION THRESHOLD (eV) FOR MODE=2 (IGNORED FOR OTHER MODES)\n 0.0  1.0e9  100                 EMIN,EMAX(eV), No. OF E BINS FOR MODE=3 (IGNORED FOR OTHER MODES)\n 0.0  0.0                        ENERGY RESOLUTION, ENTER A(eV^2),B(eV) FOR A GAUSSIAN WITH FWHM[eV]=sqrt(A+B*E[eV])\n 1                               REPORT FORMAT (1=COLUMNAR, 2=MATRIX, 3=BINARY)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PID SECTION]\n\n[SECTION TALLY FLUENCE TRACK LENGTH v.2012-06-01]\n ON                              STATUS (ON or OFF)\n 3                               DETECTION MATERIAL\n 10.0e3  80.0e3  70              EMIN,EMAX(eV), No. OF E BINS, APPEND 'LOG' FOR A LOG SCALE\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF FTL SECTION]\n\n[SECTION TALLY PHASE SPACE FILE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0                               PSF FORMAT (0=STANDARD penEasy ASCII, 1=IAEA BINARY)\n 1                               DETECTION MATERIAL (MUST BE A PERFECT ABSORBENT, EABS=+infty)\n output.psf                      PSF FILENAME, REMOVE EXTENSION IF FORMAT=1\n[END OF PSF SECTION]\n\n[SECTION TALLY PARTICLE CURRENT SPECTRUM v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0.0 1.0e9   100                 EMIN,EMAX(eV), No. OF E BINS\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PCS SECTION]\n\n[SECTION TALLY PARTICLE TRACK STRUCTURE v.2009-06-15]\n OFF                              STATUS (ON or OFF)\n 100                             NUMBER OF HISTORIES TO DISPLAY (~100 RECOMMENDED)\n[END OF PTS SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR VARIANCE-REDUCTION SECTIONS\n#\n# * Details on the features and configuration of each VR technique are provided\n#   with their documentation (see ~/documentation/*.txt).\n\n[SECTION INTERACTION FORCING v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1.0                             DON'T APPLY BELOW THIS STATISTICAL WEIGHT\n MAT  KPAR  ICOL  FORCING  (SET MAT=-1 TO END LIST)\n -1   0     0     1.0\n[END OF VRIF SECTION]\n\n[SECTION SPLITTING v.2015-05-30]\n OFF                             STATUS (ON or OFF)\n 1.0                             WGHTMIN, DO NOT SPLIT BELOW THIS STATISTICAL WEIGHT\n 1                               SPLITTING MATERIAL\n 1                               SPLITTING MODE (1=SIMPLE; 2=ROTATIONAL; 3=XY)\n 1                               SPLITTING FACTOR, IGNORED FOR MODE=3\n 0.0  0.0  0.0                   EULER ANGLES [Rz,Ry,Rz](deg), IGNORED FOR MODE=1\n 0.0  0.0  0.0                   SHIFT (cm), IGNORED FOR MODE=1\n 0                               SIGN OF W ('+', '-' OR '0'=BOTH), IGNORED FOR MODE=1\n 0.0  360.0                      AZIMUTHAL INTERVAL PHI0 IN [0,360)deg AND DeltaPHI IN (0,360]deg, USED ONLY IF MODE=2\n[END OF VRS SECTION]\n\n[SECTION RUSSIAN ROULETTE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1.0                             WGHTMAX, DO NOT PLAY ABOVE THIS STATISTICAL WEIGHT\n 1                               RUSSIAN ROULETTE MATERIAL\n 1.0                             SURVIVAL PROBABILITY\n[END OF VRRR SECTION]\n\n\n# >>>> END OF FILE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" \
                                 .format("{}.spc".format(spc_file), "oneL150", element))
    
    with open('oneL150.geo', 'w') as f:
            f.write("""0.3 mm shielding material 
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
                END      0000000000000000000000000000000000000000000000000000000""")

    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "Aire.mat")), os.path.join(simulations_path, simulation_200))
    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "penEasy.x")), os.path.join(simulations_path, simulation_200))
    shutil.copy(os.path.join(simulations_path, "{}/{}.spc".format(lucky_simulation, spc_file)), os.path.join(simulations_path, simulation_200))
    with open('penEasy.in', 'w') as fp:
                        fp.write("# >>>> CONFIG FILE FOR penEasy >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n#\n# CASE DESCRIPTION:\n#   Sample config file adapted to the example described in the README\n#   file. Before editing this file, read carefully the instructions\n#   provided here after the data sections and in the README file.\n#\n# LAST UPDATE:\n#   2015-05-26 by JS\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# GENERAL INSTRUCTIONS\n#\n# * Lines starting with a '#' (in column 1) and blank lines are\n#   comments. Comments are NOT allowed inside data sections.\n#\n# * Do not change the order in which sections appear, neither the order\n#   of data fields in each section.\n#\n# * Each data section has a version number of the form yyyy-mm-dd that is\n#   written in the corresponding section title. Should an incorrect\n#   version be introduced an error message would be issued and the\n#   execution halted.\n#\n# * Character strings (e.g. file names) are introduced in free-format\n#   style, that is, leading and trailing blanks are allowed. Their\n#   maximum extension (except when noted) is 80 characters and they must\n#   not contain blanks. Thus, for instance, 'stainless steel' should be\n#   introduced as 'stainlessSteel' or 'stainless_Steel'.\n#\n# * Most syntax errors can be easily identified by looking for error\n#   messages or inconsistencies within the last lines of penEasy output.\n#   It is always a good idea to check the output to make sure that the\n#   information written after processing each section coincides with what\n#   is expected from the input.\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION CONFIG\n#\n# * Details on the simulation configuration are provided with their\n#   documentation (see ~/documentation/*).\n\n[SECTION CONFIG v.2013-03-18]\n 4.0e9             NUMBER OF HISTORIES (1.0e15 MAX)\n 20000             ALLOTTED TIME (s) (+ FOR REAL TIME; - FOR CPU TIME)\n 100.0             UPDATE INTERVAL (s)\n 1  1              INITIAL RANDOM SEEDS\n -                 SEEDS FILE; MUST ENTER SEEDS=0,0 TO APPLY\n -                 RESTART FILE; MUST ENTER SEEDS=-1,-1 TO APPLY\n penEasy.dmp       OUTPUT DUMP FILE; ENTER '-' FOR 'NO DUMP'\n 1200.0            INTERVAL BETWEEN DUMPS (s)\n[END OF CONFIG SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SOURCE SECTIONS\n#\n# * Details on the features and configuration of each source model are\n#   provided with their documentation (see ~/documentation/*).\n#   Notice that there must be one and only one active (status ON) source model.\n\n[SECTION SOURCE BOX ISOTROPIC GAUSS SPECTRUM v.2014-12-21]\n ON                              STATUS (ON or OFF)\n 2                               PARTICLE TYPE (1=ELECTRON, 2=PHOTON, 3=POSITRON)\n  SUBSECTION FOR PHOTON POLARIZATION:\n 0                               ACTIVATE PHOTON POLARIZATION PHYSICS (0=NO, 1=YES)\n 0.0 0.0 0.0                     STOKES PARAMETERS (UNUSED IF ACTIVATE POLARIZATION=0)\n  SUBSECTION FOR PARTICLE POSITION:\n 0.0  0.0  0.0                   COORDINATES (cm) OF BOX CENTER\n 0.0  0.0  0.0                   BOX SIDES (cm)\n 0.0  0.0                        FWHMs (cm) OF GAUSSIAN X,Y DISTRIBUTIONS\n 0.0  0.0  0.0                   EULER ANGLES [OMEGA,THETA,PHI](deg) FOR BOX ROTATION Rz(PHI).Ry(THETA).Rz(OMEGA).r\n 0.0  0.0  0.0                   TRANSLATION [DX,DY,DZ](cm) OF BOX CENTER POSITION\n 0                               SOURCE MATERIAL (0=DON'T CARE, >0 FOR LOCAL SOURCE, <0 FOR IN-FIELD BEAM)\n  SUBSECTION FOR PARTICLE DIRECTION:\n 0.0  0.0  1.0                   DIRECTION VECTOR; NO NEED TO NORMALIZE\n 0.0 2.57                        DIRECTION POLAR ANGLE INTERVAL [THETA0,THETA1], BOTH VALUES IN [0,180]deg\n 0.0 360.0                       DIRECTION AZIMUTHAL ANGLE INTERVAL PHI0 IN [0,360)deg AND DeltaPHI IN [0,360]deg\n 1                               APPLY ALSO TO DIRECTION THE ROTATION USED FOR BOX POSITION (0=NO, 1=YES)\n  SUBSECTION FOR PARTICLE ENERGY:\n {}.spc                    ENERGY SPECTRUM FILE NAME; ENTER '-' TO ENTER SPECTRUM IN NEXT LINES\n 0.0                             FWHM(eV) OF GAUSSIAN ENERGY DISTRIB. [NOTE FWHM=SIGMA*sqrt(8*ln(2))]\n[END OF BIGS SECTION]\n\n[SECTION SOURCE PHASE SPACE FILE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0                               PSF FORMAT (0=STANDARD penEasy ASCII, 1=IAEA BINARY)\n particles.psf                   PSF FILENAME, REMOVE EXTENSION IF PSF FORMAT=1\n 1                               SPLITTING FACTOR\n 0.0  0.0  0.0                   EULER ANGLES [Rz,Ry,Rz](deg) TO ROTATE POSITION AND DIRECTION\n 0.0  0.0  0.0                   TRANSLATION [DX,DY,DZ](cm) OF POSITION\n 1                               VALIDATE BEFORE SIMULATION (1=YES, MAY TAKE A WHILE; 0=NO)\n 0.000e0                         MAX PSF ENERGY (eV) (UNUSED IF VALIDATE=1 OR IAEA FORMAT; ADD 1023 keV FOR e+)\n[END OF SPSF SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION PENGEOM+PENVOX\n#\n# * Enter either: (i) a file name in the QUADRICS FILE field and a dash '-' in\n#   the VOXELS FILE field if you want to define only a quadric geometry model;\n#   (ii) a file name in the VOXELS FILE field and a dash '-' in the QUADRICS\n#   FILE field if you want to define only a voxelized geometry model; or (iii)\n#   both a quadrics and a voxelized file names in the corresponding fields if\n#   you want to define a combination of overlapping quadrics and voxelized models.\n#\n# * The TRANSPARENT QUADRIC MAT and GRANULARITY field are used only if both a\n#   quadric and a voxel geometries are defined. Otherwise they are irrelevant.\n#\n# * Details on the use and configuration of these geometry models are provided\n#   in the documentation (please refer to ~/documentation/*).\n\n[SECTION PENGEOM+PENVOX v.2009-06-15]\n {}.geo                     QUADRICS FILE NAME, USE '-' IF NONE\n -                               VOXELS FILE NAME, USE '-' IF NONE\n 1                               TRANSPARENT QUADRIC MAT (USED ONLY IF QUAD&VOX)\n 10                              GRANULARITY TO SCAN VOXELS (USED ONLY IF QUAD&VOX)\n[END OF GEO SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION PENELOPE\n#\n# * Write one line of data per defined material. Each line starts with\n#   the material index (MAT#), which should be an integer starting from 1.\n#   Set MAT# to zero in the last line to denote the end of the list.\n#\n# * Use 20 characters at most to introduce the material data file name.\n#   Blanks or special characters are not allowed in file names. Thus,\n#   instead of \"stainless steel.mat\" use \"stainlessSteel.mat\".\n#\n# * If, for a certain material, the transport parameters after the file\n#   name are left empty, then they are set automatically as follows:\n#     - Eabs for charged particles are set to 1% of the\n#       initial source energy (E), with the limiting values of 50 eV\n#       (min) and 1 MeV (max).\n#     - Eabs for photons is set to 0.1% E with the limiting values of 50\n#       eV and 1 MeV.\n#     - C1 and C2 are both set to 0.1.\n#     - WCC is set to min(Eabs(e-),1% E)\n#     - WCR is set to min(Eabs(phot),0.1% E).\n#     - DSMAX is set to infinity.\n#\n# * Do not remove the line containing the table header \"MAT# FILE...\".\n\n[SECTION PENELOPE v.2009-10-01]\n MAT# FILE___(max 20 char) EABS(e-)  EABS(ph)  EABS(e+)  C1    C2    WCC      WCR      DSMAX   COMMENTS\n  1   {}.mat           100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e30  material\n  2   Aire.mat            100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e-1  air detector\n  3   Aire.mat            100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e30  air enclosure\n  0 (SET MAT=0 TO END LIST)\n[END OF PEN SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR THE TALLY SECTIONS\n#\n# * Details on the features and configuration of each tally are provided\n#   with their documentation (see ~/documentation/*.txt).\n#\n# * The required RELATIVE UNCERTAINTY that is specified for each tally\n#   (except for those that do not have an associated uncertainty, e.g. a\n#   phase-space file) is used as a condition to stop the simulation. Only\n#   when the requested relative uncertainties of *all* the tallies have\n#   been attained the uncertainty condition is considered fulfilled.\n#   Recall that the simulation can also be halted because the allotted\n#   time or the number of histories requested have been reached. Setting\n#   the RELATIVE UNCERTAINTY of all tallies to zero will prevent the\n#   execution from stopping for this cause.\n#\n# * Note for advanced users: when a certain tally scores nothing (i.e.\n#   zero) the corresponding REPORT routine reports 0% uncertainty but, at\n#   the same time, it reports that the requested uncertainty has not been\n#   reached, irrespective of the value introduced in the config file.\n#   This is to prevent the simulation from being stopped by a deceptive\n#   impression of accuracy in highly inefficient simulations, where the\n#   score and its standard deviation after a short period of time can be\n#   null.\n\n[SECTION TALLY VOXEL DOSE v.2014-12-27]\n OFF                             STATUS (ON or OFF)\n 0  0                            ROI MIN,MAX X-INDEX (0 0 FOR ALL VOXELS)\n 0  0                            ROI MIN,MAX Y-INDEX (0 0 FOR ALL VOXELS)\n 0  0                            ROI MIN,MAX Z-INDEX (0 0 FOR ALL VOXELS)\n 0                               PRINT VOXELS MASS IN REPORT (1=YES,0=NO)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO,-1=NO&BINARYFORMAT)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF VDD SECTION]\n\n[SECTION TALLY SPATIAL DOSE DISTRIB v.2009-06-15]\n OFF                              STATUS (ON or OFF)\n 0.0  0.0   0                    XMIN,XMAX(cm),NXBIN (0 FOR DX=infty)\n 0.0  0.0   0                    YMIN,YMAX(cm),NYBIN (0 FOR DY=infty)\n 0.0  7.0   40                   ZMIN,ZMAX(cm),NZBIN (0 FOR DZ=infty)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO,-1=NO&BINARYFORMAT)\n 1.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF SDD SECTION]\n\n[SECTION TALLY CYLINDRICAL DOSE DISTRIB v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0.0  8.0  80                    RMIN,RMAX(cm),NRBIN (>0)\n 0.0  7.0  40                    ZMIN,ZMAX(cm),NZBIN (0 FOR DZ=infty)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF CDD SECTION]\n\n[SECTION TALLY SPHERICAL DOSE DISTRIB v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0.0  1.0  50                    RMIN,RMAX(cm),NRBIN (>0)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF SPD SECTION]\n\n[SECTION TALLY ENERGY DEPOSITION v.2012-06-01]\n ON                              STATUS (ON or OFF)\n 3                               DETECTION MATERIAL\n 2.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF EDP SECTION]\n\n[SECTION TALLY PULSE HEIGHT SPECTRUM v.2012-06-01]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0.0  1.0e9  100                 EMIN,EMAX(eV), No. OF E BINS\n 0.0  0.0                        A(eV^2),B(eV) FOR GAUSSIAN CONVOLUTION FWHM[eV]=sqrt(A+B*E[eV])\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PHS SECTION]\n\n[SECTION TALLY PIXELATED IMAGING DETECTOR v.2015-02-06]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0                               FILTER PHOTON INTERACTION (0=NOFILTER, -1=UNSCATTERED, 1=RAYLEIGH, 2=COMPTON, 3=SECONDARIES, 9=MULTISCATTERED)\n 0   100                         X-PIXEL SIZE(cm), No. X-PIXELS (ENTER 0 IN EITHER FIELD FOR AUTO)\n 0   100                         Y-PIXEL SIZE(cm), No. Y-PIXELS (ENTER 0 IN EITHER FIELD FOR AUTO)\n 1                               DETECTION MODE (1=ENERGY INTEGRATING, 2=PHOTON COUNTING, 3=PHOTON ENERGY DISCRIMINATING aka SPECTRUM)\n 1.0e3                           ENERGY DEPOSITION THRESHOLD (eV) FOR MODE=2 (IGNORED FOR OTHER MODES)\n 0.0  1.0e9  100                 EMIN,EMAX(eV), No. OF E BINS FOR MODE=3 (IGNORED FOR OTHER MODES)\n 0.0  0.0                        ENERGY RESOLUTION, ENTER A(eV^2),B(eV) FOR A GAUSSIAN WITH FWHM[eV]=sqrt(A+B*E[eV])\n 1                               REPORT FORMAT (1=COLUMNAR, 2=MATRIX, 3=BINARY)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PID SECTION]\n\n[SECTION TALLY FLUENCE TRACK LENGTH v.2012-06-01]\n ON                              STATUS (ON or OFF)\n 3                               DETECTION MATERIAL\n 10.0e3  80.0e3  70              EMIN,EMAX(eV), No. OF E BINS, APPEND 'LOG' FOR A LOG SCALE\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF FTL SECTION]\n\n[SECTION TALLY PHASE SPACE FILE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0                               PSF FORMAT (0=STANDARD penEasy ASCII, 1=IAEA BINARY)\n 1                               DETECTION MATERIAL (MUST BE A PERFECT ABSORBENT, EABS=+infty)\n output.psf                      PSF FILENAME, REMOVE EXTENSION IF FORMAT=1\n[END OF PSF SECTION]\n\n[SECTION TALLY PARTICLE CURRENT SPECTRUM v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0.0 1.0e9   100                 EMIN,EMAX(eV), No. OF E BINS\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PCS SECTION]\n\n[SECTION TALLY PARTICLE TRACK STRUCTURE v.2009-06-15]\n OFF                              STATUS (ON or OFF)\n 100                             NUMBER OF HISTORIES TO DISPLAY (~100 RECOMMENDED)\n[END OF PTS SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR VARIANCE-REDUCTION SECTIONS\n#\n# * Details on the features and configuration of each VR technique are provided\n#   with their documentation (see ~/documentation/*.txt).\n\n[SECTION INTERACTION FORCING v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1.0                             DON'T APPLY BELOW THIS STATISTICAL WEIGHT\n MAT  KPAR  ICOL  FORCING  (SET MAT=-1 TO END LIST)\n -1   0     0     1.0\n[END OF VRIF SECTION]\n\n[SECTION SPLITTING v.2015-05-30]\n OFF                             STATUS (ON or OFF)\n 1.0                             WGHTMIN, DO NOT SPLIT BELOW THIS STATISTICAL WEIGHT\n 1                               SPLITTING MATERIAL\n 1                               SPLITTING MODE (1=SIMPLE; 2=ROTATIONAL; 3=XY)\n 1                               SPLITTING FACTOR, IGNORED FOR MODE=3\n 0.0  0.0  0.0                   EULER ANGLES [Rz,Ry,Rz](deg), IGNORED FOR MODE=1\n 0.0  0.0  0.0                   SHIFT (cm), IGNORED FOR MODE=1\n 0                               SIGN OF W ('+', '-' OR '0'=BOTH), IGNORED FOR MODE=1\n 0.0  360.0                      AZIMUTHAL INTERVAL PHI0 IN [0,360)deg AND DeltaPHI IN (0,360]deg, USED ONLY IF MODE=2\n[END OF VRS SECTION]\n\n[SECTION RUSSIAN ROULETTE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1.0                             WGHTMAX, DO NOT PLAY ABOVE THIS STATISTICAL WEIGHT\n 1                               RUSSIAN ROULETTE MATERIAL\n 1.0                             SURVIVAL PROBABILITY\n[END OF VRRR SECTION]\n\n\n# >>>> END OF FILE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" \
                                 .format("{}.spc".format(spc_file), "oneL200", element))
    
    with open('oneL200.geo', 'w') as f:
            f.write("""0.3 mm shielding material 
                9x9 cm2
                0000000000000000000000000000000000000000000000000000000000000000
                SURFACE (   1)   Z=100 cm                                           
                INDICES=( 0, 0, 0, 1, 0)
                Z-SHIFT=( 1.000000000000000E+02,   0)       
                0000000000000000000000000000000000000000000000000000000000000000
                SURFACE (   2)   Z=100.200 cm (2.00 mm thick layer)                          
                INDICES=( 0, 0, 0, 1, 0)
                Z-SHIFT=( 1.002000000000000E+02,   0)      
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
                END      0000000000000000000000000000000000000000000000000000000""")


    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "Aire.mat")), os.path.join(simulations_path, simulation_250))
    shutil.copy(os.path.join(simulations_path, "{}/{}".format(lucky_simulation, "penEasy.x")), os.path.join(simulations_path, simulation_250))
    shutil.copy(os.path.join(simulations_path, "{}/{}.spc".format(lucky_simulation, spc_file)), os.path.join(simulations_path, simulation_250))

    with open('penEasy.in', 'w') as fp:
                        fp.write("# >>>> CONFIG FILE FOR penEasy >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n#\n# CASE DESCRIPTION:\n#   Sample config file adapted to the example described in the README\n#   file. Before editing this file, read carefully the instructions\n#   provided here after the data sections and in the README file.\n#\n# LAST UPDATE:\n#   2015-05-26 by JS\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# GENERAL INSTRUCTIONS\n#\n# * Lines starting with a '#' (in column 1) and blank lines are\n#   comments. Comments are NOT allowed inside data sections.\n#\n# * Do not change the order in which sections appear, neither the order\n#   of data fields in each section.\n#\n# * Each data section has a version number of the form yyyy-mm-dd that is\n#   written in the corresponding section title. Should an incorrect\n#   version be introduced an error message would be issued and the\n#   execution halted.\n#\n# * Character strings (e.g. file names) are introduced in free-format\n#   style, that is, leading and trailing blanks are allowed. Their\n#   maximum extension (except when noted) is 80 characters and they must\n#   not contain blanks. Thus, for instance, 'stainless steel' should be\n#   introduced as 'stainlessSteel' or 'stainless_Steel'.\n#\n# * Most syntax errors can be easily identified by looking for error\n#   messages or inconsistencies within the last lines of penEasy output.\n#   It is always a good idea to check the output to make sure that the\n#   information written after processing each section coincides with what\n#   is expected from the input.\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION CONFIG\n#\n# * Details on the simulation configuration are provided with their\n#   documentation (see ~/documentation/*).\n\n[SECTION CONFIG v.2013-03-18]\n 4.0e9             NUMBER OF HISTORIES (1.0e15 MAX)\n 20000             ALLOTTED TIME (s) (+ FOR REAL TIME; - FOR CPU TIME)\n 100.0             UPDATE INTERVAL (s)\n 1  1              INITIAL RANDOM SEEDS\n -                 SEEDS FILE; MUST ENTER SEEDS=0,0 TO APPLY\n -                 RESTART FILE; MUST ENTER SEEDS=-1,-1 TO APPLY\n penEasy.dmp       OUTPUT DUMP FILE; ENTER '-' FOR 'NO DUMP'\n 1200.0            INTERVAL BETWEEN DUMPS (s)\n[END OF CONFIG SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SOURCE SECTIONS\n#\n# * Details on the features and configuration of each source model are\n#   provided with their documentation (see ~/documentation/*).\n#   Notice that there must be one and only one active (status ON) source model.\n\n[SECTION SOURCE BOX ISOTROPIC GAUSS SPECTRUM v.2014-12-21]\n ON                              STATUS (ON or OFF)\n 2                               PARTICLE TYPE (1=ELECTRON, 2=PHOTON, 3=POSITRON)\n  SUBSECTION FOR PHOTON POLARIZATION:\n 0                               ACTIVATE PHOTON POLARIZATION PHYSICS (0=NO, 1=YES)\n 0.0 0.0 0.0                     STOKES PARAMETERS (UNUSED IF ACTIVATE POLARIZATION=0)\n  SUBSECTION FOR PARTICLE POSITION:\n 0.0  0.0  0.0                   COORDINATES (cm) OF BOX CENTER\n 0.0  0.0  0.0                   BOX SIDES (cm)\n 0.0  0.0                        FWHMs (cm) OF GAUSSIAN X,Y DISTRIBUTIONS\n 0.0  0.0  0.0                   EULER ANGLES [OMEGA,THETA,PHI](deg) FOR BOX ROTATION Rz(PHI).Ry(THETA).Rz(OMEGA).r\n 0.0  0.0  0.0                   TRANSLATION [DX,DY,DZ](cm) OF BOX CENTER POSITION\n 0                               SOURCE MATERIAL (0=DON'T CARE, >0 FOR LOCAL SOURCE, <0 FOR IN-FIELD BEAM)\n  SUBSECTION FOR PARTICLE DIRECTION:\n 0.0  0.0  1.0                   DIRECTION VECTOR; NO NEED TO NORMALIZE\n 0.0 2.57                        DIRECTION POLAR ANGLE INTERVAL [THETA0,THETA1], BOTH VALUES IN [0,180]deg\n 0.0 360.0                       DIRECTION AZIMUTHAL ANGLE INTERVAL PHI0 IN [0,360)deg AND DeltaPHI IN [0,360]deg\n 1                               APPLY ALSO TO DIRECTION THE ROTATION USED FOR BOX POSITION (0=NO, 1=YES)\n  SUBSECTION FOR PARTICLE ENERGY:\n {}.spc                    ENERGY SPECTRUM FILE NAME; ENTER '-' TO ENTER SPECTRUM IN NEXT LINES\n 0.0                             FWHM(eV) OF GAUSSIAN ENERGY DISTRIB. [NOTE FWHM=SIGMA*sqrt(8*ln(2))]\n[END OF BIGS SECTION]\n\n[SECTION SOURCE PHASE SPACE FILE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0                               PSF FORMAT (0=STANDARD penEasy ASCII, 1=IAEA BINARY)\n particles.psf                   PSF FILENAME, REMOVE EXTENSION IF PSF FORMAT=1\n 1                               SPLITTING FACTOR\n 0.0  0.0  0.0                   EULER ANGLES [Rz,Ry,Rz](deg) TO ROTATE POSITION AND DIRECTION\n 0.0  0.0  0.0                   TRANSLATION [DX,DY,DZ](cm) OF POSITION\n 1                               VALIDATE BEFORE SIMULATION (1=YES, MAY TAKE A WHILE; 0=NO)\n 0.000e0                         MAX PSF ENERGY (eV) (UNUSED IF VALIDATE=1 OR IAEA FORMAT; ADD 1023 keV FOR e+)\n[END OF SPSF SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION PENGEOM+PENVOX\n#\n# * Enter either: (i) a file name in the QUADRICS FILE field and a dash '-' in\n#   the VOXELS FILE field if you want to define only a quadric geometry model;\n#   (ii) a file name in the VOXELS FILE field and a dash '-' in the QUADRICS\n#   FILE field if you want to define only a voxelized geometry model; or (iii)\n#   both a quadrics and a voxelized file names in the corresponding fields if\n#   you want to define a combination of overlapping quadrics and voxelized models.\n#\n# * The TRANSPARENT QUADRIC MAT and GRANULARITY field are used only if both a\n#   quadric and a voxel geometries are defined. Otherwise they are irrelevant.\n#\n# * Details on the use and configuration of these geometry models are provided\n#   in the documentation (please refer to ~/documentation/*).\n\n[SECTION PENGEOM+PENVOX v.2009-06-15]\n {}.geo                     QUADRICS FILE NAME, USE '-' IF NONE\n -                               VOXELS FILE NAME, USE '-' IF NONE\n 1                               TRANSPARENT QUADRIC MAT (USED ONLY IF QUAD&VOX)\n 10                              GRANULARITY TO SCAN VOXELS (USED ONLY IF QUAD&VOX)\n[END OF GEO SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR SECTION PENELOPE\n#\n# * Write one line of data per defined material. Each line starts with\n#   the material index (MAT#), which should be an integer starting from 1.\n#   Set MAT# to zero in the last line to denote the end of the list.\n#\n# * Use 20 characters at most to introduce the material data file name.\n#   Blanks or special characters are not allowed in file names. Thus,\n#   instead of \"stainless steel.mat\" use \"stainlessSteel.mat\".\n#\n# * If, for a certain material, the transport parameters after the file\n#   name are left empty, then they are set automatically as follows:\n#     - Eabs for charged particles are set to 1% of the\n#       initial source energy (E), with the limiting values of 50 eV\n#       (min) and 1 MeV (max).\n#     - Eabs for photons is set to 0.1% E with the limiting values of 50\n#       eV and 1 MeV.\n#     - C1 and C2 are both set to 0.1.\n#     - WCC is set to min(Eabs(e-),1% E)\n#     - WCR is set to min(Eabs(phot),0.1% E).\n#     - DSMAX is set to infinity.\n#\n# * Do not remove the line containing the table header \"MAT# FILE...\".\n\n[SECTION PENELOPE v.2009-10-01]\n MAT# FILE___(max 20 char) EABS(e-)  EABS(ph)  EABS(e+)  C1    C2    WCC      WCR      DSMAX   COMMENTS\n  1   {}.mat           100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e30  material\n  2   Aire.mat            100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e-1  air detector\n  3   Aire.mat            100.0e3   10.00e3   100.0e3   0.1   0.1   100.0e3  10.00e3  1.0e30  air enclosure\n  0 (SET MAT=0 TO END LIST)\n[END OF PEN SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR THE TALLY SECTIONS\n#\n# * Details on the features and configuration of each tally are provided\n#   with their documentation (see ~/documentation/*.txt).\n#\n# * The required RELATIVE UNCERTAINTY that is specified for each tally\n#   (except for those that do not have an associated uncertainty, e.g. a\n#   phase-space file) is used as a condition to stop the simulation. Only\n#   when the requested relative uncertainties of *all* the tallies have\n#   been attained the uncertainty condition is considered fulfilled.\n#   Recall that the simulation can also be halted because the allotted\n#   time or the number of histories requested have been reached. Setting\n#   the RELATIVE UNCERTAINTY of all tallies to zero will prevent the\n#   execution from stopping for this cause.\n#\n# * Note for advanced users: when a certain tally scores nothing (i.e.\n#   zero) the corresponding REPORT routine reports 0% uncertainty but, at\n#   the same time, it reports that the requested uncertainty has not been\n#   reached, irrespective of the value introduced in the config file.\n#   This is to prevent the simulation from being stopped by a deceptive\n#   impression of accuracy in highly inefficient simulations, where the\n#   score and its standard deviation after a short period of time can be\n#   null.\n\n[SECTION TALLY VOXEL DOSE v.2014-12-27]\n OFF                             STATUS (ON or OFF)\n 0  0                            ROI MIN,MAX X-INDEX (0 0 FOR ALL VOXELS)\n 0  0                            ROI MIN,MAX Y-INDEX (0 0 FOR ALL VOXELS)\n 0  0                            ROI MIN,MAX Z-INDEX (0 0 FOR ALL VOXELS)\n 0                               PRINT VOXELS MASS IN REPORT (1=YES,0=NO)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO,-1=NO&BINARYFORMAT)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF VDD SECTION]\n\n[SECTION TALLY SPATIAL DOSE DISTRIB v.2009-06-15]\n OFF                              STATUS (ON or OFF)\n 0.0  0.0   0                    XMIN,XMAX(cm),NXBIN (0 FOR DX=infty)\n 0.0  0.0   0                    YMIN,YMAX(cm),NYBIN (0 FOR DY=infty)\n 0.0  7.0   40                   ZMIN,ZMAX(cm),NZBIN (0 FOR DZ=infty)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO,-1=NO&BINARYFORMAT)\n 1.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF SDD SECTION]\n\n[SECTION TALLY CYLINDRICAL DOSE DISTRIB v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0.0  8.0  80                    RMIN,RMAX(cm),NRBIN (>0)\n 0.0  7.0  40                    ZMIN,ZMAX(cm),NZBIN (0 FOR DZ=infty)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF CDD SECTION]\n\n[SECTION TALLY SPHERICAL DOSE DISTRIB v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0.0  1.0  50                    RMIN,RMAX(cm),NRBIN (>0)\n 1                               PRINT COORDINATES IN REPORT (1=YES,0=NO)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF SPD SECTION]\n\n[SECTION TALLY ENERGY DEPOSITION v.2012-06-01]\n ON                              STATUS (ON or OFF)\n 3                               DETECTION MATERIAL\n 2.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF EDP SECTION]\n\n[SECTION TALLY PULSE HEIGHT SPECTRUM v.2012-06-01]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0.0  1.0e9  100                 EMIN,EMAX(eV), No. OF E BINS\n 0.0  0.0                        A(eV^2),B(eV) FOR GAUSSIAN CONVOLUTION FWHM[eV]=sqrt(A+B*E[eV])\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PHS SECTION]\n\n[SECTION TALLY PIXELATED IMAGING DETECTOR v.2015-02-06]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0                               FILTER PHOTON INTERACTION (0=NOFILTER, -1=UNSCATTERED, 1=RAYLEIGH, 2=COMPTON, 3=SECONDARIES, 9=MULTISCATTERED)\n 0   100                         X-PIXEL SIZE(cm), No. X-PIXELS (ENTER 0 IN EITHER FIELD FOR AUTO)\n 0   100                         Y-PIXEL SIZE(cm), No. Y-PIXELS (ENTER 0 IN EITHER FIELD FOR AUTO)\n 1                               DETECTION MODE (1=ENERGY INTEGRATING, 2=PHOTON COUNTING, 3=PHOTON ENERGY DISCRIMINATING aka SPECTRUM)\n 1.0e3                           ENERGY DEPOSITION THRESHOLD (eV) FOR MODE=2 (IGNORED FOR OTHER MODES)\n 0.0  1.0e9  100                 EMIN,EMAX(eV), No. OF E BINS FOR MODE=3 (IGNORED FOR OTHER MODES)\n 0.0  0.0                        ENERGY RESOLUTION, ENTER A(eV^2),B(eV) FOR A GAUSSIAN WITH FWHM[eV]=sqrt(A+B*E[eV])\n 1                               REPORT FORMAT (1=COLUMNAR, 2=MATRIX, 3=BINARY)\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PID SECTION]\n\n[SECTION TALLY FLUENCE TRACK LENGTH v.2012-06-01]\n ON                              STATUS (ON or OFF)\n 3                               DETECTION MATERIAL\n 10.0e3  80.0e3  70              EMIN,EMAX(eV), No. OF E BINS, APPEND 'LOG' FOR A LOG SCALE\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF FTL SECTION]\n\n[SECTION TALLY PHASE SPACE FILE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 0                               PSF FORMAT (0=STANDARD penEasy ASCII, 1=IAEA BINARY)\n 1                               DETECTION MATERIAL (MUST BE A PERFECT ABSORBENT, EABS=+infty)\n output.psf                      PSF FILENAME, REMOVE EXTENSION IF FORMAT=1\n[END OF PSF SECTION]\n\n[SECTION TALLY PARTICLE CURRENT SPECTRUM v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1                               DETECTION MATERIAL\n 0.0 1.0e9   100                 EMIN,EMAX(eV), No. OF E BINS\n 0.0                             RELATIVE UNCERTAINTY (%) REQUESTED\n[END OF PCS SECTION]\n\n[SECTION TALLY PARTICLE TRACK STRUCTURE v.2009-06-15]\n OFF                              STATUS (ON or OFF)\n 100                             NUMBER OF HISTORIES TO DISPLAY (~100 RECOMMENDED)\n[END OF PTS SECTION]\n\n\n# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n# INSTRUCTIONS FOR VARIANCE-REDUCTION SECTIONS\n#\n# * Details on the features and configuration of each VR technique are provided\n#   with their documentation (see ~/documentation/*.txt).\n\n[SECTION INTERACTION FORCING v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1.0                             DON'T APPLY BELOW THIS STATISTICAL WEIGHT\n MAT  KPAR  ICOL  FORCING  (SET MAT=-1 TO END LIST)\n -1   0     0     1.0\n[END OF VRIF SECTION]\n\n[SECTION SPLITTING v.2015-05-30]\n OFF                             STATUS (ON or OFF)\n 1.0                             WGHTMIN, DO NOT SPLIT BELOW THIS STATISTICAL WEIGHT\n 1                               SPLITTING MATERIAL\n 1                               SPLITTING MODE (1=SIMPLE; 2=ROTATIONAL; 3=XY)\n 1                               SPLITTING FACTOR, IGNORED FOR MODE=3\n 0.0  0.0  0.0                   EULER ANGLES [Rz,Ry,Rz](deg), IGNORED FOR MODE=1\n 0.0  0.0  0.0                   SHIFT (cm), IGNORED FOR MODE=1\n 0                               SIGN OF W ('+', '-' OR '0'=BOTH), IGNORED FOR MODE=1\n 0.0  360.0                      AZIMUTHAL INTERVAL PHI0 IN [0,360)deg AND DeltaPHI IN (0,360]deg, USED ONLY IF MODE=2\n[END OF VRS SECTION]\n\n[SECTION RUSSIAN ROULETTE v.2009-06-15]\n OFF                             STATUS (ON or OFF)\n 1.0                             WGHTMAX, DO NOT PLAY ABOVE THIS STATISTICAL WEIGHT\n 1                               RUSSIAN ROULETTE MATERIAL\n 1.0                             SURVIVAL PROBABILITY\n[END OF VRRR SECTION]\n\n\n# >>>> END OF FILE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" \
                                 .format("{}.spc".format(spc_file), "oneL250", element))
    
    with open('oneL250.geo', 'w') as f:
            f.write("""0.3 mm shielding material 
                9x9 cm2
                0000000000000000000000000000000000000000000000000000000000000000
                SURFACE (   1)   Z=100 cm                                           
                INDICES=( 0, 0, 0, 1, 0)
                Z-SHIFT=( 1.000000000000000E+02,   0)       
                0000000000000000000000000000000000000000000000000000000000000000
                SURFACE (   2)   Z=100.250 cm (2.50 mm thick layer)                          
                INDICES=( 0, 0, 0, 1, 0)
                Z-SHIFT=( 1.002500000000000E+02,   0)      
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
                END      0000000000000000000000000000000000000000000000000000000""")



