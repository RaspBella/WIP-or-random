class Cube(object):
    def __init__(self, U, L, F, R, B, D):
        self.faces = {"U":[[U]*3]*3, "L":[[L]*3]*3, "F":[[F]*3]*3, "R":[[R]*3]*3, "B":[[B]*3]*3, "D":[[D]*3]*3}
        self.display()
    
    def display(self):
        for x in range(3):
            print("\t", end="")
            for y in range(3):
                print(self.faces["U"][x][y], end=" ")
            print()
        print()
        for x in range(3):
            for y in range(3):
                print(self.faces["L"][x][y], end=" ")
            print("\t", end="")
            for y in range(3):
                print(self.faces["F"][x][y], end=" ")
            print("\t", end="")
            for y in range(3):
                print(self.faces["R"][x][y], end=" ")
            print("\t", end="")
            for y in range(3):
                print(self.faces["B"][x][y], end=" ")
            print()
        print()
        for x in range(3):
            print("\t", end="")
            for y in range(3):
                print(self.faces["D"][x][y], end=" ")
            print()
    
    def Ui(self):
        current_rung = [self.faces["L"][0], self.faces["F"][0], self.faces["R"][0], self.faces["B"][0]]
        new_rung = [[""]]*4
        self.faces["U"] = list(list(x) for x in zip(*self.faces["U"]))[::-1]
        for x in range(4):
            new_rung[x] = current_rung[x-1]
        self.faces["L"][0], self.faces["F"][0], self.faces["R"][0], self.faces["B"][0] = new_rung[0], new_rung[1], new_rung[2], new_rung[3]
    
    def U2(self):
        self.Ui(), self.Ui()
    
    def U(self):
        self.U2(), self.Ui()

    def Li(self):
        current_rung = [[self.faces["U"][0][0], self.faces["U"][1][0], self.faces["U"][2][0]], [self.faces["B"][0][0], self.faces["B"][1][0], self.faces["B"][2][0]], [self.faces["D"][0][0], self.faces["D"][1][0], self.faces["D"][2][0]], [self.faces["F"][0][2], self.faces["F"][1][2], self.faces["F"][2][2]]]
        new_rung = [[""]]*4
        self.faces["L"] = list(list(x) for x in zip(*self.faces["L"]))[::-1]
        for x in range(4):
            new_rung[x] = current_rung[x-3]
        [self.faces["U"][0][0], self.faces["U"][1][0], self.faces["U"][2][0]], [self.faces["B"][0][0], self.faces["B"][1][0], self.faces["B"][2][0]], [self.faces["D"][0][0], self.faces["D"][1][0], self.faces["D"][2][0]], [self.faces["F"][0][2], self.faces["F"][1][2], self.faces["F"][2][2]] = new_rung[0], new_rung[1], new_rung[2], new_rung[3]
    
    def L2(self):
        self.Li(), self.Li()
    
    def L(self):
        self.L2(), self.Li()
    
    def Fi(self):
        current_rung = [self.faces["U"][2], [self.faces["R"][0][0], self.faces["R"][1][0], self.faces["R"][2][0]], self.faces["D"][0], [self.faces["L"][0][2], self.faces["L"][1][2], self.faces["L"][2][2]]]
        new_rung = [[""]]*4
        self.faces["F"] = list(list(x) for x in zip(*self.faces["F"]))[::-1]
        for x in range(4):
            new_rung[x] = current_rung[x-1]
        self.faces["U"][2], [self.faces["R"][0][0], self.faces["R"][1][0], self.faces["R"][2][0]], self.faces["D"][0], [self.faces["L"][0][2], self.faces["L"][1][2], self.faces["L"][2][2]] = new_rung[0], new_rung[1], new_rung[2], new_rung[3]
    
    def F2(self):
        self.Fi(), self.Fi()
    
    def F(self):
        self.F2(), self.Fi()
    
    def Ri(self):
        current_rung = [[self.faces["U"][0][2], self.faces["U"][1][2], self.faces["U"][2][2]], [self.faces["B"][0][0], self.faces["B"][1][0], self.faces["B"][2][0]], [self.faces["D"][0][2], self.faces["D"][1][2], self.faces["D"][2][2]], [self.faces["F"][0][2], self.faces["F"][1][2], self.faces["F"][2][2]]]
        new_rung = [[""]]*4
        self.faces["R"] = list(list(x) for x in zip(*self.faces["R"]))[::-1]
        for x in range(4):
            new_rung[x] = current_rung[x-1]
        [self.faces["U"][0][2], self.faces["U"][1][2], self.faces["U"][2][2]], [self.faces["B"][0][0], self.faces["B"][1][0], self.faces["B"][2][0]], [self.faces["D"][0][2], self.faces["D"][1][2], self.faces["D"][2][2]], [self.faces["F"][0][2], self.faces["F"][1][2], self.faces["F"][2][2]] = new_rung[0], new_rung[1], new_rung[2], new_rung[3]
    
    def R2(self):
        self.Ri(), self.Ri()
    
    def R(self):
        self.R2(), self.Ri()
    
    def Bi(self):
        current_rung = [self.faces["U"][0], [self.faces["L"][0][0], self.faces["L"][1][0], self.faces["L"][2][0]], self.faces["D"][2], [self.faces["R"][0][2], self.faces["R"][1][2], self.faces["R"][2][2]]]
        new_rung = [[""]]*4
        self.faces["B"] = list(list(x) for x in zip(*self.faces["B"]))[::-1]
        for x in range(4):
            new_rung[x] = current_rung[x-1]
        self.faces["U"][0], [self.faces["L"][0][0], self.faces["L"][1][0], self.faces["L"][2][0]], self.faces["D"][2], [self.faces["R"][0][2], self.faces["R"][1][2], self.faces["R"][2][2]] = new_rung[0], new_rung[1], new_rung[2], new_rung[3]
    
    def B2(self):
        self.Bi(), self.Bi()
    
    def B(self):
        self.B2(), self.Bi()
    
    def Di(self):
        current_rung = [self.faces["L"][2], self.faces["F"][2], self.faces["R"][2], self.faces["B"][2]]
        new_rung = [[""]]*4
        self.faces["D"] = list(list(x) for x in zip(*self.faces["D"]))[::-1]
        for x in range(4):
            new_rung[x] = current_rung[x-1]
        self.faces["L"][2], self.faces["F"][2], self.faces["R"][2], self.faces["B"][2] = new_rung[0], new_rung[1], new_rung[2], new_rung[3]
    
    def D2(self):
        self.Di(), self.Di()
    
    def D(self):
        self.D2(), self,Di()
    
    def checkered_alg(self):
        self.U2(), self.display(), print()
        self.D2(), self.display(), print()
        self.L2(), self.display(), print()
        self.R2(), self.display(), print()
        self.F2(), self.display(), print()
        self.B2(), self.display()

cube = Cube("W", "O", "G", "R", "B", "Y")

print()
cube.checkered_alg()
#cube.display()