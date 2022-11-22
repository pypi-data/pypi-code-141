#!/bin/python3
# The MIT License (MIT)
# Copyright © 2021 Yuma Rao

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
""" Benchmarking pytest fixture.

Example:
    $ python3  benchmarks/template_miner.py --nucleus.nhid 600

"""
import subprocess
from benchmarks import QueryBenchmark
import bittensor

class Benchmark ( QueryBenchmark ):
    r""" Benchmark pytest class.
    """

    @staticmethod
    def miner_name() -> str:
        r""" Return miner name
        """
        return 'template_miner'

    @staticmethod
    def run_neuron( config ):
        r""" To be implemented in the subclass, runs the neuron.
            Args:
                config (bittensor.Config)
                    Run config
        """
        bittensor.neurons.text.template_miner.neuron(config).run()

    @staticmethod
    def config() -> 'bittensor.Config':
        r""" Return config
            Returns:
                config (bittensor.Config)
                    Run config.
        """
        return bittensor.neurons.text.template_miner.neuron.config()

    def benchmark_custom( self ):
        r""" Custom benchmark
        """
        history = self.query_sequence( ncalls = 100, batch_size = 15, block_size = 10 )
        self.print_query_analysis( history )
        history.to_csv( self.log_dir + '/custom-queries.csv' )


if __name__ == '__main__':
    benchmark = Benchmark()
    benchmark.run()

