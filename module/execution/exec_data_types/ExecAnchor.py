def exec_anchor(model):
    for point in model:
        point.create_point(name="reference", size=1)