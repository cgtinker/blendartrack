from module.preperation.importing import ImportData
from module.preperation.queue import QueuePosition
import importlib

importlib.reload(ImportData)
importlib.reload(QueuePosition)


class QueueData:
    def __init__(self, model, title, valid, queue):
        self.model = model
        self.title = title
        self.valid = valid
        self.queue = queue

    def __lt__(self, other):
        return self.queue < other.queue

    def print_contents(self):
        print(self.title, "|| valid:", self.valid, "|| queue position:", self.queue)


def get_valid_files(paths):
    queue_data = []
    for path in paths:
        process_data_for_queue(queue_data, path)

    queue_data.sort()
    return queue_data
    # execute_queue(queue_data)


# processing the json data for further import and get the queue position
def process_data_for_queue(models, path):
    model_data, title, valid = ImportData.import_tracking_data(path)
    if valid is True:
        queue = QueuePosition.get_queue_position(title)
        append_queue_data(model_data, models, queue, title, valid)


# the queue position data contains a value and a title for sorting
def append_queue_data(model_data, models, queue, title, valid):
    if queue != -1:
        data = QueueData(model=model_data, title=title, valid=valid, queue=queue)
        models.append(data)
