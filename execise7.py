

import os
# os.rename("foo.txt","Cluster.txt")
i = 1
files = os.listdir("Cluster")
for file in files:
        if file.endswith(".png"):
            print(file)
            os.rename(f"Cluster/{file}",f"Cluster/{i}.png")
            i = i + 1