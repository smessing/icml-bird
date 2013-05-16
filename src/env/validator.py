"""
  validator.py - checks the environment for all the dependent environment
                 variables.

  To register a new environment variable, do the following:

   - Define all the requisite variables as a list of strings and define it as
     the attribute PATH_VARS on the given module.
   - Add the module to the list MODULES in this file. 
"""
import analysis.svm
from input import loader
import output.svm
import os

MODULES = [ analysis.svm, loader, outpt.svm ]

def check_environs(raise_exceptions=True):
  """
    Check the required environment variables for the codebase.

    If any required path variables are not found, an exception is raised. The
    exception includes a message parameter, as well as the specific path
    variable that was missing.
  """
  print 'checking environs...'
  for module in MODULES:
    for path_var in module.PATH_VARS:
      if not os.environ.has_key(path_var):
        print 'ERR: Env variable %s must be defined (required by %s).' % \
            (path_var, module.__name__)
        if raise_exceptions:
          raise Exception('Path variable not found.', path_var)
  print '...done'

