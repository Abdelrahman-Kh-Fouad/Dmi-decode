class DMIParser :
    def __init__(self ,file :str):
        self.content={}
        self.fileAsLines = file.splitlines()
        self.numberOfSpacesInIntend = self.GetNumberOfSpaces()
        self.lineNumber = -1


    def GetNumberOfSpaces(self):
        '''
        Get number of spaces in one intend for parsing.
        Return:
            intger -- number of spaces.
        '''
        for line in self.fileAsLines:
            if len(line) - len(line.lstrip())!=0:
                return len(line) - len(line.lstrip())


    def GetNumberOfIntend(self , line:str):
        '''
        Get number of intend in a line.
        Param:
            line:string -- line we want search.
        Return:
            intger -- number of intends
        '''
        return (len(line)-len(line.lstrip())) / self.numberOfSpacesInIntend

    '''noOp: no action yet
        sectionName: read sectionName
        readKeyValue: read a line has colon : in it into a key value pair
        readList: when the next line has greater indentation level than the property line'''


    def GetMove(self):
        '''
        Get what will happen to state.
        Param:
            lineNumber:intger -- line number
        Return:
             Difference to state
        '''
        current = self.GetNumberOfIntend(self.fileAsLines[self.lineNumber])
        next = current if self.lineNumber +1 >= len(self.fileAsLines)  else self.GetNumberOfIntend(self.fileAsLines[self.lineNumber+1])
        return next -current

    def GetSectionFromLine(self , line ):
        pass


    def Parse(self ,  state:int =0 , section=None , property:str=None):
        """parsing file line by line

        Param:
            lineNumber:Intger -- number of line we in in file.\n
            state: Intger -- our state --> noOp : 0 , sectionName : 1 , readKeyValue :2  , readList:3.\n
        """

        while



    def __str__(self):
        result:str =''
        for section in self.content.keys():

            result+=section+'\n'
            for prop in self.content[section]:
                if type(self.content[section][prop]) ==str :
                    result+='\t'+prop + ':' +self.content[section][prop]+'\n'
                else :
                    result +='\t'+prop+':'+'\n'
                    for elem in self.content[section][prop]:
                        result+='\t\t'+elem+'\n'


        return result


