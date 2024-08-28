import m5
from m5.objects import *
from m5.util import addToPath

# addToPath('../../')

from common import CacheConfig
from common.Caches import *
from common import Platforms

def setup_system(cpu_type):
    # Setup based on the specified CPU type
    system = System()

    system.clk_domain = SrcClockDomain()
    system.clk_domain.clock = '1GHz'
    system.clk_domain.voltage_domain = VoltageDomain()

    system.mem_mode = 'timing'  # Although we use timing, it's within the context of SE mode
    system.mem_ranges = [AddrRange('512MB')]

    # Choose the CPU model based on the parameter passed
    if cpu_type == "simple":
        system.cpu = RiscvTimingSimpleCPU()
    elif cpu_type == "o3":
        system.cpu = RiscvO3CPU()

    # Cache setup
    system.cpu.icache = L1ICache(size='16kB', assoc=2)
    system.cpu.icache.response_latency = 2
    system.cpu.icache.cpu_side = system.cpu.icache_port

    system.cpu.dcache = L1DCache(size='16kB', assoc=2)
    system.cpu.dcache.response_latency = 2
    system.cpu.dcache.cpu_side = system.cpu.dcache_port

    system.l2bus = L2XBar()
    system.cpu.icache.mem_side = system.l2bus.slave
    system.cpu.dcache.mem_side = system.l2bus.slave

    system.l2cache = L2Cache(size='256kB', assoc=4)
    system.l2cache.response_latency = 10
    system.l2cache.cpu_side = system.l2bus.master

    system.membus = SystemXBar()
    system.l2cache.mem_side = system.membus.slave
    system.system_port = system.membus.slave

    # SE mode specific setup
    process = Process()
    process.cmd = ['mibench/automotive/qsort/qsort_small.elf']
    system.cpu.workload = process
    system.cpu.createThreads()

    return system

def simulate_system(cpu_type):
    system = setup_system(cpu_type)
    root = Root(full_system=False, system=system)
    m5.instantiate()

    print(f"Beginning simulation with {cpu_type} CPU in SE mode!")
    exit_event = m5.simulate()
    print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))

    # Dump the statistics to a file
    stats_file = f"stats_{cpu_type}.txt"
    m5.stats.dump()
    m5.stats.reset()  # Reset statistics for the next run (if any)
    with open(stats_file, 'w') as f:
        f.write(m5.stats.text())
    print(f"Statistics saved to {stats_file}")


if __name__ == "__main__":
    simulate_system("simple")  # Run with simple CPU
    # simulate_system("o3")      # Run with O3 CPU