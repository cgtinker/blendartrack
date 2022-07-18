import bpy


class CompositingTree:
    def __init__(self):
        bpy.context.scene.use_nodes = True
        self.tree = bpy.context.scene.node_tree
        self.clear_default_nodes()
    
    def clear_default_nodes(self):
        for node in self.tree.nodes:
            self.tree.nodes.remove(node)
        
    def new_node(self, node_type, location):
        node = self.tree.nodes.new(type=node_type)
        node.location = location
        return node
  
    def connect_nodes(self, output, input):
        links = self.tree.links
        link = links.new(output[0].outputs[output[1]], input[0].inputs[input[1]])


def get_active_movie_clip():
    camera = bpy.context.scene.camera
    clip = None
    active = False
    
    if camera.data.show_background_images is True and camera.data.background_images[0].clip is not None:
        for movie in bpy.data.movieclips:
            if movie.filepath == camera.data.background_images[0].clip.filepath:
                print(clip, movie)
                clip = movie 
                active = True

    return clip, active


def set_internal_compositing(compositor):
    clip = compositor.new_node('CompositorNodeMovieClip', [-400, 200])
    scale = compositor.new_node('CompositorNodeScale', [-200, 200])
    scale.space = 'RENDER_SIZE'
    render = compositor.new_node('CompositorNodeRLayers', [-400, -200])
    alpha_over = compositor.new_node('CompositorNodeAlphaOver', [200, 0])  
    output = compositor.new_node('CompositorNodeComposite', [400, 0])
        
    compositor.connect_nodes([clip, 0], [scale, 0])
    compositor.connect_nodes([scale, 0], [alpha_over, 1])
    compositor.connect_nodes([render, 0], [alpha_over, 2])
    compositor.connect_nodes([alpha_over, 0], [output, 0])
    

    movie_clip, active= get_active_movie_clip()
    if active:
        clip.clip = movie_clip


def set_external_compositing(compositor):
    clip = compositor.new_node('CompositorNodeMovieClip', [-400, 200])
    scale = compositor.new_node('CompositorNodeScale', [-200, 200])
    scale.space = 'RENDER_SIZE'
    render = compositor.new_node('CompositorNodeRLayers', [-400, -200])
    output = compositor.new_node('CompositorNodeOutputFile', [400, 0])
    
    output.file_slots.remove(output.inputs[0])
    output.file_slots.new("movie")
    output.file_slots.new("render")
    output.file_slots.new("alpha")
    output.file_slots.new("depth")
    
    compositor.connect_nodes([clip, 0], [scale, 0])
    compositor.connect_nodes([scale, 0], [output, 0])
    compositor.connect_nodes([render, 0], [output, 1])
    compositor.connect_nodes([render, 1], [output, 2])
    compositor.connect_nodes([render, 2], [output, 3])    

    movie_clip, active= get_active_movie_clip()
    if active:
        clip.clip = movie_clip


def setup_render():
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.image_settings.color_mode = 'RGBA'

