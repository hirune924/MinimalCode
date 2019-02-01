#!/usr/bin/env python
# -*- coding: utf-8 -*-
from absl import flags, app

# str, int, float, bool
# exe command: `--s_key string`
# exe command: `--i_key 10`
# exe command: `--f_key 0.01`
# exe command: `--b_key` or `--nob_key`
# exe command: `--b_key=True` or `--b_key=False`
flags.DEFINE_string('s_key', 'default string', 'help message for this argument.', short_name='s')
flags.DEFINE_integer('i_key', None, 'help message for this argument.', short_name='i')
flags.DEFINE_float('f_key', None, 'help message for this argument.', short_name='f')
flags.DEFINE_bool('b_key', True, 'help message for this argument.', short_name='b')

# list
# exe command: `--list_key x,y`
flags.DEFINE_list('list_key', None, 'help message for this argument.', short_name='l')

# enum
# error occurs if you specify something other than x, y, z
# exe command: `--enum_key z`
flags.DEFINE_enum('enum_key', 'x', ['x', 'y', 'z'], 'help message for this argument.', short_name='e')

# alias
# s_key is an alias for alias_key
# exe command: `--alias_key string`
flags.DEFINE_alias('alias_key', 's_key')

FLAGS = flags.FLAGS


def main(argv=None):
    print('s_key: {}'.format(FLAGS.s_key))
    print('i_key: {}'.format(FLAGS.i_key))
    print('f_key: {}'.format(FLAGS.f_key))
    print('b_key: {}'.format(FLAGS.b_key))

    print('list_key: {}'.format(FLAGS.list_key))

    print('enum_key: {}'.format(FLAGS.enum_key))

    print('alias_key: {}'.format(FLAGS.alias_key))

    #print('all args: {}'.format(FLAGS.flag_values_dict()))

    return


if __name__ == '__main__':
    flags.mark_flags_as_required(['i_key', 'f_key'])
    app.run(main)
