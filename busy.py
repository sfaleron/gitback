from time import sleep
import sys

bg = '----'
fg = '*'
delay = .4

N = len(bg)
n = len(fg)

i = 0

while True:
   print bg[:i]+fg+bg[i+n:]+bg[i+n:]+fg+bg[:i]+'\r',

   if i == N-n:
      inc = -1

   if i == 0:
      inc = 1

   i += inc

   sys.stdout.flush()
   sleep(delay)
