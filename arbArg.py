def write_multiple_items(file, separator, *args):
	file.write(separator.join(args))

# print write_multiple_items

print range(3,6)
args = [3,6]
print range(*args)