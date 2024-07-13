# Permutation Generator

This script generates arrangements of elements from a file, which can be useful for creating password sets for brute-force attacks.

## Requirements

- Python 3.6+
- joblib
- tqdm

Install dependencies using `pip`:

pip install -r requirements.txt


## Usage

Run the script `main.py` with the following command format:

python main.py elements.txt --min_elem=1 --max_elem=3


### Arguments

- `--file_in`: Input file containing elements, one per line.
- `--min_elem`: Minimum number of elements per permutation.
- `--max_elem`: Maximum number of elements per permutation.
- `--file_out`: (Optional) Output file to save permutations (default: result_elements.txt).

### Example

Generate permutations with elements from `elements.txt`, using a minimum of 1 and a maximum of 3 elements per permutation:


### Special example
python main.py --file_in=files/dict_BTC_small.txt --file_out=files/pass_BTC_small.txt --min_elem=1 --max_elem=9
python main.py --file_in=files/dict_BTC.txt --file_out=files/pass_BTC.txt --min_elem=1 --max_elem=9
python main.py --file_in=files/dict_wallet.txt --file_out=files/pass_wallet.txt --min_elem=1 --max_elem=9
python main.py --file_in=files/dict_wallet_small.txt --file_out=files/pass_wallet_small.txt --min_elem=1 --max_elem=9
python main.py --file_in=files/dict_core.txt --file_out=files/pass_core.txt --min_elem=1 --max_elem=9
