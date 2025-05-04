#!/usr/bin/env python3

import code
import os
import readline


REPL_HISTORY_FILE = os.path.expanduser(".repl_history")
REPL_HISTORY_SIZE = 1024

if readline and os.path.exists(REPL_HISTORY_FILE):
  readline.read_history_file(REPL_HISTORY_FILE)

class Repl(code.InteractiveConsole):
  def runsource(self, source, filename='<input>', symbol='single'):
    if not source.endswith(';'):
      return True
    print('source:', source)

repl = Repl()
repl.interact(banner='', exitmsg='')

if readline:
  readline.set_history_length(REPL_HISTORY_SIZE)
  readline.write_history_file(REPL_HISTORY_FILE)
