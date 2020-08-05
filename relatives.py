#******************************************************************************
# relatives.py
#******************************************************************************
# Name: Ron Balaban
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# Win Seen
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#

my_file=open("dna.txt","r")
whole_file= my_file.read()
dna_list=whole_file.split()
# Here, I've turned the dna.txt document into 1 list of 200 entries.

smallest_distance=100                                       # Smallest distance found so far, starting at max value of 100
for i in range(0,len(dna_list)):                            # Look at each DNA strand in entire list
    for j in range(i+1,len(dna_list)):                      # Look at the next DNA strand(s) in entire list
        current_distance=0                                  # Starting distance between 2 current DNA strands
        for letter in range(0,100):    
            if dna_list[i][letter] != dna_list[j][letter]:  # Look at each individual letter (ACTG) in second strand
                current_distance+=1                         # For every different letter in our 2 strands, their distance goes up.
        if current_distance<smallest_distance:              # If current distance between current 2 strands is smaller than min, it becomes new min.
            smallest_distance=current_distance
            str_a=i                                    # I've defined these two strands as the closest pair. 
            str_b=j                                    #
              
print("Smallest distance between 2 strings is {0}, in lines {1} and {2}".format(smallest_distance, str_a+1,str_b+1))

my_file.close()


