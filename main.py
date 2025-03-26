import itertools
import argparse
import os
import logging
from tqdm import tqdm
import math
import time

# Logging configuration
log_file = 'log.log'
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Create a file handler for logging
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S'))

# Add the file handler to the root logger
logging.getLogger().addHandler(file_handler)


class PermutationGenerator:
    """
    Class for generating permutations of elements.

    Attributes:
    - file_in (str): Path to the input file.
    - min_elem (int): Minimum number of elements in permutations.
    - max_elem (int): Maximum number of elements in permutations.
    - file_out (str): Path to the output file.
    """

    def __init__(self, file_in, min_elem, max_elem, directory, file_out='results.txt'):
        """
        Initialize the permutation generator.

        Parameters:
        - file_in (str): Input file name.
        - min_elem (int): Minimum number of elements in permutations.
        - max_elem (int): Maximum number of elements in permutations.
        - directory (str): Directory for input/output files.
        - file_out (str): Output file name.
        """
        self.warning_file_elements_count = 20
        self.warning_max_elements = 14
        self.file_in = os.path.join(directory, file_in)
        self.min_elem = min_elem
        self.max_elem = max_elem
        self.file_out = os.path.join(directory, file_out)
        self.elements = self.read_elements_from_file()

        if self.min_elem > self.max_elem:
            raise ValueError("min_elem cannot be greater than max_elem")

        if not self.elements:
            raise ValueError(f"No elements found in {self.file_in}")

    def read_elements_from_file(self):
        """
        Read elements from the input file.

        Returns:
        - list: List of elements read from the file.
        """
        if not os.path.exists(self.file_in):
            logging.error(f"File {self.file_in} not found.")
            return []

        try:
            with open(self.file_in, 'r', encoding='utf-8') as file:
                elements = [line.strip() for line in file if line.strip()]
            logging.info(f"---------------------------------------------------------------------------------")
            logging.info(f"Read {len(elements)} elements from file {self.file_in}.")
            if len(elements) > self.warning_file_elements_count:
                logging.warning(f"Warning: The input file contains {len(elements)} elements, "
                                f"which may lead to excessive memory and CPU usage.")
            if self.max_elem > self.warning_max_elements:
                logging.warning(f"Warning: The input of --max_elem contains {self.max_elem} elements, "
                                f"which may lead to excessive memory and CPU usage.")
            return elements
        except Exception as e:
            logging.error(f"Error reading file {self.file_in}: {e}")
            return []

    def count_total_permutations(self):
        """
        Calculate the total number of permutations.

        Returns:
        - int: Total number of permutations.
        """
        try:
            total = sum(
                math.perm(len(self.elements), n)
                for n in range(self.min_elem, self.max_elem + 1)
            )
            logging.info(f"Total permutations calculated: {total}")
            return total
        except Exception as e:
            logging.error(f"Error calculating total permutations: {e}")
            return 0

    def run(self):
        """
        Run the permutation generation and write to the file.
        """
        start_time = time.time()  # Track the start time
        logging.info(f"Script started at: {time.strftime('%H:%M:%S', time.localtime(start_time))}")

        total_permutations = self.count_total_permutations()
        if total_permutations == 0:
            logging.error("Total permutations calculation failed.")
            return

        logging.info(f"Total permutations: {total_permutations}")

        buffer_size = 1000  # Buffer size for writing to file
        buffer = []  # List for accumulating strings

        try:
            with open(self.file_out, 'w', encoding='utf-8') as file_out, tqdm(
                    total=total_permutations, desc="Processing permutations") as progress_bar:

                for n in range(self.min_elem, self.max_elem + 1):
                    for perm in itertools.permutations(self.elements, n):
                        buffer.append(''.join(perm) + "\n")
                        if len(buffer) >= buffer_size:
                            file_out.writelines(buffer)  # Write buffer to file
                            buffer.clear()  # Clear the buffer
                        progress_bar.update(1)

                if buffer:  # Write remaining elements at the end
                    file_out.writelines(buffer)

            end_time = time.time()  # Track the end time
            execution_time = end_time - start_time
            logging.info(f"Permutation generation completed successfully. Results saved in {self.file_out}.")
            logging.info(f"Script execution time: {execution_time:.2f} seconds.")

            # General success report in log file
            logging.info(f"Success report: Total permutations: {total_permutations}.")
            logging.info(f"Script executed in {execution_time:.2f} seconds.")

        except Exception as e:
            logging.error(f"Error during permutation generation: {e}")


def parse_arguments():
    """
    Parse command line arguments.

    Returns:
    - Namespace: Object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Generate permutations of elements.")
    parser.add_argument('--file_in', type=str, required=True, help="Input file with elements, one per line.")
    parser.add_argument('--min_elem', type=int, required=True, help="Minimum number of elements in permutations.")
    parser.add_argument('--max_elem', type=int, required=True, help="Maximum number of elements in permutations.")
    parser.add_argument('--file_out', type=str, default='results.txt', help="Output file for permutations.")
    parser.add_argument('--directory', type=str, default='examples', help="Directory for input/output files.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    try:
        generator = PermutationGenerator(args.file_in, args.min_elem, args.max_elem, args.directory, args.file_out)
        generator.run()
    except ValueError as e:
        logging.error(f"Error: {e}")
