#!/usr/bin/env python

import os, re, sys
import unittest
sys.path.append('..')
import ecs

TEST_PATH = os.path.join( os.path.dirname(__file__), '.')

def get_test_modules():
    modules = []
    for f in os.listdir(TEST_PATH):
        if f.startswith('__init__') or f.startswith('.'):
            continue
        modules.append(os.path.splitext(f)[0])
    return modules

def run_tests(modules, verbosity=1):
    all_modules = get_test_modules()
    if len(modules) == 0:
        # using ALL modules
        modules = all_modules

    suite = unittest.TestSuite()
    for module in [ x for x in modules if x in all_modules ]:
        if verbosity > 0 :
            print "Import module %s ..." % module
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(module))

    results = unittest.TextTestRunner(verbosity=verbosity).run(suite)
    return len(results.failures)

if __name__ == "__main__":
    from optparse import OptionParser
    usage = "%prog [options] [model model ...]"
    parser = OptionParser(usage= usage)
    parser.add_option('-v', '--verbosity', action='store', dest='verbosity', default='0',
        type='choice', choices=['0', '1', '2'],
        help='Verbosity level; 0=minimal output, 1=normal output, 2=all output')
    options, args = parser.parse_args()
    failures = run_tests(args, int(options.verbosity))
    if failures:
        sys.exit(failures)
