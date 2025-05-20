class logicGate():
    def __init__(self,label):
        self.label=label

    def getoutput():
        pass

class andGate(logicGate):
    def __init__(self,label):
        super().__init__(label)
    
    def getOutput(self,n1,n2):

        if n1==1 and n2==1:
            return 1
        else:
            return 0
    
class orGate(logicGate):
    def __init__(self,label):
        super().__init__(label)
    
    def getOutput(self,n1,n2):

        if n1==1 or n2==1:
            return 1
        else:
            return 0

class notGate(logicGate):
    def __init__(self,label):
        super().__init__(label)

    def getOutput(self,n):
        if n==1:
            return 0
        else:
            return 1

class nandGate(logicGate): 
    def getOutput(self,n1,n2):

        if n1==1 and n2==1:
            return 0
        else:
            return 1

class norGate(logicGate):
    def getOutput(self,n1,n2):
        
        if n1==1 or n2==1:
            return 0
        else:
            return 1 

class xorGate(LogicGate):
    def evaluate(self, n1,n2):
        return n1 != n2

class xnorGate(LogicGate):
    def evaluate(self, n1, n2):
        return n1 == n2       
    
and_gate=andGate("AND")
or_gate=orGate("OR")
not_gate=notGate("NOT")
nand_gate=nandGate("NAND")
nor_gate=norGate("NOR")
xor_gate=xorGate("XOR")
xnor_gate=xnorGate("XNOR")


print("AND gate output for (1,1) = ",and_gate.getOutput(1,1))
print("AND gate output for (1,0) = ",and_gate.getOutput(1,0))
print("AND gate output for (0,0) = ",and_gate.getOutput(0,0))

print("OR gate output for (1,1) = ",or_gate.getOutput(1,1))
print("OR gate output for (1,0) = ",or_gate.getOutput(1,0))
print("OR gate output for (0,0) = ",or_gate.getOutput(0,0))

print("NOT gate output for (1) = ",not_gate.getOutput(1))
print("NOT gate output for (0) = ",not_gate.getOutput(0))
