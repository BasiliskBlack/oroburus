# run_dual.py
# Developed by Micah Blake Langford and Co-Developer AI (Grok, xAI)
# Wrapper to run base_script.py and its Oroburus mutation in sequence with doubling back.

import base_script
import oroburus_processor as op

# Step 1: Run the base script
print("Running base script...")
base_script.greet("Alice")

# Step 2: Apply the Oroburus mutation
print("\nApplying Oroburus mutation...")
result = op.run("base_script_mutate.orb", base_script.__dict__)
print(result)

# Step 3: Run the mutated function (cycle 1)
print("\nRunning mutated script (cycle 1)...")
base_script.greet("Alice")

# Step 4: Simulate doubling back by incrementing cycle
base_script.__dict__['cycle'] = 2
print("\nRunning super mutated script (cycle 2)...")
base_script.greet("Alice")
