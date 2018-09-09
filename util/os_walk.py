import os
for root, dirs, files in os.walk("C:\Users\Parthiban_Dhandapani\Desktop\python_examples"):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
   print os.path.basename(os.path.join(root, name))
print __file__
