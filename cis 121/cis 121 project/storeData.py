from visualization import visualization_scroll 
import time 
for i in range(10):
    with open("data.txt", "w") as f:
        f.write(visualization_scroll(i))
        time.sleep(1)
    
# outputs the commands into a text file 