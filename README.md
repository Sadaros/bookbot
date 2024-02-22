# bookbot
Boot.dev bookbot project

If the program is called with no arguments you will have to provide the relative path to the document, and it will only output the report to the terminal

If the program is called with a single argument, it will take it as the input document, and output the report to the terminal

If the program is called with 2 arguments, the first argument will be the input file. And the second argument will be the output file. The report will then not print to terminal.

## ToDo:

- Allow you to chose what metrics to analyze
- Error handling
    - check whether file exists before opening
    - check if file exists before writing report to file, so as to avoid overwriting something
- Refactor code and pull single use functions into main()
- Add introduction to README
- Add examples to README
- Use argparse module

- ~Allow you to specify input file with command line argument~ done 17.02.24
- ~Allow you to save the report to file~ done 17.02.24