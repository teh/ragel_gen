import argparse
import collections
import random
from lxml import etree

T = collections.namedtuple('T', 'start end newstate')

def get_state_machine(path):
    states = {}
    final_set = set()

    tree = etree.parse(path)
    entry = tree.find('/ragel_def/machine/entry_points/entry[1]')
    entry_state = int(entry.text)

    for state in tree.findall('/ragel_def/machine/state_list/state'):
        id = int(state.get('id'))
        final = state.get('final', 'f') == 't'
        if final:
            final_set.add(id)
            
        l = []
        for t in state.findall('./trans_list/t'):
            start, end, newstate, _ = t.text.split()
            l.append(T(int(start), int(end), int(newstate)))
        states[id] = l
    return entry_state, states, final_set

def run_random(e, sm, final_set):
    s = sm[e]
    while True:
        t = random.choice(s)
        
        c = random.choice(range(t.start, t.end + 1))
        if c < 0:
            yield c + 128
        else:
            yield c

        if t.newstate in final_set:
            break
        s = sm[t.newstate]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()

    e, sm, f = get_state_machine(args.path)

    while True:
        word = ''.join(chr(x) for x in run_random(e, sm, f))
        print repr(word)

if __name__ == '__main__':
    main()
