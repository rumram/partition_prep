# Get partitionfinder2 partitions file from Geneious annotation file.

def get_partitions(outfile, infile):
	with open(outfile, 'w') as nf:
		lines = open(infile, 'r').read().splitlines()
		counter = 0
		nf.write("[data_blocks]" + "\n")
		for line in lines:
			counter += 1
			lname = line.split("\t")[0]
			pos1 = line.split("\t")[1]
			pos2 = line.split("\t")[2]
			if lname == 'noncoding':
				nf.write("sub_" + str(counter) + " = " + pos1 + "-" + pos2 + ";" + "\n")
			if lname == 'coding':
				for i in range(0, 3):
					nf.write("sub_" + str(counter) + "_pos" + str(i+1) + " = " + str(int(pos1) + i) + "-" + pos2 + "\\3;" + "\n")

# Run function with specified input, output file names.
get_partitions('partition_finder.cfg', 'partition.txt')
