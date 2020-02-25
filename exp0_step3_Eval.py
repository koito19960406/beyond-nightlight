from argparse import Namespace

from maskrcnn.train import run


args = Namespace()
args.comment = 'tmp'
args.config = ['main', 'mexico']
args.mode = ['val']
args.resume_run = 'run_15_Pool'
args.no_cuda = False
args.cuda_max_devices = 1

run(args)