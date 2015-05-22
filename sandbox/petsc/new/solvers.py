#!/usr/bin/env python

#KSP: fgmres, lgmres, gmres, bcgs, bicg, tfqmr, tcqmr, lsqr
#ymmetric only: chebychev, cg
#arallel only: ibcgs

#PC: sor, jacobi, bjacobi, asm(k) [k=0..3], 
#sequential only: ilu(k) [k=0..3], 
#symmetric only: icc(k) instead of ilu
#any matrix with (some) 0 diagonal entries:
#-pc_fieldsplit_type schur in conjunction with -pc_fieldsplit_detect_saddle_point (Boyana will look into that)

solvers = ['gmres','fgmres','lgmres','bicg','bcgs','tmfqmr','tcqmr','lsqr','chebychev','cg', 'ibcgs']
pcs = { 'ilu': {'factor_levels':[0,1,2,3]},
	'asm': {'asm_overlap' : [0,1,2,3]},
     	'jacobi' : {},
	'bjacobi' : {},
	'icc' : {'factor_levels':[0,1,2,3]}
    }

commands = {}
	
for solver in solvers:
  for pc, pcopts in pcs.items():
    for pc_optname, pc_optvals in pcopts.items():
      for pc_optval in pc_optvals:
        optstr = ' -ksp_type %s -pc_type %s -pc_%s %s ' % (solver, pc, pc_optname, str(pc_optval))
        hashstr = str(abs(hash(optstr.strip())) % (10 ** 8))
        commands[hashstr] = optstr

print commands
