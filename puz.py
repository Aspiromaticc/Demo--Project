def spiral(kay):
    brymo = kay * 3
    wizkid = brymo / 2
    justin = wizkid / 3
    return brymo, wizkid, justin
kay = 4
free = spiral(kay)
print("""
Brymo's {} songs garnered 24, 000 streams. While Wizkid's
6 songs had 2.4 Billion streams
But Davido beat them all with his {}  songs
""".format(*free))
