# Brainfuck-Interpreter
A Python Brainfuck Interpreter Class

## Exaple
```python
from brain.py import BrainfuckInterpreter

brain = BrainfuckInterpreter()
brain.read_program_from_string("--<-<<+[+[<+>--->->->-<<<]>]<<--.<++++++.<<-..<<.<+.>>.>>.<<<.+++.>>.>>-.<<<+.")

brain.run_program()
```
