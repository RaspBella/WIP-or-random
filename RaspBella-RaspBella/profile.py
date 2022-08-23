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
