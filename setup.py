import cx_Freeze
import sys
sys.setrecursionlimit(10000000)
buildOptions = dict(include_files = ['Assets/'])
executables = [cx_Freeze.Executable("main.py")]
# {"build_exe": {"packages": ["pygame"], 
# 						"include_files": [""]}}
cx_Freeze.setup(
	name = "Hamiltonian Path",
	version = "1.0",
	options= dict(build_exe = buildOptions),
	executables = executables
)