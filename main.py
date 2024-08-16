from rembg import remove

inputPath = "C:/Users/user/Downloads/inputFile/input.jpg" # You should give a path for input directory
outputPath = "C:/Users/user/Downloads/outputFile/output1.png" # You should give a path for output directory

with open(inputPath, 'rb') as i:
    with open(outputPath, 'wb') as o:
        inputFile = i.read()
        outputFile = remove(inputFile)
        o.write(outputFile)

