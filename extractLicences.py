import sys
import json
from ecosystemDataManager.ecosystemDataManager import EcosystemDataManager

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage:", sys.argv[0], "<ecosystem> [<licenses>]")
		sys.exit(1)
	if len(sys.argv) > 3:
		licenses = sys.argv[2]
	else:
		print("licenses not provided. using default.")
		licenses = "licenses.json"
	try:
		with open(licenses) as file:
			extracted = json.load(file)
			print("licenses loaded")
	except Exception as e:
		print("licenses not loaded. continuing.")
			extracted = []
	ecosystem = sys.argv[1]
	ecosystemDataManager = EcosystemDataManager(ecosystem)
	for package in ecosystemDataManager.getPackages():
		for version in package.getVersions():
			for license in version.getLicenses():
				extracted.append(license.getName())
	extracted = set(extracted)
	extracted = list(extracted)
	with open(licenses, "w") as file:
		print("writing")
		file.write(json.dumps(extracted, separators=(',\n', ':')))
		print("written")