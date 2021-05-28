# Brainfuck-Interpreter
A Python Brainfuck Interpreter Class

## Exaple
```python
from brain.py import BrainfuckInterpreter

brain = BrainfuckInterpreter()
brain.read_program_from_string("--<-<<+[+[<+>--->->->-<<<]>]<<--.<++++++.<<-..<<.<+.>>.>>.<<<.+++.>>.>>-.<<<+.")

brain.run_program()
```
```
Hello, World!
```
<br><br>

```python
from brain.py import BrainfuckInterpreter

brain = BrainfuckInterpreter()
brain.read_program_from_file('program.txt')

brain.run_program()
```
```
Hello World! 255
```


## Usage
### BrainfuckInterpreter Class
#### Values
| Value Name | Pass Value Name | Default Value| Explanation |
| ------------- | ------------- | ------------- | ------------- |
| program | N/A | NULL | This stores the program that is executed when calling run_program() |
| cellSize | cell_size | 255 | This defines how high of a value a cell can store (These Values Are allways unsigned) |
| memorySize | memory_size | 3000 | This defines how many memory cells the interpreter can use |

#### Functions
| Class Function Name | Explanation |
| ------------- | ------------- |
|  validate_program() | This removes all invalid characters from the loaded program |
|  read_program_from_string(String program_string)  | This function reads in a string then validates and stores it as the program |
|  read_program_from_file(String file_path) | This function takes in a file path in the form of a string then reads the file validates it and stores it as the program  |
|  run_program() | This Executes what is stored in the program Variable |
