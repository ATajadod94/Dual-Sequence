import collections
import os
from random import seed
from gui import getparticipant, window, homestim, mousestim, arrowstim, cursorstim, textstim
from studylogic import initblocks, runblock
from myexp import initexp


cfg = collections.defaultdict(list)
cfg = initexp(cfg)
cfg = getparticipant(cfg)
cfg = window(cfg)
cfg = homestim(cfg)
cfg = mousestim(cfg)
cfg = cursorstim(cfg)
cfg = textstim(cfg)
cfg = arrowstim(cfg, [0,0])
seed(int(cfg['P_number']) + sum([ord(x) for x in 'garage experiment']))

if not os.path.isdir('Data'):
    os.makedirs('Data')


all_blocks = initblocks(cfg)

for block in all_blocks:
    runblock(block, cfg)

cfg['win'].close()            