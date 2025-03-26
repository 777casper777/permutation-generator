
## Password Permutation Generator  

Sometimes you may forget your password but remember approximate phrases it consists of.  
This script helps you generate a list of possible passwords based on given elements.  
You can then use this list with Hashcat or other password recovery tools.  

### Features:  
- Useful for dictionary-based brute-force attacks and custom dictionary generation.
- Uses `tqdm` to display the progress of permutation generation.  
- Generates permutations of elements from a file, which can be useful for creating password lists for brute-force attacks.  
- If you remember only parts of your password (e.g., `7777777a!b!c?`) but recall specific symbols like `"7777777"`, `"a"`, `"b"`, `"!"`, `"c"`, `"?"`, and `"!!"`, this script can help generate all possible combinations.  
- Particularly useful when working with tools like [Hashcat](https://hashcat.net/wiki/) for dictionary attacks.  


### Legal Use Disclaimer:
This script is intended for use in legitimate password recovery and testing scenarios. Do not use this script to attempt unauthorized access to accounts or systems.



## Requirements

- Python 3.6+
- tqdm

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

Run the script `main.py` with the following command format:

```bash
python main.py --file_in example_1.txt --file_out example_1_result.txt --min_elem 1 --max_elem 6
```

### Arguments

- `--file_in <input_file>`: The input file containing elements, one per line.
- `--min_elem <min_elements>`: The minimum number of elements to include in each permutation (required).
- `--max_elem <max_elements>`: The maximum number of elements to include in each permutation (required).
- `--file_out <output_file>`: The output file to save permutations (default: results.txt).
- `--dir <directory>`: The directory where input and output files are located (default: examples).

### Example Usage

Generate permutations with elements from `example_1.txt`, using a minimum of 1 and a maximum of 7 elements per permutation, and save the results to `result_example_1.txt`:

```bash
python main.py --file_in example_1.txt --file_out result_example_1.txt --min_elem 1 --max_elem 5
```

Generate permutations with elements from `example_2.txt`, using a minimum of 1 and a maximum of 3 elements per permutation, and save the results to `result_example_2.txt`:

```bash
python main.py --file_in example_2.txt --file_out result_example_2.txt --min_elem 1 --max_elem 3
```
<div style="text-align: center; margin: 20px 0; padding: 20px; background-color: #f9f9f9; border: 2px solid #ccc; border-radius: 10px;">
  <h2 style="color: #ffb400;">👻 Support This Project 👻</h2>
  <p style="font-size: 18px;">If you find this project useful and want to support its continued development, please consider making a donation:</p>
  <p style="font-size: 16px; color: #555;">Your support will help improve the script and add new features to make it even more useful for password recovery.</p>
  <a href="https://buymeacoffee.com/777casper777" target="_blank" style="display: inline-block; padding: 10px 20px; margin: 10px 0; font-size: 20px; color: white; background-color: #ffb400; text-decoration: none; border-radius: 5px;">☕ Buy Me a Coffee</a>
  <br>
  <a href="https://www.paypal.com/ncp/payment/5CTH5JXASWEBJ" target="_blank" style="display: inline-block; padding: 10px 20px; margin: 10px 0; font-size: 20px; color: white; background-color: #0070ba; text-decoration: none; border-radius: 5px;">
    💰 Donate via PayPal
  </a>
</div>




