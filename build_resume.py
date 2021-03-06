#!/usr/bin/env python

#
# see readme for more instructions.
#

import sys
import imp
import os.path

import jinja2


def main():
    """render templates using sourcefile.

    takes the arg passed at the command line and saves output
    there.  uses export type to determine the template name
    and what filename to give the output.
    """

    # parse argument filepath
    SOURCE_FILE = sys.argv[1]
    name, ext = os.path.splitext(SOURCE_FILE)
    SAVE_AS = os.path.basename(name)

    # import the argument as a python module
    resume_module = imp.load_source('resume', SOURCE_FILE)

    # render templates
    template_types = ['html','tex','txt']

    for ttype in template_types:
        # open the template file, make it an object
        template_string = open('templates/%s_template.%s' % (ttype, ttype), 'r').read()
        template = jinja2.Template(template_string)

        # write the rendered template to file
        output = open('output/%s.%s' % (SAVE_AS, ttype), 'w')
        output.write(template.render(resume_module.RESUME, mode=ttype))
        output.close()

if __name__ == '__main__':
    main()
