import time
import copy
import importlib
import argparse


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f"> {(te - ts) * 1000} ms")
        return result

    return timed


class Runner:
    def __init__(self, category: str, question: str):
        self.question = question
        self.path = f"{category}.{question}"
        self.samples = self.load("data", "samples")

    def load(self, file, function):
        full_path = f"{self.path}.{file}"
        mod = importlib.import_module(full_path)
        return getattr(mod, function)

    def verify(self, func):
        samples = copy.deepcopy(self.samples)
        for sample in samples:
            result = func(**sample["input"])
            answer = sample["output"]
            passed = result == answer
            if not passed:
                print(f"{passed}: Expect {answer} but got {result}")

    @timeit
    def single(self, file):
        func = self.load(file, self.question)
        self.verify(func)

    def all(self, recipes: list):
        for recipe in recipes:
            print(f"Timing {recipe}:")
            self.single(recipe)


def main(args):
    r = Runner(args.category, args.question)
    r.all(args.recipe)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test")
    parser.add_argument(
        "-c",
        "--category",
        type=str,
        help="select category",
        dest="category",
        required=True,
    )
    parser.add_argument(
        "-q",
        "--question",
        type=str,
        help="select question",
        dest="question",
        required=True,
    )
    parser.add_argument(
        "-r",
        "--recipe",
        type=str,
        help="select recipes",
        nargs="+",
        required=True,
    )
    main(parser.parse_args())
