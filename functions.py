from xml.dom import minidom
import svg.path

# Read the SVG file and separate SVG paths commands in lists
def read_svg_paths(path_to_svg):
	doc = minidom.parse(path_to_svg)
	paths_colors = [path.getAttribute('style').split(';')[1].split(':')[1][5:][:-1].split(',') for path in doc.getElementsByTagName('path')]
	paths_colors = [[int(path_color[0]), int(path_color[1]), int(path_color[2]), int(path_color[3])] for path_color in paths_colors]
	path_commands = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
	doc.unlink()

	new_paths = []
	path_color_i = 0;
	for path_string in path_commands:
		path = svg.path.parse_path(path_string)

		new_path = svg.path.Path()
		for e in path:
			new_path.insert(-1, e)
		new_paths.append([new_path, paths_colors[path_color_i]])
		path_color_i+=1
		new_path = svg.path.Path()

		# new_path = svg.path.Path()
		# for e in path:
		# 	new_path.insert(-1, e)
		# 	if isinstance(e, svg.path.Close):
		# 		new_paths.append([new_path, paths_colors[path_color_i]])
		# 		path_color_i+=1
		# 		new_path = svg.path.Path()

	return new_paths
