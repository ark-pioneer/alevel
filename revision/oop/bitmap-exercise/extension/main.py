class BitMap():
    def load(fname):
        with open(fname) as f:
            data = f.read().splitlines()
        grid = [line.split(",") for line in data]
        return BitMap(grid, fname)

    def save(bitmap, fname=False):
        if not fname:
            fname = bitmap.fname
        with open(fname, "w") as f:
            for line in bitmap.grid:
                f.write(",".join(line)+"\n")
    
    def save_binary(bitmap, fname=False):
        if not fname:
            fname = bitmap.fname
        # create new filename
        slug, ext = fname.split('.')
        bin_fname = slug + '.bin.' + ext
        # open file with new filename in write mode
        with open(bin_fname, "w") as f:
            # calculate the 8bit bin number for height and width, write to file.
            height = len(bitmap.grid)
            width = len(bitmap.grid[0])
            metadata = format(height, '08b')+format(width, '08b')
            f.write(metadata)
            # then for each line in the image write to the file the binary strings for the colours in the line
            for line in bitmap.grid:
                # first, turn the pixel colour into its ascii code
                ascii_line = [ord(pixel) for pixel in line]
                # then, turn the ascii code into its 8bit binary code
                bin_line = [format(ascii, '08b') for ascii in ascii_line]
                # then join the line items together with no separator and write it to the file
                f.write("".join(bin_line))
    
    def load_binary(fname):
        # open file in read mode and read the file data into memory as one string
        with open(fname) as f:
            data = f.read()
        # first extract height and width from first 16bits.
        metadata = data[0:16]
        # image_height = int(metadata[:8],2)
        image_width = int(metadata[8:],2)

        # then, create the grid as a 2d list of 8bit bin strings. Later convert each back to pixel colours.
        # so, chunk the rest of the data into heightxwidth strings each of length 8 (because 8bit bin numbers)
        # create the grid outer list
        lines = []
        # variable controls iteration
        index = 16
        # each line fills up to max width before new line created
        current_line = []
        # go through all the data, taking 8 chars at a time,  building the grid
        while index <= len(data):
            # if the line is full (line has as many pixels as image_width)
            if len(current_line) >= image_width:
                # add line to the grid
                lines.append(current_line)
                # reset the line
                current_line = []
            # add next 8 characters of data to the line 
            current_line.append(data[index:index+8])
            index += 8

        # then, convert binary into integer into character for each bin code in each line.
        grid = [[chr(int(bin, 2)) for bin in line] for line in lines]
        # instantiate the bitmap correctly
        return BitMap(grid, fname)
    
    def __init__(self, grid, fname=False):
        self.fname = fname
        self.grid = grid
    
    def draw_y(self, colour, coords, length, direction):
        x, y = coords
        for _i in range(length):
            self.grid[y][x] = colour
            if direction == "UP":
                y -= 1
            elif direction == "DOWN":
                y += 1

b = BitMap.load("image.txt")
BitMap.save_binary(b)
b_from_bin = BitMap.load_binary("image.bin.txt")
for row in b_from_bin.grid:
    print(row)