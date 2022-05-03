bashCommand = "ls"
import subprocess
print
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
print("hello")