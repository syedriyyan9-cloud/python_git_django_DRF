"""
import vs from in python
"""
# Using import
import math
print(math.sqrt(16))  # 4.0
# sqrt(16) would raise NameError

# Using from
from math import sqrt
print(sqrt(16))       # 4.0

# Watch out for name clash
sqrt = "my variable"
from math import sqrt  # overwrites my variable!
print(sqrt(16))        # 4.0, not "my variable"

# Safe with alias
from math import sqrt as square_root
print(square_root(25)) # 5.0

"""
Creating module called mymath.py and importing it
"""
# main.py (in same folder)
import my_math

print(my_math.add(10, 5))        # 15
print(my_math.multiply(3, 4))    # 12



"""
Exploring __name__ == "__main__" block
"""
# present in files of demo.ppy and importer.py



"""
PYTHONPATH
"""

import sys

# See where Python looks for modules
print("Search paths:")
for i, path in enumerate(sys.path):
    print(f"{i}: {path}")

# Let's say you have a module at /my_libs/helper.py
# Method 1: Set PYTHONPATH before running script
# export PYTHONPATH="/my_libs:$PYTHONPATH"

# Method 2: Modify sys.path at runtime
custom_path = "/my_libs"
if custom_path not in sys.path:
    sys.path.insert(0, custom_path)

# Now you can import from that location
try:
    # import helper
    print("Module found!")
except ImportError:
    print("Module not found. Check your PYTHONPATH.")