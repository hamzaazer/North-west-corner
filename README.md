# North-West Corner Method

A Python implementation of the North-West Corner method to produce an initial feasible solution for the transportation problem. Use this README as a starting point — if the repository has a different purpose or specific filenames/functions, tell me and I will adapt the README.

## Table of contents
- About
- Features
- Requirements
- Installation
- Usage
  - As a library
  - As a script / CLI
- Example
- Algorithm overview
- Complexity
- Testing
- Contributing
- License

## About
This project provides code to compute an initial feasible allocation for transportation problems using the North-West Corner rule. It is intended for education, quick prototyping, and as a preprocessing step before optimization/refinement (e.g., MODI method).

## Features
- Compute initial allocation given supply and demand
- Works with rectangular cost/allocation matrices
- Returns allocation matrix and (optionally) basic feasibility checks

## Requirements
- Python 3.8+
- (Optional) NumPy for convenient matrix handling — code can be pure-Python as well

## Installation
Clone the repository and (optionally) create a virtual environment:

```bash
git clone https://github.com/hamzaazer/North-west-corner.git
cd North-west-corner
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt  # if present
```

## Usage

As a library (recommended)
- Import the solver function/class from the package/module (replace names with the actual module in this repo):

```python
from north_west_corner import north_west_corner
supply = [20, 30, 25]
demand = [10, 25, 15, 25]
allocation = north_west_corner(supply, demand)
print(allocation)  # allocation as a matrix or list of lists
```

As a script / CLI
- If the repo contains a CLI entrypoint (e.g., north_west_corner.py), run:

```bash
python north_west_corner.py --supply 20,30,25 --demand 10,25,15,25
```

- Or provide input via CSV/JSON files (adapt to the repo’s actual input format).

## Example (conceptual)
Given supply = [20, 30] and demand = [10, 15, 25]:
- Start at the north-west (top-left) cell
- Allocate min(current_supply, current_demand)
- Subtract allocation from supply and demand, move right if supply exhausted or down if demand exhausted
- Repeat until all supplies and demands are satisfied

A simple example in code (adapt to your implementation):

```python
def north_west_corner(supply, demand):
    n_rows, n_cols = len(supply), len(demand)
    alloc = [[0]*n_cols for _ in range(n_rows)]
    i = j = 0
    s = supply.copy()
    d = demand.copy()
    while i < n_rows and j < n_cols:
        q = min(s[i], d[j])
        alloc[i][j] = q
        s[i] -= q
        d[j] -= q
        if s[i] == 0 and i < n_rows - 1:
            i += 1
        elif d[j] == 0 and j < n_cols - 1:
            j += 1
        else:
            # handle corner cases where both zero or last row/col
            if s[i] == 0 and d[j] == 0:
                if i < n_rows - 1:
                    i += 1
                elif j < n_cols - 1:
                    j += 1
                else:
                    break
    return alloc
```

## Algorithm overview
The North-West Corner rule fills the transportation table starting at the top-left cell and proceeds by allocating as much as possible to each visited cell, moving east or south as supplies or demands become zero. It is simple and fast but does not guarantee optimality (only a starting solution).

## Complexity
Time complexity: O(m + n) allocations for an m x n transportation table (practically O(m*n) in worst-case scanning).
Space complexity: O(m*n) for the allocation matrix.

## Testing
- If tests are present, run:

```bash
pytest
```

- Add unit tests for edge cases:
  - Imbalanced supply/demand (should be balanced by adding a dummy row/column)
  - Single row / single column
  - Zero supply or demand entries

## Contributing
- Fork the repo
- Create a feature branch
- Add tests and documentation for new features
- Open a pull request describing your changes

Please include real input/output examples and expected behavior when adding new features.

## License
No license is specified here. If you want a license added (MIT/Apache/BSD/etc.), tell me which one and I can add a LICENSE file and update this README.

---

Would you like me to:
- adapt this README to match specific filenames/functions in the repo (tell me module or function names), or
- commit this README.md directly to hamzaazer/North-west-corner (and if so, which license and branch)?