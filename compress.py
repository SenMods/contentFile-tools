import struct, os

def buildheader_contentFile(countFiles):
    fileCount_contentFileType=(countFiles).to_bytes(4, 'big')
    contentFile_toHex = b'\x63\x6F\x6E\x74\x65\x6E\x74\x46\x69\x6C\x65'
    version = b'\x00\x00\x00\x01'
    separator = b'\x00\x00\x00\x00'
    
    allheader = contentFile_toHex + version + fileCount_contentFileType + separator
    return allheader

def buildFile_contentFile(fileName):
    lenght_of_FileName = len(fileName).to_bytes(4, 'big')
    fileName_toHex = fileName.encode('utf_8')
    with open('toCompress/'+fileName, 'rb') as f:
        contents=f.read()
        lenContents = len(contents)

    separatorFinishFile = b'\x77\x77\x77\x77'+'separate_File_contentFile'.encode()+b'\x77\x77\x77\x77'
    separatorFileName = b'\x77\x77\x77\x77'+('separatorFileName').encode()+b'\x77\x77\x77\x77'

    # len mechanism
    lendecrypted = str(lenContents).encode('utf_8')
    lenoflendecrypted = len(lendecrypted).to_bytes(4, 'big')


    allFile = lenght_of_FileName + fileName_toHex + separatorFileName + lenoflendecrypted + lendecrypted + contents + separatorFinishFile
    return allFile

def main():
    print('contentFile - Final - Built 05 Feb 2023 - 17:01')

    os.makedirs('toCompress', exist_ok=True)
    os.makedirs('compressed', exist_ok=True)

    for file in os.listdir('toCompress'):
        with open('compressed/'+file.split('.')[0]+'.contentFile', 'wb') as dec:
            dec.write(buildheader_contentFile(1))
            dec.write(buildFile_contentFile(file))

main()












