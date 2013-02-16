Ragel random output generator
=============================

This tool allows you to generate random output from a `ragel <http://www.complang.org/ragel/>`_ FSM.

A useful example is fuzz testing. Assume you have a HTTP header parser
implemented in ragel. By definition the parser will be able to parse
the output of this tool. By flipping a few bits in the output you can
feed your parser almost-correct data and see how it behaves.

It's also useful to get a feel for possible inputs of your grammar. I
managed to spot a few bugs just by looking at the output from this
tool and realising that the grammar was too permissive.

Usage
=====

First you need to generate the XML version of your FSM. E.g.:

::
    ragel -x smtp.ragel > smtp.xml

Now you can run this tool:

::
    python rg.py smtp.xml

Here's some example output for a SMTP parser I wrote a while back:

::

    'HELO [05.73]\n'
    'DATA\n'
    'EHLO 5.7eKI\r\n'
    'QUIT\r\n'
    'DATA\r\n'
    'EHLO K\n'
    'EHLO s\n'
    'RCPT To:<+\\4"vT.4.\\"Id8".\\7.\\D8"+6"d\\J"\\A5+"F>\n'
    'QUIT\n'
    'DATA\n'
    'EHLO [4.1]\n'
    'DATA\r\n'
    'RCPT tO:<..7>\r\n'
    'QUIT\r\n'
    'EHLO [58.0xfa.9]\r\n'

Licence
=======

This code is public domain.


