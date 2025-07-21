import argparse
from calculator import calculator
parser= argparse.ArgumentParser(description="Adding Description")
parser.add_argument("-o","--Output",type=str,nargs='+', help="show the output")
arg =parser.parse_args()
print(arg.Output)
parser.set_defaults(func=calculator(arg.Output))
arg1 = parser.parse_args()
if arg1.func:
    print(f"The Output is:", arg1.func)