# (C) Copyright IBM Corp. 2019, 2020, 2021, 2022.

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#           http://www.apache.org/licenses/LICENSE-2.0

#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from typing import List
import dask.array as da
import h5py
import numpy as np

class CompressedPinv:

    def __init__(self, D:h5py.Dataset=None, chunks:tuple=None, k:int=100) -> None:

        self.D = da.from_array(D, chunks=chunks)
        self.k = k
        self.u, self.s, self.v_star = da.linalg.svd_compressed(self.D, k=k)

        self.s_pinv = 1/self.s.compute()
        self.u_star = self.u.conj().T
        self.v = self.v_star.conj().T

        self.v_bar = self.v*self.s_pinv

        self.n_rows = self.u_star.shape[0]

    def __call__(self, Y:h5py.Dataset=None, batches:List[slice]=None) -> None:

        output = np.zeros((self.n_rows, Y.shape[-1]))

        for batch in batches:

            output += self.u_star[:, batch].compute() @ Y[batch]

        return self.v_bar.compute() @ output




