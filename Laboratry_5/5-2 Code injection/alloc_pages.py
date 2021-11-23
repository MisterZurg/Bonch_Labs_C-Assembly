#!/ usr/bin/ python

from argparse import ArgumentParser
from py_ptrace import alloc_pages

arg_parser = ArgumentParser()
arg_parser.('-p', '--pid ', type=int, required = True, help ='set process id')
arg_parser.add_argument('-n', '--npages', type=int, required = True, help='allocate n rwx pages')
arg_parser.add_argument('-d', '--data', type =str, required = False, help='insert data')

args = arg_parser . parse_args ()
pid = args.pid
npages = args. npages
data = args.data
addr = alloc_pages(pid, npages, data)
print("rwx page has address" + str(hex(addr)))