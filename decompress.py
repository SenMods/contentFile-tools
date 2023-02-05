import struct, os

# getHeader - Useless function - Will be used in the future

def getHeader(filename):
    contentFile = open(filename, 'rb')

    contentFile.read(11) # contentFile string
    contentFile.read(4) # version
    filecount = struct.unpack('>I', contentFile.read(4))
    contentFile.read(4) # separator

    filecount = filecount.replace('(', '')
    filecount = filecount.replace(')', '')
    filecount = filecount.replace(',', '') # removing all useless values

    return filecount

def getFile(filename):
    file = open('toDecompress/'+filename, 'rb')

    file.read(23) # header

    lenFilename = struct.unpack('>I', file.read(4))[0]

    filename_fromContent = file.read(lenFilename).decode('utf-8')

    file.read(25) # Separator

    outputFile = open('decompressed/'+filename_fromContent, 'wb')

    lenOfLenOfContents = struct.unpack('>I', file.read(4))[0]

    len_decrypted = file.read(lenOfLenOfContents)

    fileContents = file.read(int(len_decrypted))

    outputFile.write(fileContents)

    file.close()
    outputFile.close()

def main():
    print('contentFileDec - Final - Built 05 Feb 2023 - 17:12')

    os.makedirs('toDecompress', exist_ok=True)
    os.makedirs('decompressed', exist_ok=True)

    for file in os.listdir('toDecompress'):
        getFile(file)

main()





    
