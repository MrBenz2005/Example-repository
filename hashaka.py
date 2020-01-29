class My_class():
    def __init__(self):
        self.table = []
        for i in range(50):
            self.table.append([])

    def __len__(self, hashka_tab):
        counter = len(hashka_tab)


    def add(self, value):
        a = hash(value) % len(self.table)
        if value in self.table[a]:
            pass
        else:
            self.table[a].append(value)

    def remove(self, name):
        b = hash(name) % len(self.table)
        if name in self.table[b]:
            self.table[b].remove(name)


"""
spicok = [['kost', 'egort', 'mpops'], [18,14,43,3,7], ['tri', 'chetire', 'vosem']]
Hashka = hash_table(spicok)
print(Hashka.add('3', 'lada'))
print(Hashka.remove('2'))"""