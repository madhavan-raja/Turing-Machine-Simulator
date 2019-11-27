import state

q0 = state.state()
q0.name = 'Q0'

q_accept = state.state()
q_accept.name = 'Accept'
q_accept.halt = True

q0.transition['0'] = ['1', True, q0]
q0.transition['1'] = ['0', True, q0]
q0.transition[None] = [None, False, q_accept]

tape_string = '101101'
tape = [x for x in tape_string]
tape.extend([None for _ in range(10)])
head = 0

def output_tape(blanks=True):
    global tape

    for symbol in tape:
        if symbol == None and blanks == False:
            continue
        if symbol == None:
            final_symbol = 'B'
        else:
            final_symbol = symbol
        print(final_symbol, end='')
    print()


def output_head():
    global head

    for _ in range(head):
        print(' ', end='')
    print('^')


def main():
    global tape, head

    current_state = q0

    for s in range(10):
        print(f'At step {s} in state {current_state.name}')
        output_tape()
        output_head()

        if current_state.halt or current_state == None:
            break

        print(f'Encounterd {tape[head]} at position {head}')

        current_state_transition = current_state.transition.get(tape[head])
        if current_state_transition == None:
            break

        print(f'Replacing it with {current_state_transition[0]}')
        print(f'Moving {"Right" if current_state_transition[1] else "Left"}')

        tape[head] = current_state_transition[0]
        if (current_state_transition[1]):
            head += 1
        else:
            head -= 1
        current_state = current_state_transition[2]
        print()

    print(f'Halted at {current_state.name} with final tape:')
    output_tape(False)


if __name__ == '__main__':
    main()
