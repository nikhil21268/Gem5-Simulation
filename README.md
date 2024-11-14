# Computer Architecture Cache Simulation

The goal here is to analyze the impact of cache configurations on miss rates in a simulated computer system using gem5. This project simulates two different CPU models—RiscvTimingSimpleCPU() and RiscvO3CPU()—with varying L2 cache configurations.

## Description

The simulation leverages the "qsort_small" benchmark from the MiBench benchmark suite to observe how cache size and associativity influence cache miss rates across two CPU models. We analyze these effects under various cache configurations, particularly focusing on the L2 cache.

## Dependencies

- Python 3.x
- [gem5](http://www.gem5.org/)
- RISC-V GNU Toolchain

## Installation

## RISC-V Toolchain Setup

sudo apt-get update
sudo apt-get install autoconf automake autotools-dev curl python3 libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev ninja-build git cmake libglib2.0-dev libslirp-dev
git clone https://github.com/riscv/riscv-gnu-toolchain
cd riscv-gnu-toolchain
./configure --prefix=/opt/riscv
make
export PATH=/opt/riscv/bin:$PATH

## Gem5 Installation

## Assuming dependencies are installed and PATH is set
git clone https://gem5.googlesource.com/public/gem5
cd gem5
scons build/RISCV/gem5.opt -j$(nproc)

## Running Simulations

To run a simulation, use the following command:

./build/RISCV/gem5.opt configs/tutorial/two_level.py

## Plots

![1](https://github.com/nikhil21268/Gem5-Simulation/blob/main/Plots/Plot1.png)

![2](https://github.com/nikhil21268/Gem5-Simulation/blob/main/Plots/Plot2.png)

## Tables

![1](https://github.com/nikhil21268/Gem5-Simulation/blob/main/Plots/Table1.png)

![2](https://github.com/nikhil21268/Gem5-Simulation/blob/main/Plots/Table2.png)


## Contributing

Contributions to improve the simulations or extend the configurations are welcome. Please submit a pull request or open an issue to discuss your ideas.
