# svgwriteで生成

# viewBox="-21.5 -21.5 100 100"
import svgwrite

# dwg = svgwrite.Drawing('Circle.svg', profile='tiny')
dwg = svgwrite.Drawing('react.svg')
marker = dwg.marker(insert=(5,5), size=(10,10))

marker.add(dwg.circle((5, 5), r=5, fill='red'))
dwg.defs.add(marker)
line = dwg.add(dwg.polyline(
[(10, 10), (50, 20), (70, 50), (100, 30)],
stroke='black', fill='none'))
line.set_markers(marker)
line['marker'] = marker.get_funciri()
dwg.save()