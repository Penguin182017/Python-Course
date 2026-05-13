outputFile = open("UpdatedFile.txt", "w")

input = open("Repeted.txt", "r")

lines_seen_so_far = set()
print("Eliminating duplicate lines....")

