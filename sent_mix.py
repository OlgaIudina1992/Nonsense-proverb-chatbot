from corpus_animal import *
from corpus_misc import *
from corpus_ros import *
import itertools
import random


global_nouns = list(itertools.chain(anim_nouns, misc_nouns, ros_nouns))
global_verbs = list(itertools.chain(anim_verbs, misc_verbs, ros_verbs))
global_adjs = list(itertools.chain(anim_adjs, misc_adjs, ros_adjs))
global_advs = list(itertools.chain(anim_advs, misc_advs, ros_advs))
global_vbns = list(itertools.chain(misc_vbn, ros_vbn))
global_gers = list(itertools.chain(misc_vbg, ros_vbg, anim_vbg))

S = random.choice(global_nouns[0:4090])
O = random.choice(global_nouns[4091:])
V = random.choice(global_verbs)
A = random.choice(global_adjs)
Av = random.choice(global_advs)
V_ing = random.choice(global_gers)
V_ed = random.choice(global_vbns)
