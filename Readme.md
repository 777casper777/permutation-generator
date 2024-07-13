# Permutation Generator

- This script generates permutations of elements from a file, which can be useful for creating password sets for brute-force attacks. 
  For instance, if you've forgotten your password but remember certain symbols like "7777777", "a", "b", "!", "c", "?", and "!!", 
  this script can help generate all possible combinations. 
  This can be particularly useful when working with tools like [Hashcat](https://hashcat.net/wiki/) using dictionary attack methods.


- The code uses tqdm to display the progress of permutation generation.
- It utilizes joblib.Parallel for parallel execution of permutation generation, which speeds up the process on multi-core systems.

## Requirements

- Python 3.6+
- joblib
- tqdm

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

Run the script `main.py` with the following command format:

```bash
python main.py --file_in elements.txt --min_elem 1 --max_elem 3
```

### Arguments

- `--file_in <input_file>`: The input file containing elements, one per line.
- `--min_elem <min_elements>`: The minimum number of elements to include in each permutation (required).
- `--max_elem <max_elements>`: The maximum number of elements to include in each permutation (required).
- `--file_out <output_file>`: The output file to save permutations (default: results.txt).
- `--examples_dir <examples_directory>`: The directory where input and output files are located (default: examples).

### Examples

Generate permutations with elements from `elements.txt`, using a minimum of 1 and a maximum of 3 elements per permutation:

```bash
python main.py --file_in elements.txt --min_elem 1 --max_elem 3
```

### Special Examples

```bash
python main.py --file_in example_1.txt --file_out result_example_1.txt --min_elem 1 --max_elem 7
python main.py --file_in example_2.txt --file_out result_example_2.txt --min_elem 1 --max_elem 3
```

```

