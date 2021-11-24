from management import queue, task_allocation


class ExecutionManager(object):
    def __init__(self):
        # Todo: add event stucture to recognize button press event from listner
        pass

    def import_models(self, paths):
        queue_manager = queue.QueueManager(paths)
        allocator = task_allocation.TaskAllocator(queue_manager.staged_files)
        for model in allocator.staged_models:
            self.execute_model(model)

    @staticmethod
    def execute_model(model):
        model.initialize()
        model.generate()
        model.animate()
        model.structure()
