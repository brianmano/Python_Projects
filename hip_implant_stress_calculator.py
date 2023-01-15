import math
import time 

def subprogram_1(body_weight, canal_diameter, ult_ten_strength, femoral_head_offset):  
    
    time.sleep(0.5)
    print("The body weight of patient Freida Pinto is:", round(body_weight, 1), "Newtons.")

    time.sleep(0.5)
    print("\nThe canal diameter of patient Freida Pinto is:", round(canal_diameter,1), "mm.")

    time.sleep(0.5)
    print("\nThe ultimate tensile stress of Tantalum is", round(ult_ten_strength,1), "MPa.")

#Axial Stress Calculations
    x = 0.0001 #Arbitrary value
    stem_diameter = (x*canal_diameter)
    force = (3.25 * body_weight)
    cross_sectional_area = ((math.pi / 4) * (stem_diameter ** 2))
    axial_stress = (force / cross_sectional_area)

#Bending Stress and Applied Tensile Stress Calculations
    moment = (force * femoral_head_offset)
    y = (0.5 * stem_diameter)
    inertia = ((math.pi / 64) * (stem_diameter ** 4))
    bending_stress = ((moment * y) / inertia)
    app_ten_stress = round((axial_stress + bending_stress), 1)
    while app_ten_stress > ult_ten_strength:
        x += 0.0001
        stem_diameter = (x * canal_diameter)
        force = (3.25 * body_weight)
        cross_sectional_area = ((math.pi / 4) * (stem_diameter ** 2))
        axial_stress = (force / cross_sectional_area)

        femoral_head_offset = 31
        moment = (force * femoral_head_offset)
        y = (0.5 * stem_diameter)
        inertia = ((math.pi / 64) * (stem_diameter ** 4))
        bending_stress = ((moment * y) / inertia)
        app_ten_stress = round((axial_stress + bending_stress), 1)

    min_stem_dia = round((stem_diameter+0.1), 1)
    time.sleep(0.5)
    print("\nThe minimum stem diameter is:", min_stem_dia, "mm")
    time.sleep(0.5)
    print("\nThe applied tensile stress is:", app_ten_stress, "N/mm^2\n")
    
    main()

def subprogram_2(team_number, stem_dia, body_weight):  
    file_cyc = open("SN Data - Sample Metal.txt", "r")
    cross_sectional_area = ((math.pi / 4) * (stem_dia ** 2))
    stress_max = (12 * body_weight) / cross_sectional_area
    stress_min = (-12 * body_weight) / cross_sectional_area
    stress_amp = (stress_max - stress_min) / 2
    for line in file_cyc: #Runs through every line in the file
        sn_data = line.split()
        stress = float(sn_data[0]) #Converts data into floats and sets variable stress according to the position on each line given in the file
        cycles_fail = float(sn_data[1]) #Converts data into floats and sets number of cycles variable according to the position on each line given in the file
        stress_concentration = (8.5 + math.log(cycles_fail, 10) ** ((0.7 * team_number) / 40)) #Calculate the stress concentration for each corresponding number of cycles in each line
        adj_stress_amp = stress_amp * stress_concentration
        if  adj_stress_amp > 800:
            time.sleep(0.5)
            print("Stress concentration is: ", round(adj_stress_amp,1), "The number of cycles is less than the minimum number of cycles: 10688\n")
            break
        
        elif adj_stress_amp < 440:
            time.sleep(0.5)
            print("Stress concentration is: ", round(adj_stress_amp,1), "The number of cycles is greater than the minimum number of cycles: 46210417\n")
            break

        elif stress <= adj_stress_amp: #Once there is a line with our team values stress concentration, according to cycles in line, that reaches beyond the corresponding stress, it stops as the stress has failed
            stress_fail = round(adj_stress_amp,1) #Re-establish the stress concentration as stress fail
            time.sleep(0.5)
            print("Stress concentration is: ", stress_fail, " with number of cycles: ", cycles_fail,"\n")
            break
    main()


def subprogram_3(modulus_bone, modulus_implant, outer_dia, body_weight, canal_diameter):  
    
    comp_stress = (body_weight * 30) / ((math.pi) * ((outer_dia) ** 2 - (canal_diameter) ** 2) / 4)
    stress_reduc = comp_stress * (((3 * modulus_bone) / (modulus_bone + modulus_implant)) ** (1 / 3))
    E_ratio = (modulus_implant / modulus_bone) ** (1 / 2)
    x = 0 #Set initial number of years to 0 (kept number of years as variable x as stated in equation instructions) to establish a starting point of function
    comp_strength = 0.0015 * (x ** 2) - (3.752 * x * E_ratio) + 168.54
    while stress_reduc < comp_strength: #Keeps running the while function if the stress reduction is below the comp strength
        x += 1 #Everytime while loop runs, adds a counter to the number of years to calculate comp stress for every year
        comp_strength =round(0.0015 * (x ** 2) - (3.752 * x * E_ratio) + 168.54,1)
        time.sleep(0.5)
        print("Year:", str(x), "Comp Strength: ", str(comp_strength), "MPa")
    yrs_fail = x #Sets new value of years as the final counter in the while loop before it breaks
    stress_fail = round(comp_strength,1) #Sets new value of comp strength as the stress fail since it broke out of the while loop with this value corresponding to higher stress reduction
    time.sleep(0.5)
    print("The number of years taken to fail is: ", yrs_fail, "with the compressive strength of: ", stress_fail,"MPa\n")
    main()


def main():
    body_weight = 44.4*9.8
    canal_diameter = 10
    ult_ten_strength = 760
    team_number = 13
    stem_dia = 10 * 0.8
    modulus_bone = 17  # Y. S. Lai, W. C. Chen, C. H. Huang, C. K. Cheng, K. K. Chan, and T. K. Chang, “The Effect of Graft Strength on Knee Laxity and Graft In-Situ Forces after Posterior Cruciate Ligament Reconstruction,” PLOS ONE, vol. 10, no. 5, p. e0127293, May 2015, Available: doi: 10.1371/JOURNAL.PONE.0127293. (Accessed: December 1st, 2021)
    modulus_implant = 175  # Tantalum
    outer_dia = 16
    femoral_head_offset = 31
    print("Welcome to the menu: \n 1. Subprogram 1 \n 2. Subprogram 2 \n 3. Subprogram 3 \n 4. Exit from program")
    selection = input("Please input which corresponding integer command you would like to run: ")

    if selection.isdigit(): #Checks to see if the number is a proper digit or not, in order to not break function if string is inputted (else statement)
        selection = int(selection)
        if selection == 1:
            subprogram_1(body_weight, canal_diameter, ult_ten_strength, femoral_head_offset)
        elif selection == 2:
            subprogram_2(team_number, stem_dia, body_weight)
        elif selection == 3:
            subprogram_3(modulus_bone, modulus_implant, outer_dia, body_weight, canal_diameter)
        elif selection == 4:
            exit
        else:
            print("Select a command from integer 1 to 4")
            main()
    else:
        print("Input an integer from 1 to 4")
        main()


main()