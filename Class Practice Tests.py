##### Testing Area #####

baran = Player("Baran", 50, "Catcher", .300)
karnik = Player("Karnik", 2, "Left Field", .205)
longo = Player("Longoria", 100, "Third Base", .100)
archer = Player("Archer", 0, "Pitcher", .005)
price = Player("Price", 1, "Pitcher", .010)
cabrera = Player("Cabrera", 15, "Shortstop", .250)
zobrist = Player("Zobrist", 11, "Utilityman", .350)
maddon = Player("Maddon", 0, "Manager", .000)
cash = Player("Cash", 4, "Backup Catcher", .040)
poop = Player("Poop", 20, "Who Cares", .743)
list1 = [baran, longo, archer, price, cabrera, zobrist, maddon, cash, poop]
list2 = [karnik, longo, archer, price, cabrera, zobrist, maddon, cash, poop]
Rays = Team("Rays", 4, 158, list1)
Orioles = Team("Orioles", 158, 4, list2)
print Rays.roster()
print baran.displayStats()
print moreHomers(Orioles, Rays)
Rays.addPlayer(karnik)
print Rays.roster()
