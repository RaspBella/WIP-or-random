class OS():
    def __init__(self, DE, browser, IDE):
        self.DE = DE
        self.browser = browser
        self.IDE = IDE

class Computer():
    def __init__(self, OS):
        self.OS = OS
            

class Programmer():
    def __init__(self, name, age, pronouns, favourite_languages, desktop, laptop):
        self.name =  name
        self.age = age
        self.pronouns = pronouns
        self.favourite_languages = favourite_languages
        self.desktop = desktop
        self.laptop = laptop

    def display(self):
        print("Name:", self.name+"\nAge:", str(self.age)+"\nPronouns:", end=" ")
        print(*self.pronouns, sep=', ')
        print("Favourite languages:", end=" ")
        print(*self.favourite_languages, sep=', ')
        print("Desktop:")
        for x in self.desktop.OS:
            print("\t"+x+":")
            if len(self.desktop.OS[x].DE) > 0:
                print("\t\tDE: "+self.desktop.OS[x].DE)
            if len(self.desktop.OS[x].browser) > 0:
                print("\t\tBrowser: "+self.desktop.OS[x].browser)
            if len(self.desktop.OS[x].IDE) > 0:
                print("\t\tIDE: "+self.desktop.OS[x].IDE)
        print("Laptop:")
        for x in self.laptop.OS:
            print("\t"+x+":")
            if len(self.laptop.OS[x].DE) > 0:
                print("\t\tDE: "+self.laptop.OS[x].DE)
            if len(self.laptop.OS[x].browser) > 0:
                print("\t\tBrowser: "+self.laptop.OS[x].browser)
            if len(self.laptop.OS[x].IDE) > 0:
                print("\t\tIDE: "+self.laptop.OS[x].IDE)

Me = Programmer(
    "Bella Campbell",
    17,
    ["She", "They"],
    ["C", "Python"],
    Computer(
        {
            "Arch":OS("wayfire", "firefox", "code"),
            "Gentoo":OS("", "", "nvim"),
            "LFS_soon":OS("", "", "cat")
        }
    ),
    Computer(
        {
            "Arch":OS("awesome", "qutebrowser", "code"),
            "Gentoo":OS("awesome", "qutebrowser", "nvim")
        }
    )
)

Me.display()