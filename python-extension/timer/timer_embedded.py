import os, sys
import time
import json
import datetime
import psutil

class timeit():

    def __init__(self):
        get_pure = lambda x: os.path.splitext(os.path.basename(x))[0]
        self.script_name = get_pure(sys.argv[0])
        self.executor_name = get_pure(sys.executable)
        self.start_time = 0
        self.end_time = 0

    def __enter__(self):
        self.start_time = time.time_ns()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time_ns()
        if exc_val:
            raise exc_val
        result_time = (self.end_time - self.start_time) / 1e9
        self.update_results(result_time)

    def update_results(self, result_time):
        with open('../result/result.json','r',encoding='utf-8') as f:
            prev_results = json.loads(f.read())

        item_pointer = prev_results.setdefault(self.executor_name, {
            'executor_name': self.executor_name,
            'version': 'Reserved',
            'items': {}
        })
        item_pointer = item_pointer['items']
        current_test_item_list = item_pointer.setdefault(self.script_name, [])
        current_test_item_list.append({
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'time': result_time,
            'mem': psutil.Process(os.getpid()).memory_full_info().uss
        })
        while len(current_test_item_list) > 100:
            current_test_item_list.pop(0)

        with open('../result/result.json','w',encoding='utf-8') as f:
            f.write(json.dumps(prev_results, indent=2))
