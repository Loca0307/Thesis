import bpy
import bmesh
from mathutils import Vector, Matrix
from bpy.props import StringProperty, FloatProperty, IntProperty, PointerProperty, BoolProperty
from bpy.types import Operator, Panel, PropertyGroup
from collections import defaultdict
import math

bl_info = {
    "name": "Spread Connected Mesh Groups",
    "blender": (2, 80, 0),
    "category": "Object",
}

preview_object_prefix = "PREVIEW_"
final_object_prefix = "SPREAD_"

def update_preview_mesh(self, context):
    settings = context.scene.spread_settings
    target_obj = settings.target_object
    if not (target_obj and target_obj.type == 'MESH'):
        return

    preview_name = preview_object_prefix + target_obj.name
    preview_obj = bpy.data.objects.get(preview_name)

    if preview_obj:
        bpy.data.objects.remove(preview_obj, do_unlink=True)

    preview_obj = target_obj.copy()
    preview_obj.data = target_obj.data.copy()
    preview_obj.name = preview_name
    preview_obj.data.name = preview_name

    context.collection.objects.link(preview_obj)
    preview_obj.matrix_world = target_obj.matrix_world.copy()

    preview_obj.hide_select = True
    preview_obj.hide_render = True
    preview_obj.select_set(False)

    # Set preview material
    if "SpreadPreviewMat" not in bpy.data.materials:
        mat = bpy.data.materials.new(name="SpreadPreviewMat")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs['Base Color'].default_value = (0.0, 0.4, 1.0, 1.0)
            bsdf.inputs['Alpha'].default_value = 0.4
        mat.blend_method = 'BLEND'
        mat.shadow_method = 'NONE'
    else:
        mat = bpy.data.materials["SpreadPreviewMat"]

    if preview_obj.data.materials:
        preview_obj.data.materials[0] = mat
    else:
        preview_obj.data.materials.append(mat)

    preview_obj.display_type = 'SOLID'
    preview_obj.show_transparent = True

    bm = bmesh.new()
    bm.from_mesh(preview_obj.data)
    bm.verts.ensure_lookup_table()

    visited = set()
    groups = []

    def get_connected_group(start_vert):
        stack = [start_vert]
        group = []
        while stack:
            v = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            group.append(v)
            for e in v.link_edges:
                stack.append(e.other_vert(v))
        return group

    for v in bm.verts:
        if v not in visited:
            group = get_connected_group(v)
            groups.append(group)

    deform_layer = bm.verts.layers.deform.verify()
    vg_name = settings.vertex_group_name.strip()
    vg_index = None
    if vg_name in preview_obj.vertex_groups:
        vg_index = preview_obj.vertex_groups[vg_name].index

    body_verts = set()
    if vg_index is not None:
        for v in bm.verts:
            d = v[deform_layer]
            if vg_index in d:
                body_verts.add(v)

    def group_centroid(group):
        return sum((v.co for v in group), Vector()) / len(group)

    group_centroids = [group_centroid(g) for g in groups]
    main_index = None

    if body_verts:
        for i, group in enumerate(groups):
            if any(v in body_verts for v in group):
                main_index = i
                break

    if main_index is None:
        distances = [c.length for c in group_centroids]
        main_index = distances.index(min(distances))

    tolerance = settings.tolerance
    distance_tolerance = settings.distance_tolerance
    group_spacing_x = settings.group_spacing_x
    group_spacing_y = settings.group_spacing_y
    group_spacing_z = settings.group_spacing_z
    local_spacing_x = settings.local_spacing_x
    local_spacing_y = settings.local_spacing_y
    local_spacing_z = settings.local_spacing_z
    preserve_symmetry = settings.preserve_symmetry

    poly_groups = defaultdict(list)
    for i, group in enumerate(groups):
        if i == main_index:
            continue
        polycount = len(group)
        has_x_zero = any(abs(v.co.x) < 1e-6 for v in group)
        key = f"{round(polycount / tolerance) * tolerance}"
        if has_x_zero:
            key += "_x0"
        poly_groups[key].append(group)

    if preserve_symmetry:
        # Merge symmetrical groups
        keys = list(poly_groups.keys())
        merged = set()
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i] in merged or keys[j] in merged:
                    continue
                group_list_a = poly_groups[keys[i]]
                group_list_b = poly_groups[keys[j]]
                for ga in group_list_a:
                    for gb in group_list_b:
                        if any((va.co - Vector((-vb.co.x, vb.co.y, vb.co.z))).length < 1e-4 for va in ga for vb in gb):
                            group_list_a.extend(group_list_b)
                            merged.add(keys[j])
                            break
                    if keys[j] in merged:
                        break
        for key in merged:
            del poly_groups[key]

    sorted_keys = sorted(poly_groups.keys())
    angle_step = 2 * math.pi / max(1, len(sorted_keys))

    for i, key in enumerate(sorted_keys):
        inner_groups = poly_groups[key]
        if len(inner_groups) <= 1:
            continue  # Skip solo groups

        angle = angle_step * i
        outer_offset = Vector((
            math.sin(angle) * group_spacing_x,
            math.cos(angle) * group_spacing_y,
            math.sin(angle) * group_spacing_z
        ))

        inner_centroids = [group_centroid(g) for g in inner_groups]
        inner_center = sum(inner_centroids, Vector()) / len(inner_centroids)

        for group in inner_groups:
            group_centroid_vec = group_centroid(group)
            direction = (group_centroid_vec - inner_center).normalized()
            if direction.length == 0:
                direction = Vector((0, 0, 1))
            local_offset = Vector((
                direction.x * local_spacing_x,
                direction.y * local_spacing_y,
                direction.z * local_spacing_z
            ))
            move_vec = outer_offset + local_offset

            bmesh.ops.translate(bm, verts=group, vec=move_vec)

    bm.normal_update()
    bm.to_mesh(preview_obj.data)
    bm.free()


class SpreadSettings(PropertyGroup):
    target_object: PointerProperty(
        name="Target Object",
        type=bpy.types.Object,
        description="Object to spread mesh islands from",
        update=update_preview_mesh
    )
    vertex_group_name: StringProperty(
        name="Body Group",
        description="Name of the vertex group to leave in place",
        default="Body",
        update=update_preview_mesh
    )
    tolerance: IntProperty(
        name="Similarity Tolerance",
        description="How close polygon counts need to be to group islands together",
        default=20,
        min=1,
        update=update_preview_mesh
    )
    distance_tolerance: FloatProperty(
        name="Distance Tolerance",
        description="Maximum distance between group centroids to be grouped together",
        default=5.0,
        min=0.0,
        update=update_preview_mesh
    )
    group_spacing_x: FloatProperty(
        name="Group Spacing X",
        description="X direction distance between polygon groups",
        default=0.0,
        min=0.0,
        update=update_preview_mesh
    )
    group_spacing_y: FloatProperty(
        name="Group Spacing Y",
        description="Y direction distance between polygon groups",
        default=10.0,
        min=0.0,
        update=update_preview_mesh
    )
    group_spacing_z: FloatProperty(
        name="Group Spacing Z",
        description="Z direction distance between polygon groups",
        default=10.0,
        min=0.0,
        update=update_preview_mesh
    )
    local_spacing_x: FloatProperty(
        name="Island Spacing X",
        description="X direction spacing within a polygon group",
        default=0.0,
        min=0.0,
        update=update_preview_mesh
    )
    local_spacing_y: FloatProperty(
        name="Island Spacing Y",
        description="Y direction spacing within a polygon group",
        default=2.0,
        min=0.0,
        update=update_preview_mesh
    )
    local_spacing_z: FloatProperty(
        name="Island Spacing Z",
        description="Z direction spacing within a polygon group",
        default=2.0,
        min=0.0,
        update=update_preview_mesh
    )
    preserve_symmetry: BoolProperty(
        name="Preserve Symmetry",
        description="Ensure symmetrical groups are spread symmetrically",
        default=True,
        update=update_preview_mesh
    )


class SpreadMeshPanel(Panel):
    bl_label = "Model Exploder"
    bl_idname = "VIEW3D_PT_model_exploder"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Exploder"

    def draw(self, context):
        layout = self.layout
        settings = context.scene.spread_settings

        layout.label(text="Spread Mesh Preview")
        layout.prop(settings, "target_object")
        layout.prop(settings, "vertex_group_name")
        layout.prop(settings, "tolerance")
        layout.prop(settings, "distance_tolerance")
        layout.label(text="Group Spacing")
        layout.prop(settings, "group_spacing_x")
        layout.prop(settings, "group_spacing_y")
        layout.prop(settings, "group_spacing_z")
        layout.label(text="Island Spacing")
        layout.prop(settings, "local_spacing_x")
        layout.prop(settings, "local_spacing_y")
        layout.prop(settings, "local_spacing_z")
        layout.prop(settings, "preserve_symmetry")
        layout.operator("object.spread_connected_verts", text="Preview")
        layout.operator("object.finalize_spread_mesh", text="Finalize Mesh")


class SpreadGroups(Operator):
    bl_idname = "object.spread_connected_verts"
    bl_label = "Spread Connected Mesh Groups"

    def execute(self, context):
        update_preview_mesh(self, context)
        self.report({'INFO'}, "Preview mesh updated")
        return {'FINISHED'}


class FinalizeSpreadMesh(Operator):
    bl_idname = "object.finalize_spread_mesh"
    bl_label = "Finalize Spread Mesh"

    def execute(self, context):
        for obj in bpy.data.objects:
            if obj.name.startswith(preview_object_prefix):
                meshname = obj.name[len(preview_object_prefix):]
                obj.name = final_object_prefix + meshname
                obj.data.name = final_object_prefix + meshname
                if obj.active_material and obj.active_material.name == "SpreadPreviewMat":
                    obj.active_material = None
                obj.hide_select = False
                obj.hide_viewport = False
                obj.hide_render = False
                obj.select_set(True)
                context.view_layer.objects.active = obj

        for obj in list(bpy.data.objects):
            if obj.name.startswith(preview_object_prefix):
                if not obj.name.startswith(final_object_prefix):
                    bpy.data.objects.remove(obj, do_unlink=True)

        self.report({'INFO'}, "Spread mesh finalized")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SpreadSettings)
    bpy.types.Scene.spread_settings = PointerProperty(type=SpreadSettings)
    bpy.utils.register_class(SpreadMeshPanel)
    bpy.utils.register_class(SpreadGroups)
    bpy.utils.register_class(FinalizeSpreadMesh)


def unregister():
    bpy.utils.unregister_class(SpreadSettings)
    del bpy.types.Scene.spread_settings
    bpy.utils.unregister_class(SpreadMeshPanel)
    bpy.utils.unregister_class(SpreadGroups)
    bpy.utils.unregister_class(FinalizeSpreadMesh)


if __name__ == "__main__":
    register()