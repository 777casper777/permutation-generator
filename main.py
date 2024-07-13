import itertools
import argparse
import os
from tqdm import tqdm
import time
from joblib import Parallel, delayed


class PermutationGenerator:
    def __init__(self, file_in, min_elem, max_elem, dir, file_out='results.txt'):
        self.file_in = os.path.join(dir, file_in)
        self.min_elem = min_elem
        self.max_elem = max_elem
        self.file_out = os.path.join(dir, file_out)
        self.elements = self.read_elements_from_file()

    def read_elements_from_file(self):
        try:
            with open(self.file_in, 'r') as file:
                elements = file.read().splitlines()
                return elements
        except FileNotFoundError:
            print(f"File {self.file_in} not found.")
            return []

    def generate_permutations(self, n):
        return list(itertools.permutations(self.elements, n))

    def save_to_file(self, permutations):
        os.makedirs(os.path.dirname(self.file_out), exist_ok=True)
        with open(self.file_out, 'w') as file:
            for permutation in permutations:
                permutation_str = ''.join(permutation)
                file.write(permutation_str + "\n")

    def run(self):
        all_permutations = []
        total_permutations = 0
        for n in range(self.min_elem, self.max_elem + 1):
            all_permutations.extend(self.generate_permutations(n))
            total_permutations += len(self.generate_permutations(n))

        start_time = time.time()
        with tqdm(total=total_permutations, desc='Generating permutations', unit='permutations') as pbar:
            pbar.set_postfix_str('Calculating...')
            results = Parallel(n_jobs=-1)(
                delayed(self.generate_permutations)(n) for n in range(self.min_elem, self.max_elem + 1))
            for permutations in results:
                for permutation in permutations:
                    pbar.update(1)
                    elapsed_time = time.time() - start_time
                    remaining_time_hours = int(
                        (total_permutations - pbar.n) * (elapsed_time / pbar.n) // 3600) if pbar.n > 0 else 0
                    remaining_time_minutes = int(
                        ((total_permutations - pbar.n) * (elapsed_time / pbar.n) % 3600) // 60) if pbar.n > 0 else 0
                    remaining_time_seconds = int(
                        ((total_permutations - pbar.n) * (elapsed_time / pbar.n)) % 60) if pbar.n > 0 else 0
                    pbar.set_description(
                        f'Generating permutations - ETA: {remaining_time_hours}h {remaining_time_minutes}m {remaining_time_seconds}s')

        self.save_to_file(all_permutations)
        print(f"\nGenerated {total_permutations} permutations and saved to {self.file_out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate permutations of elements.')
    parser.add_argument('--file_in', type=str, help='The input file containing elements, one per line.')
    parser.add_argument('--min_elem', type=int, required=True,
                        help='The minimum number of elements to include in each permutation.')
    parser.add_argument('--max_elem', type=int, required=True,
                        help='The maximum number of elements to include in each permutation.')
    parser.add_argument('--file_out', type=str, default='results.txt',
                        help='The output file to save permutations (default: results.txt).')
    parser.add_argument('--examples_dir', type=str, default='examples',
                        help='The directory where input and output files are located (default: examples).')

    args = parser.parse_args()

    generator = PermutationGenerator(args.file_in, args.min_elem, args.max_elem, args.examples_dir, args.file_out)
    generator.run()
