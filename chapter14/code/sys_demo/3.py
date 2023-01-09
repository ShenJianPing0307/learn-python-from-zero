import sys
import os

pig_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), "pig.py")

sys.path.append(pig_path)

print(sys.path)
