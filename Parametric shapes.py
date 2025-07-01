import math
import bpy
import bmesh

print("-------------------------------------------------------------")


#Create new object with mesh
mesh = bpy.data.meshes.new(name="shape");
shape = bpy.data.objects.new("shape", mesh);

#Select the new object
bpy.context.collection.objects.link(shape)
shape.select_set(True)

#Switch to edit mode
if bpy.context.mode != "EDIT_MESH" and bpy.ops.object.mode_set.poll():
    bpy.ops.object.mode_set(mode="EDIT");

#Delete all vertices except one    
bpy.ops.mesh.primitive_cube_add();
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

#math constants
pi = math.pi
sin = math.sin
cos = math.cos

def calc_x(t):
    return 2 * cos(t) + 3 * sin(4 * t)

def calc_y(t):
    return 3 * sin(t) + 2 * cos(4 * t)

#Update t based on render frame rate
fps = bpy.context.scene.render.fps
delta = pi/fps

for t in range(0, 100):
    x = calc_x(t)
    y = calc_y(t)
    
    vertex.co = [x,y,0]
    print("vertex", vertex.co)
    
    t += delta
    
    if(t >= 2*pi):
        break