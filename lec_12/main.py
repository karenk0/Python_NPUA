import random
import time

f = open("lec12file.txt",'w')

for row in range(100):
    line = ""
    for count in range(20):
        randomNumber = str(random.randint(1, 100))
        line += f"{randomNumber} "
    line += "\n"
    f.write(line)
print("File is ready.")

f.close()

f = open("lec12file.txt",'r')

print("Processing data using map...")

filteredFile = ""
for line in f:
    myList = list(map(lambda x: int(x), line.split()))
    filteredLine = list(filter(lambda x: x > 40, myList))
    filtered_line = ' '.join(map(str, filteredLine))
    filteredFile += filtered_line + "\n"

f.close()

f = open("lec12file.txt",'w')

f.write(filteredFile)

f.close()
print("Filtered lines appended to the file.")

def timingDecorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} sec")
        return result
    return wrapper

def read_file_as_generator(fileName):
    f = open(fileName, 'r')
    for line in f:
        yield line

@timingDecorator
def proccess(fileName):
    generator = read_file_as_generator(fileName)
    for line in generator:
            print(line)

proccess("lec12file.txt")


