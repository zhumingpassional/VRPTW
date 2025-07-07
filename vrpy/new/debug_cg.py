# tests/debug_cg.py

import functools
import vrpy.vrp as vrp_module
cd C:\Users\casia\projects\vrpy_clone

# 如果已经有 upstream，先换 URL
git remote set-url upstream https://github.com/zhumingpassional/vrpy.git

# 或者如果还没设
# git remote add upstream https://github.com/zhumingpassional/vrpy.git

# 再 fetch
git fetch upstream

called = False

_original_find_columns = vrp_module.VehicleRoutingProblem._find_columns

def _trace_find_columns(self, *args, **kwargs):
    global called
    called = True
    print(">>> [DEBUG] _find_columns was called！")
    return _original_find_columns(self, *args, **kwargs)

vrp_module.VehicleRoutingProblem._find_columns = _trace_find_columns
