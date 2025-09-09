
import sys
import os
import time
import numpy as np
from PIL import Image


def hextorgb(value) :

    value = value.lstrip("#")
    value = value.rstrip()
    
    
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def main () :



    oghexes = []
    newhexes = []
    
    try :
        imagedir = os.listdir("INPUT")
    except:
        print("Missing 'INPUT' folder.") 
        return 
    
    if imagedir == [] :
        print("Empty or missing 'INPUT' folder. Please put images in the 'INPUT' folder before running the program.")
        return

    for n in range(0, len(imagedir)) :
        try :
            iimage = Image.open(f"INPUT\\{imagedir[n]}")
        except :
            print(f"Something went wrong! Image '{imagedir[n]}' produced an error while opening.")
            return
        
        data = np.array(iimage)
        red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]    
        
        try :
            f = open("INPUTHEX\palette1.txt")  
        except:
            print("Missing 'palette1.txt' in 'INPUTHEX' folder.") 
            return 
        
        for y,line in enumerate(f) :

            try :
                newhex = line.lstrip("#")
                newhex = newhex.rstrip()

                newrgb = []

                newrgb += hextorgb(newhex)
                
                oghexes.append(newrgb)
            except :
                print("Something went wrong! Are you sure the HEXes in palette1.txt are correctly written?")
                return
        
        try :
            f = open("OUTPUTHEX\palette2.txt")  
        except:
            print("Missing 'palette2.txt' in 'OUTPUTHEX' folder.") 
            return

        for y,line in enumerate(f) :

            try :
                newhex = line.lstrip("#")
                newhex = newhex.rstrip()

            

                newrgb = []

                newrgb += hextorgb(newhex)

            

                newhexes.append(newrgb)
            except :
                print("Something went wrong! Are you sure the HEXes in palette1.txt are correctly written?")
                return


        if len(oghexes) != len(newhexes) :

            print("The amount of HEXes in the palette1 and palette2 file shall be equal.")
            return

        for x in range(0, len(oghexes)) :

            try :
                mask = (red == oghexes[x][0]) & (green == oghexes[x][1]) & (blue == oghexes[x][2])
                data[:,:,:3][mask] = [newhexes[x][0],newhexes[x][1],newhexes[x][2]]
                
                iimage = Image.fromarray(data)
            except :
                print("Something went wrong! Are you sure your HEXes are written correctly?")

        
        try :
            iimage.save(f'OUTPUT\{imagedir[n]}')
        except:
            print("Missing 'OUTPUT' folder.") 
            return 
        
    

print("Put the images you want to change in the INPUT folder.\nPut the Input HEX list in the INPUTHEX folder as a .txt file named palette1.txt.\nPut the Output HEX list in the OUTPUTHEX folder as a .txt file named palette2.txt. \n\n(NOTE: every HEX shall be on a newline alone, and the HEX entries shall be the same in both files.)\n")
input("Once done hit ENTER")
main()