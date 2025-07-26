import re

runIf= False
previousIf= False
PreviousIfStack= False
TokenList= []

def IfconditionCheck(method):
        def wrapper(self, *args, **kwargs):
            if len(self.Ifcondition) not in [0 ,1]:
                raise RuntimeError(f"[Error] ~ If class ~ Ifcondition ~ more than one condition found")
            return method(self, *args, **kwargs)
        return wrapper

def Start():
    global runIf ,previousIf
    runIf= True
    previousIf= True

def End():
    global runIf
    runIf= False

class If:
    def __init__(self ,argument1):
        if runIf:
            self.argument1= argument1
            self.Ifcondition= []
            self.state= False
        else:
            raise RuntimeError("[Error] ~ If class ~ start not found")
    
    @IfconditionCheck
    def EqualTo(self ,argument2):
        try:
            self.Ifcondition.append("EqualTo")
            self.state= bool(self.argument1== argument2)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ EqualTo ~\n{e}")
        return self

    @IfconditionCheck
    def NotEqualTo(self ,argument2):
        try:
            self.Ifcondition.append("NotEqualTo")
            self.state= bool(self.argument1!= argument2)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ NotEqualTo ~\n{e}")
        return self
    
    @IfconditionCheck
    def In(self ,argument2):
        try:
            self.Ifcondition.append("In")
            self.state= bool(self.argument1 in argument2)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ In ~\n{e}")
        return self
    
    @IfconditionCheck
    def NotIn(self ,argument2):
        try:
            self.Ifcondition.append("NotIn")
            self.state= bool(self.argument1 not in argument2)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ NotIn ~\n{e}")
        return self
    
    @IfconditionCheck
    def GreaterThan(self ,argument2):
        try:
            self.Ifcondition.append("GreaterThan")
            self.state= bool(self.argument1> argument2)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ GreaterThan ~\n{e}")
        return self
    
    @IfconditionCheck
    def SmallerThan(self ,argument2):
        try:
            self.Ifcondition.append("SmallerThan")
            self.state= bool(argument2> self.argument1)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ SmallerThan ~\n{e}")
        return self
    
    @IfconditionCheck
    def GreaterOrEqualThan(self ,argument2):
        try:
            self.Ifcondition.append("GreaterOrEqualThan")
            self.state= bool(self.argument1>= argument2)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ GreaterOrEqualThan ~\n{e}")
        return self
    
    @IfconditionCheck
    def SmallerOrEqualThan(self ,argument2):
        try:
            self.Ifcondition.append("SmallerOrEqualThan")
            self.state= bool(argument2>= self.argument1)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ SmallerOrEqualThan ~\n{e}")
        return self
    
    @IfconditionCheck
    def Condition(self ,argument2):
        try:
            self.Ifcondition.append("Condition")
            self.state= bool(argument2)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ Condition ~\n{e}")
        return self
    
    @IfconditionCheck
    def Anything(self):
        try:
            self.Ifcondition.append("Anything")
            self.state= True 
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ Anything ~\n{e}")
        return self
    
    @IfconditionCheck
    def MatchesPattern(self ,argument2):
        try:
            self.Ifcondition.append("MatchesPattern")
            self.state= bool(re.match(argument2, str(self.argument1)))
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ MatchesPattern ~\n{e}")
        return self
    
    @IfconditionCheck
    def MatchesAnyPattern(self, patterns: list):
        try:
            self.Ifcondition.append("MatchesAnyPattern")
            self.state= any(re.match(p, str(self.argument1)) for p in patterns)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ MatchesAnyPattern ~\n{e}")
        return self
    
    def Then(self ,then= "__if__"):
        try:
            global previousIf
            if then=="__if__":
                if self.state and previousIf: 
                    self.state= True
                else:
                    self.state= False
                    previousIf= False
            elif then=="__else__":
                if self.state and not previousIf: 
                    self.state= True
                else:
                    self.state= False
                    previousIf= True
            else:
                raise RuntimeError(f"[Error] ~ If class ~ Then ~ invalid argument")
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ Then ~\n{e}")
        return self
    
    def Run(self, func, args=(), kwargs=None):
        kwargs = kwargs or {}
        try:
            if self.state:
                func(*args, **kwargs)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ Run ~ {func.__name__} ~\n{e}")
        return self
    
    def StopStack(self):
        try:
            global PreviousIfStack
            if self.state:
                PreviousIfStack= True
            else:
                PreviousIfStack= False
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ StopStack ~\n{e}")
    
    def AddToTokenList(self ,token):
        try:
            global TokenList
            if self.state:
                TokenList.append(token)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ AddToTokenList ~\n{e}")
        return self

    def ExtendTokenListWith(self ,tokens):
        try:
            global TokenList
            if self.state:
                if isinstance(tokens ,list):
                    TokenList.extend(tokens)
                else:
                    raise RuntimeError("[Error] ~ If class ~ ExtendTokenList ~ list not found")
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ ExtendTokenList ~\n{e}")
        return self

    def InsertTokenAt(self ,index ,token):
        try:
            global TokenList
            if self.state:
                if isinstance(index ,int):
                    TokenList.insert(index ,token)
                else:
                    raise RuntimeError(f"[Error] ~ If class ~ InsertTokenAt ~ invalid index")
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ InsertTokenAt ~\n{e}")
        return self
    
    def RemoveFromTokenList(self ,token):
        try:
            global TokenList
            if self.state:
                TokenList.remove(token)
        except ValueError:
            raise RuntimeError(f"[Error] ~ If class ~ RemoveFromTokenList ~ token not found")
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ RemoveFromTokenList ~\n{e}")
        return self
        
    def PopToken(self):
        try:
            global TokenList
            if self.state and TokenList:
                TokenList.pop()
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ PopToken ~\n{e}")
        return self
    
    def PopTokenAt(self, index):
        try:
            global TokenList
            if self.state and isinstance(index, int) and 0 <= index < len(TokenList):
                TokenList.pop(index)
            else:
                raise RuntimeError("[Error] ~ If class ~ PopTokenAt ~ invalid index")
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ PopTokenAt ~\n{e}")
        return self
    
    def ReplaceTokenAt(self, index, token):
        try:
            global TokenList
            if self.state and isinstance(index, int) and 0 <= index < len(TokenList):
                TokenList[index] = token
            else:
                raise RuntimeError("[Error] ~ If class ~ ReplaceTokenAt ~ invalid index")
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ ReplaceTokenAt ~\n{e}")
        return self
        
    def SwapTokens(self, index1, index2):
        try:
            global TokenList
            if self.state:
                if all(isinstance(i, int) and 0 <= i < len(TokenList) for i in [index1, index2]):
                    TokenList[index1], TokenList[index2] = TokenList[index2], TokenList[index1]
                else:
                    raise RuntimeError("[Error] ~ If class ~ SwapTokens ~ invalid index")
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ SwapTokens ~\n{e}")
        return self
    
    def RemoveTokenRange(self, start, end):
        try:
            global TokenList
            if self.state:
                if all(isinstance(i, int) for i in [start, end]) and 0 <= start < end <= len(TokenList):
                    del TokenList[start:end]
                else:
                    raise RuntimeError("[Error] ~ If class ~ RemoveTokenRange ~ invalid range")
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ RemoveTokenRange ~\n{e}")
        return self
    
    def ResetTokenList(self):
        try:
            global TokenList
            if self.state:
                TokenList.clear()
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ ResetTokenList ~\n{e}")
        return self
    
    def Print(self, text):
        try:
            if self.state:
                print(text)
        except Exception as e:
            raise RuntimeError(f"[Error] ~ If class ~ Print ~\n{e}")
        return self