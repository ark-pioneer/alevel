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

        image_width = 3
        # then, create the grid as a 2d list of 8bit bin strings. Later convert each back to pixel colours.
        # so, chunk the rest of the data into sets of 3 strings each of length 8 (because 8bit bin numbers)
        # create the grid outer list
        lines = []
        # variable controls iteration
        index = 0
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

# Create an instance of bitmap using data from a file
b = BitMap.load("image.txt")

# Create an instance of bitmap with a grid
b2 = BitMap([
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
    ])

# draw a vertical line, 3 pixels, down from top left
b.draw_y("G", [0,0], 3, "DOWN")

# draw a vertical line, 2 pixels, up from bottom middle
b2.draw_y("K", [1,2], 2, "UP")

# save the file with its default file name
BitMap.save(b)

# save the file with a specific file name
BitMap.save(b2, "image2.txt") 

# save the file as a binary string with a specific file name
BitMap.save_binary(b2, "image2.txt") 

# load the file from a binary string and save the contents as a CSV in a new file
b_bin = BitMap.load_binary("image2.bin.txt")
BitMap.save(b_bin, "image3.txt")