

import time
#from cryptodome.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Padding
import os




def encryptcbc(file,name,size):
  dataraw = file.read()
  encripter = AES.new(b'the key 12345678', AES.MODE_CBC)
  print('key has been entered')
  datapadded = Padding.pad(dataraw, AES.block_size)
  time1 = time.perf_counter_ns()
  datacripted = encripter.encrypt(datapadded)
  time2 = time.perf_counter_ns()
  print(f'Encription time : {time2-time1: .1f} Nanoseconds')
  cryptwriter = open('ENCRYPTED - ' + os.path.basename(file.name), 'wb')
  cryptwriter.write(datacripted)
  print('Name of encrypted file : ' + name)
  print('Size : ' + size + ' kB')
  try: 
    with open('benchmarkresult-CBC.txt', 'a') as filetext:
      filetext.write(name + ' ' + size + f' {time2-time1 : .1f} Nanoseconds' + '\n')
  except IOError:
    filetext = open('benchmarkresult-CBC.txt', 'w')
    filetext.write(name + ' ' + size + f' {time2-time1 : .1f} Nanoseconds' + '\n')




def encrypteax(file,name,size):
  dataraw = file.read()
  encripter = AES.new(b'the key 12345678', AES.MODE_EAX)
  print('key has been entered')
  datapadded = Padding.pad(dataraw, AES.block_size)
  time1 = time.process_time()
  datacripted, tag = encripter.encrypt_and_digest(datapadded)
  time2 = time.process_time()
  print(f'Encription time : {time2-time1: .9f} Seconds')
  cryptwriter = open('ENCRYPTED - ' + os.path.basename(file.name), 'wb')
  cryptwriter.write(datacripted)
  print('Name of encrypted file : ' + name)
  print('Size : ' + size + ' kB')
  try: 
    with open('benchmarkresult-EAX.txt', 'a') as filetext:
      filetext.write(name + ' ' + size + f' {time2-time1 : .9f} Seconds' + '\n')
  except IOError:
    filetext = open('benchmarkresult-EAX.txt', 'w')
    filetext.write(name + ' ' + size + f' {time2-time1 : .9f} Seconds' + '\n')

def encryptgcm(file,name,size):
  dataraw = file.read()
  encripter = AES.new(b'the key 12345678', AES.MODE_GCM)
  print('key has been entered')
  datapadded = Padding.pad(dataraw, AES.block_size)
  time1 = time.process_time()
  datacripted, tag = encripter.encrypt_and_digest(datapadded)
  time2 = time.process_time()
  print(f'Encription time : {time2-time1: .9f} Seconds')
  cryptwriter = open('ENCRYPTED - ' + os.path.basename(file.name), 'wb')
  cryptwriter.write(datacripted)
  print('Name of encrypted file : ' + name)
  print('Size : ' + size + ' kB')
  try: 
    with open('benchmarkresult-GCM.txt', 'a') as filetext:
      filetext.write(name + ' ' + size + f' {time2-time1 : .9f} Seconds' + '\n')
  except IOError:
    filetext = open('benchmarkresult-GCM.txt', 'w')
    filetext.write(name + ' ' + size + f' {time2-time1 : .9f} Seconds' + '\n')

def encryptecb(file,name,size):
  dataraw = file.read()
  encripter = AES.new(b'the key 12345678', AES.MODE_ECB)
  print('key has been entered')
  datapadded = Padding.pad(dataraw, AES.block_size)
  time1 = time.process_time()
  datacripted = encripter.encrypt(datapadded)
  time2 = time.process_time()
  print(f'Encription time : {time2-time1: .9f} Seconds')
  cryptwriter = open('ENCRYPTED - ' + os.path.basename(file.name), 'wb')
  cryptwriter.write(datacripted)
  print('Name of encrypted file : ' + name)
  print('Size : ' + size + ' kB')
  try: 
    with open('benchmarkresult-ECB.txt', 'a') as filetext:
      filetext.write(name + ' ' + size + f' {time2-time1 : .9f} Seconds' + '\n')
  except IOError:
    filetext = open('benchmarkresult-ECB.txt', 'w')
    filetext.write(name + ' ' + size + f' {time2-time1 : .9f} Seconds' + '\n')

def encryptsiv(file,name,size):
  dataraw = file.read()
  nonce = get_random_bytes(16)
  encripter = AES.new(b'the key 12345678the key 12345678', AES.MODE_SIV,nonce=nonce)
  datapadded = Padding.pad(dataraw, AES.block_size)
  time1 = time.process_time()
  datacripted, tag = encripter.encrypt_and_digest(datapadded)
  time2 = time.process_time()
  print(f'Encription time : {time2-time1: .9f} Seconds')
  cryptwriter = open('ENCRYPTED - ' + os.path.basename(file.name), 'wb')
  cryptwriter.write(datacripted)
  print('Name of encrypted file : ' + name)
  print('Size : ' + size + ' kB')
  try: 
    with open('benchmarkresult-SIV.txt', 'a') as filetext:
      filetext.write(name + ' ' + size + f' {time2-time1 : .9f} Seconds' + '\n')
  except IOError:
    filetext = open('benchmarkresult-SIV.txt', 'w')
    filetext.write(name + ' ' + size + f' {time2-time1 : .9f} Seconds' + '\n')

def main():
  mode = 'start'
  while (mode != 'quit'):
    print('Encryption mode available : ')
    print('1. AES - CBC Cipher-Block Chaining')
    print('2. AES - EAX encrypt-then-authenticate-then-translate')
    print('3. AES - ECB Electronic Code Block ')
    print('4. AES - GCM Galois Counter Mode')
    print('5. AES - SIV Synthetic Initialization Vector')
    mode = input('Select Encryption mode (1 - 5): ')
    totalfile = 0
    cwd = os.getcwd()
    print('working directory : ' + cwd)
    filelist = []
    print('Available files : ')
    for files in os.listdir(cwd):
      filesize = os.stat(files)
      filesize = str(float(filesize.st_size) / 1024) + ' kB'
      if files.endswith('.png'):
        totalfile += 1\
        
        print(str(totalfile) + '. ' + files + ' | Size : ' + filesize + ' kB') 
        filelist.append(files)
      if files.endswith('.jpg'):
        totalfile += 1
        print(str(totalfile) + '. ' + files + ' | Size : ' + filesize + ' kB')
        filelist.append(files)
      if files.endswith('.pdf'):
        totalfile += 1
        print(str(totalfile) + '. ' + files + ' | Size : ' + filesize + ' kB')
        filelist.append(files)
      if files.endswith('txt'):
        totalfile += 1
        print(str(totalfile) + '. ' + files + ' | Size : ' + filesize + ' kB')
        filelist.append(files)
    if( mode != 'quit'):
      print(filelist)
      whichfile = input('Select file to encrypt (x for encrypt ALL files): ')
      if(whichfile != 'x'):
        print(filelist[int(whichfile)-1])
        rawdata = open(filelist[int(whichfile)-1], 'rb')
      else:
        print('ALL files selected')

      if (mode == '1'):
        if(whichfile =='x'):
          for embuh in filelist:
            filesize = str(float(os.stat(embuh).st_size) / 1024) + ' kB'
            thisfile = open(embuh, 'rb')
            encryptcbc(thisfile,embuh,filesize)
        else:
          filename = filelist[int(whichfile)-1]
          filesize = str(float(os.stat(filename).st_size) / 1024) + ' kB'
          encryptcbc(rawdata,filename,filesize)
      elif (mode == '2'):
        if(whichfile =='x'):
          for embuh in filelist:
            filesize = str(float(os.stat(embuh).st_size) / 1024) + ' kB'
            thisfile = open(embuh, 'rb')
            encrypteax(thisfile,embuh,filesize)
        else:
          filename = filelist[int(whichfile)-1]
          filesize = str(float(os.stat(filename).st_size) / 1024) + ' kB'
          encrypteax(rawdata,filename,filesize)
      elif (mode == '3'):
        if(whichfile =='x'):
          for embuh in filelist:
            filesize = str(float(os.stat(embuh).st_size) / 1024) + ' kB'
            thisfile = open(embuh, 'rb')
            encryptecb(thisfile,embuh,filesize)
        else:
          filename = filelist[int(whichfile)-1]
          filesize = str(float(os.stat(filename).st_size) / 1024) + ' kB'
          encryptecb(rawdata,filename,filesize)
      elif (mode == '4'):
        if(whichfile =='x'):
          for embuh in filelist:
            filesize = str(float(os.stat(embuh).st_size) / 1024) + ' kB'
            thisfile = open(embuh, 'rb')
            encryptgcm(thisfile,embuh,filesize)
        else:
          filename = filelist[int(whichfile)-1]
          filesize = str(float(os.stat(filename).st_size) / 1024) + ' kB'
          encryptgcm(rawdata,filename,filesize)
      elif (mode == '5'):
        if(whichfile =='x'):
          for embuh in filelist:
            filesize = str(float(os.stat(embuh).st_size) / 1024) + ' kB'
            thisfile = open(embuh, 'rb')
            encryptsiv(thisfile,embuh,filesize)
        else:
          filename = filelist[int(whichfile)-1]
          filesize = str(float(os.stat(filename).st_size) / 1024) + ' kB'
          encryptsiv(rawdata,filename,filesize)
      else: 
        print('Unknown input?')
        break
    else:
      print('Exit code detected')   
      break



'''
#decryption
decripter = AES.new(b'the key 12345678', AES.MODE_CBC, b'iv is 1234567890')
print('Decrypting.. ')
f = open("encryptedfile.txt", "rb")
x = f.read()
decript = decripter.decrypt(x)
depadded = Padding.unpad(decript, AES.block_size)
print('Decrypted javanese: ')
print(depadded.decode('utf-8'))
'''

if __name__ == "__main__":
  main()