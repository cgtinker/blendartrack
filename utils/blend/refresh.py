def objects(objs, frame, scene):
    scene.frame_current = frame
    for obj in objs:
        obj.update_tag(refresh={'OBJECT'})
    scene.update_android()


def scene(scene):
    scene.refresh()


def object(obj):
    obj.update_tag(refresh={'OBJECT'})


def time(obj):
    obj.update_tag(refresh={'TIME'})


def data(obj):
    obj.update_tag(refresh={'DATA'})
