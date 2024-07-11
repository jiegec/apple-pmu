import plistlib
import sys
import glob
import os

for file in glob.glob('/usr/share/kpep/*.plist'):
	res = []
	with open(file, 'rb') as f:
		data = plistlib.load(f)
		for key in data['system']['cpu']['events']:
			value = data['system']['cpu']['events'][key]
			if 'number' in value:
				res.append((key, value['number'], value['description']))

	basename = os.path.basename(file)
	basename = basename.removesuffix('.plist')
	out = open(f'{basename}.md', 'w')

	marketing_name = data['system']['cpu']['marketing_name']
	print(f'Marketing name: {marketing_name}', file=out)

	print('', file=out)
	print('Performance counters:', file=out)
	res = sorted(res, key=lambda x:x[0])
	for key, id, desc in res:
		print(f'- {key} ({id}, 0x{id:x}): {desc}', file=out)
