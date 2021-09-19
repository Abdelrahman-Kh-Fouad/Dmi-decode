class DNIParser :
    def __init__(self ,file :str):
        self.content={}
        self.fileAsLines = file.splitlines()
        self.numberOfSpacesInIntend =self.GetNumberOfSpaces()


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

    #state = noOp : 0 , sectionName : 1 , readKeyValue :2  , readList:3
    def Parse(self , lineNumber:int , state:int ):
        """parsing file line by line

        Param:
            lineNumber:Intger -- number of line we in in file.\n
            state: Intger -- our state --> noOp : 0 , sectionName : 1 , readKeyValue :2  , readList:3.\n
        """
        if lineNumber == len(self.fileAsLines):
            return

        line = self.fileAsLines[lineNumber]
        if state == 0 :
            if lineNumber +1  < len(self.fileAsLines):
                if self.GetNumberOfIntend(self.fileAsLines[lineNumber + 1]) > self.GetNumberOfIntend(line):
                    self.Parse(lineNumber +1 , 1 )