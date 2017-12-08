"""
Generate structure factor list.
"""

from cctbx import miller
from cctbx import crystal
import numpy as np
import sys


space_group = sys.argv[1]
a = float(sys.argv[2])
b = float(sys.argv[3])
c = float(sys.argv[4])
alpha = float(sys.argv[5])
beta = float(sys.argv[6])
gamma = float(sys.argv[7])
low_res = float(sys.argv[8])
high_res = float(sys.argv[9])
ms = miller.build_set(
    crystal_symmetry=crystal.symmetry(
        space_group_symbol=space_group,
        unit_cell=(a,b,c,alpha,beta,gamma)),
    anomalous_flag=True,
    d_min=high_res,
    d_max=low_res,
    )
ms_comp = ms.expand_to_p1()

np.savetxt('sf.hkl', ms_comp.indices(), fmt='%d')
