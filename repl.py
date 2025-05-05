#!/usr/bin/env python3

import code
import os
import readline
import sys

REPL_HISTORY_FILE = os.path.expanduser(".repl_history")
REPL_HISTORY_SIZE = 1024

if readline and os.path.exists(REPL_HISTORY_FILE):
  readline.read_history_file(REPL_HISTORY_FILE)

class Repl(code.InteractiveConsole):
  def runsource(self, source, filename='<input>', symbol='single'):
    if not source.endswith('\n'):
      return True
    # print('source:', source)
    eval(source)

if readline:
  readline.set_history_length(REPL_HISTORY_SIZE)
  readline.write_history_file(REPL_HISTORY_FILE)

sys.ps1 = '[ '
sys.ps2 = '  '
repl = Repl()
repl.interact(banner='', exitmsg='')
