from DMIParser import DMIParser
if __name__ == '__main__':
    file =open('myDmi.txt')
    file = file.read()
    dm = DMIParser(file)
    dm.Parse()
    print(dm)