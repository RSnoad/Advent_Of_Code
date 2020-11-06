from itertools import chain

# Function that takes a row and returns the difference between its largest and smallest values.
def difference(row):
    row = row.split()
    row = list(map(int, row))
    return max(row) - min(row)

# Function that uses the difference function to calculate the checksum of any number of input rows.
def checksum(*args):
    total = 0
    for i in args:
        total += difference(i)
    return total

# Function that takes an input row, finds the only present evenly divisible pair value, and returns that division.
def evendivision(row):
    row = row.split()
    row = list(map(int, row))

    for listiterator in range(0, len(row) + 1):
        # Loop over every element in the list, other than the currently selected element.
        looprange = chain(range(0, listiterator), range(listiterator + 1, len(row)))
        for digititerator in looprange:
            if row[listiterator] % row[digititerator] == 0:
                return int(row[listiterator] / row[digititerator])

# Takes any number of input rows and returns the sum of the even divisions. (Very similar to checksum function above,
# only taking different function, could be merged?)
def divisionsum(*args):
    total = 0
    for i in args:
        total += evendivision(i)
    return total


print(divisionsum("5 9 2 8", "9 4 7 3", "3 8 6 5"))

row1 = "4168 3925 858 2203 440 185 2886 160 1811 4272 4333 2180 174 157 361 1555"
row2 = "150	111	188	130	98	673	408	632	771	585	191	92	622	158	537	142"
row3 = "5785	5174	1304	3369	3891	131	141	5781	5543	4919	478	6585	116	520	673	112"
row4 = "5900	173	5711	236	2920	177	3585	4735	2135	2122	5209	265	5889	233	4639	5572"
row5 = "861	511	907	138	981	168	889	986	980	471	107	130	596	744	251	123"
row6 = "2196	188	1245	145	1669	2444	656	234	1852	610	503	2180	551	2241	643	175"
row7 = "2051	1518	1744	233	2155	139	658	159	1178	821	167	546	126	974	136	1946"
row8 = "161	1438	3317	4996	4336	2170	130	4987	3323	178	174	4830	3737	4611	2655	2743"
row9 = "3990	190	192	1630	1623	203	1139	2207	3994	1693	1468	1829	164	4391	3867	3036"
row10 = "116	1668	1778	69	99	761	201	2013	837	1225	419	120	1920	1950	121	1831"
row11 = "107	1006	92	807	1880	1420	36	1819	1039	1987	114	2028	1771	25	85	430"
row12 = "5295	1204	242	479	273	2868	3453	6095	5324	6047	5143	293	3288	3037	184	987"
row13 = "295	1988	197	2120	199	1856	181	232	564	1914	1691	210	1527	1731	1575	31"
row14 = "191	53	714	745	89	899	854	679	45	81	726	801	72	338	95	417"
row15 = "219	3933	6626	2137	3222	1637	5312	238	5895	222	154	6649	169	6438	3435	4183"
row16 = "37	1069	166	1037	172	258	1071	90	497	1219	145	1206	143	153	1067	510"

# There has to be a better way than this.
print(checksum(row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15, row16))
print(divisionsum(row1, row2, row3, row4, row5, row6, row7, row8, row9,row10, row11, row12, row13, row14, row15, row16))
