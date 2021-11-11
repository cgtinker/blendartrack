from utils.blend import user


class TaskManager(object):
    def __init__(self, staged_models):
        self.staged_models = staged_models

    def execute(self):
        for model in self.staged_models:
            self.execute_model(model)

    @staticmethod
    def execute_model(model):
        model.initialize()
        model.generate()
        model.animate()
        model.structure()
