from . import cgt_queue, task_allocation
from ..import_models import iCustomData


class ExecutionManager(object):
    def __init__(self):
        # Todo: add event stucture to recognize button press event from listner
        pass

    def import_models(self, paths):
        # structure the data by setting up a queue
        queue_manager = queue.QueueManager(paths)
        # get the import models of the staged data
        allocator = task_allocation.TaskAllocator(queue_manager.staged_files)
        # execute the models
        for model in allocator.staged_models:
            self.execute_model(model)

    @staticmethod
    def execute_model(model: iCustomData):
        model.initialize()
        model.generate()
        model.animate()
        model.structure()
