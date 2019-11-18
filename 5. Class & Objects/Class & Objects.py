class motor():

    def __init__(self, merek, harga):
        self.merek = merek
        self.harga = harga

    def test(self):
        print("Motor %s" % self.nama)

    def get_motor(self):
        print("Merek %s, Harga %d" %(self.merek, self.harga))

detail = motor("Supra", 18000000)
print(detail.get_motor())
print("======================")
detail.merek = "Beat"
detail.harga = 20000000
print(detail.get_motor())