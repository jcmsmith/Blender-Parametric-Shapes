import math
import bpy
import bmesh

#math constants
pi = math.pi
sin = math.sin
cos = math.cos

period = 2*pi

#Update t based on frame rate
fps = bpy.context.scene.render.fps
delta = ((2*pi)/fps)

def calc_x(t):
    return 2 * cos(t) + 3 * sin(4 * t)

def calc_y(t):
    return 3 * sin(t) + 2 * cos(4 * t)



print("-------------------------------------------------------------")

#Create cube to serve as shape object and immediately enter edit mode
shape = bpy.ops.mesh.primitive_cube_add(enter_editmode=True);

#Delete all vertices except one
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.mesh.select_random(ratio=0.875)
bpy.ops.mesh.delete()

#Create bmesh to access vertex data
obj_data = bpy.context.object.data
bm = bmesh.from_edit_mesh(obj_data)
bm.verts.ensure_lookup_table()
vertex = bm.verts[0]

#Subtract the coordinates of the original point from its current point to move while maintaining offset - probably unnecessary here we're just trying to move it to the origin
v_coords = vertex.co.copy()
v_coords -= v_coords
    
#Update mesh data
obj_data.update()
bm.verts.ensure_lookup_table()

escape = 0
t = 0

while t < period:
    x = calc_x(t)
    y = calc_y(t)
    
    #vertex.co = [x,y,0]
    print("vertex", vertex.co)
    
    t += delta
    
    ++escape
    
    if(escape >= 420):
        print('escaped')
        break

print('done')