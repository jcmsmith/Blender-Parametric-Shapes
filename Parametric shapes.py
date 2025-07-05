import math
import mathutils
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

def calculate_points(period = 2*pi):
    escape = 0
    t = 0
    vertices = []

    while t < period:
        if(escape >= 420):
            print('oops, escaped')
            break;
        
        x = calc_x(t)
        y = calc_y(t)
        
        coordinates = mathutils.Vector([x,y,0])
        
        vertices.append(coordinates)
        t += delta;
        
        escape += 1;
        
    return vertices;


print("-------------------------------------------------------------")

#Create object, enter edit mode & delete existing vertices
shape = bpy.ops.mesh.primitive_cube_add(enter_editmode=True);
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.delete()

#Create bmesh to access and manipulate vertex properties
obj_data = bpy.context.object.data
bm = bmesh.from_edit_mesh(obj_data)
bm.verts.ensure_lookup_table()

points = calculate_points();
for point in points:
    newvert = bm.verts.new(point)
    
#Update mesh data
obj_data.update()
bm.verts.ensure_lookup_table()

