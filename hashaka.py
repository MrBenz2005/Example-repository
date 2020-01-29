class hash_table():
    def __init__(self,hash):
        spicok = []
        for i in
        self.hash = hash


    def add(self, object):

        return self.hash

    def remove(self, name):
        del self.hash[name]
        return self.hash

spicok = [['kost', 'egort', 'mpops'], [18,14,43,3,7], ['tri', 'chetire', 'vosem']]
Hashka = hash_table(spicok)
print(Hashka.add('3', 'lada'))
print(Hashka.remove('2'))