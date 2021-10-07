# Import the Random Module 
import random  
# Code Name Lists 
alpha = ['Crimson', 'Phantom', 'Zephyr', 'Palisade', 'Skyfall'] 
omega = ['Whirlwind', 'Gatecrasher', 'Iceberg', 'Zealot', 'Element']  
# 1.CREATE FOR LOOP HERE # HINT: You will have a nested For loop.  

for _ in alpha:
    for _ in omega:
        # 2. The Random Code Names will print here.
        print ("Operation: " + random.choice(alpha) + " " + random.choice(omega))
        
# HINT: Remember your indentions. 
 