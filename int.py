class Item:
    @classmethod
    def read_file(kdd):
        with open("volinfo.txt", 'r') as f:
            reader = txt.DictReader(f)

    for item in reader:
        print(item)
read_file(kdd)
