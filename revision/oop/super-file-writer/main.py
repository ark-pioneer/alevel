class SuperFileWriter():
    def __init__(self, fname):
        self.fname = fname
    
    def super_write(self):
        while True:
            data = input("enter data: ")
            if data == "STOP":
                break
            with open(self.fname, "a") as f:
                f.write(data + "\n")

    def super_edit(self, num, data):
        with open(self.fname) as f:
            lines = f.read().splitlines()
        if not (0 < num <= len(lines)):
            print("invalid line number ["+str(num)+"] for max lines:", len(lines))
        else:
            lines[num-1] = data
            with open(self.fname, "w") as f:
                f.write("\n".join(lines))

s = SuperFileWriter("test.txt")
s.super_edit(5, "WASSUP, PUPILS")
