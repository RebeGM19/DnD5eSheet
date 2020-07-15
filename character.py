

class character:

    def __init__(self, name, cclass, race, background, level, attr, mods):
        self.name = name
        self.cclass = cclass
        self.race = race
        self.background = background
        self.level = level
        self.attr = attr
        self.mods = mods

    def saveCharacter(self, cursor):
        params = (self.name, self.cclass, self.race, self.background, self.level, self.attr, self.mods)
        cursor.execute("INSERT INTO Character VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", params)