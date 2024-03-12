# Decision Tree Learning for Classification

Welcome to the Decision Forest Classification project! This project implements a decision tree learning algorithm for classification tasks, offering both optimized and randomized versions. The decision forest is a collection of decision trees, and it classifies instances based on their features.

## Project Structure

1. **Decision Tree Implementation:** The core decision tree learning algorithm is implemented in `decision_forest.py`. It includes functions for reading input files, calculating entropy, choosing attributes, and constructing decision trees.

2. **Decision Tree Class:** The `Node` class represents a node in the decision tree. It can be an internal node with an attribute and threshold or a leaf node with a distribution of class labels.

3. **Decision Tree Learning Algorithms:**
   - `DTL`: Decision Tree Learning for the optimized version.
   - `DTLRandom`: Decision Tree Learning for the randomized version.
   - `Forest`: Decision Forest, combining multiple decision trees for classification.

4. **Utility Functions:**
   - `LabelArray`: Generates a global array of unique class labels.
   - `read_file`: Reads a file and returns a list of examples.
   - `SelectColumn`: Selects a column (attribute) from the dataset.
   - `Distribution`: Calculates the distribution of class labels.

5. **Testing Functions:**
   - `TestingTree`: Tests a single decision tree on a given instance and prints the result.
   - `TestingTreeForest`: Tests a forest of decision trees on an instance and returns the distribution.
   - `Testing`: Tests a decision tree on a set of instances and prints the accuracy.

## How to Run

To run the project, use the following command:

```bash
python decision_forest.py <training-file> <testing-file> <option>
```

- `<training-file>`: Path to the training file containing labeled examples.
- `<testing-file>`: Path to the testing file containing examples for evaluation.
- `<option>`: Choose the learning algorithm option ("optimized," "randomized," "forest3," or "forest15").

## Example Usage

```bash
python decision_forest.py training_data.txt testing_data.txt optimized
```

This example runs the decision forest algorithm using the optimized learning approach. Feel free to explore other options and datasets.

## Options
- **optimized**: Decision Tree Learning using the optimized version.
- **randomized**: Decision Tree Learning using the randomized version.
- **forest3**: Decision Forest with 3 decision trees.
- **forest15**: Decision Forest with 15 decision trees.

