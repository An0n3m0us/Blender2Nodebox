import bpy
from bpy import context

filepath = bpy.path.abspath("//blender.lua")
bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)

with open(filepath, 'w') as f:
	for x in context.selected_objects:
		obj = x
		mesh = obj.data
		face1 = obj.matrix_world*mesh.vertices[2].co*16 + obj.matrix_world*mesh.vertices[3].co*16 + obj.matrix_world*mesh.vertices[6].co*16 + obj.matrix_world*mesh.vertices[7].co*16
		face1 = str(round(face1[0]/4, 1))
		face2 = obj.matrix_world*mesh.vertices[1].co*16 + obj.matrix_world*mesh.vertices[2].co*16 + obj.matrix_world*mesh.vertices[5].co*16 + obj.matrix_world*mesh.vertices[6].co*16
		face2 = str(round(face2[2]/4, 1))
		face3 = obj.matrix_world*mesh.vertices[4].co*16 + obj.matrix_world*mesh.vertices[5].co*16 + obj.matrix_world*mesh.vertices[6].co*16 + obj.matrix_world*mesh.vertices[7].co*16
		face3 = str(round(face3[1]/4, 1))
		face4 = obj.matrix_world*mesh.vertices[0].co*16 + obj.matrix_world*mesh.vertices[1].co*16 + obj.matrix_world*mesh.vertices[4].co*16 + obj.matrix_world*mesh.vertices[5].co*16
		face4 = str(round(face4[0]/4, 1))
		face5 = obj.matrix_world*mesh.vertices[0].co*16 + obj.matrix_world*mesh.vertices[3].co*16 + obj.matrix_world*mesh.vertices[4].co*16 + obj.matrix_world*mesh.vertices[7].co*16
		face5 = str(round(face5[2]/4, 1))
		face6 = obj.matrix_world*mesh.vertices[0].co*16 + obj.matrix_world*mesh.vertices[1].co*16 + obj.matrix_world*mesh.vertices[2].co*16 + obj.matrix_world*mesh.vertices[3].co*16
		face6 = str(round(face6[1]/4, 1))
		faces = "{" + face1 + "/16, " + face2 + "/16, " + face3 + "/16, " + face4 + "/16, " + face5 + "/16, " + face6 + "/16}, -- " + x.name
		f.write("\n")
