import time
import copy
import importlib


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print(f'{method.__name__}: {(te - ts) * 1000} ms')
        return result
    return timed


class Runner:
    def __init__(self, category: str, question: str):
        self.question = question
        self.path = f'{category}.{question}'
        self.samples = self.load('data', 'samples')

    def load(self, file, function):
        full_path = f'{self.path}.{file}'
        mod = importlib.import_module(full_path)
        return getattr(mod, function)

    def verify(self, func):
        samples = copy.deepcopy(self.samples)
        for sample in samples:
            result = func(**sample['input'])
            answer = sample['output']
            passed = result == answer
            if not passed:
                print(f"{passed}: Expect {answer} but got {result}")

    @timeit
    def single(self, file):
        func = self.load(file, self.question)
        self.verify(func)

    def all(self, menu: list):
        for item in menu:
            print(f'Timing {item}:')
            self.single(item)


if __name__ == "__main__":
    category = 'array'
    question = 'nonConstructibleChange'
    menu = ['1', '2']
    r = Runner(category, question)
    r.all(menu)
