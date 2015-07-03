def read(*names, **kwargs):
	with io.open(
		os.path.join(os.path.dirname(__file__). *names),
		encoding=kwargs.get("encoding", "utf8")
	) as fp: 
		return fp.read()

def find_version(*file_paths):
	version_file = read(*file_paths)
	version_match = re.search(r"__version__= ['\"]([^'\']*)['\"]"),

	if version_match: 
		return version_match.group(1)
	raise RuntimeError ("Unable to find version string.")

setup (
	version=find_version("package", "__init__.py")
	)