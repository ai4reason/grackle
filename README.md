# Grackle

Grackle is an automated system for invention of a set of **good-performing** and **complementary** configurations of an arbitrary parametrized algorithm.

## Quick Install

Clone the repository from *github* and install Grackle through `pip`.

```bash
git clone https://github.com/ai4reason/grackle.git
cd grackle
pip install . 
```

### Developers installation notes

This is a manual installation for developers and it is intended to be done instead of the standard `pip` installation.
First, clone the repository:

```bash
git clone https://github.com/ai4reason/grackle.git
cd grackle
```

The scripts from the directory `bin` and `paramils` must be in some `PATH` directory.  For example, run the following from the main repository directory `grackle`, or create symbolic links from some `PATH` directory pointing to the repository files in `bin` and `paramils`.

```bash
export PATH=$PATH:$PWD/bin:$PWD/paramils
```

To manually install the Grackle Python package, create a symbolic link from your local user Python packages pointing to the directory `grackle/grackle` in the repo.  This will make the development easier because you will not need to install the package again after every change in the repository.
Typically, this can be done as follows (provided you use Python 3.11, and you are in the main `grackle` repository directory):

```bash
ln -s $PWD/grackle $HOME/.local/lib/python3.11/site-packages
```

Note that the link must point to the "inner" `grackle` directory (inside the repository, `grackle/grackle`).

## Running Grackle

Grackle is launched by the command `fly-grackle.py` which takes as the only parameter a configuration file
typically named `grackle.fly`.

In order to launch Grackle, you need the following.

1. A set of benchmark problems for which you want to invent new strategies.
2. Some initial strategies to start with (at least 2).

### Configuration file `grackle.fly`

The configuration file provides all necessary information about the experiment to be ran.
Typically, it looks as follows.

```
cores = 56
tops = 50
best = 3
rank = 1
inits = greedy15
timeout = 86400
atavistic = False
selection = default

runner.prefix = lash-

trains.data = problems.ok
trains.runner = grackle.runner.lash.LashRunner
trains.runner.timeout = 1
trains.runner.penalty = 10000000
trains.runner.cores = 50

trainer = grackle.trainer.lash.paramils.LashParamilsTrainer
trainer.runner = grackle.runner.lash.LashRunner
trainer.runner.timeout = 1
trainer.runner.penalty = 10000000
trainer.timeout = 300
trainer.restarts = True
trainer.log = True
```

### Examples

Example run scripts can be found in the directory `examples` in this repository for `vampire` and `lash` ATP provers.
At first, extract the benchmark problems in the file `benchmarks.tar.gz`.
Then the script `run-grackle.sh` shows how to run Grackle.

## Credits

Development of this software prototype was supported by: 

+ ERC-CZ grant no. LL1902 *POSTMAN*
+ ERC Consolidator grant no. 649043 *AI4REASON*
+ ERC Starting grant no. 714034 *SMART*
+ FWF grant P26201
+ Cost Action CA15123 *EUTypes*

