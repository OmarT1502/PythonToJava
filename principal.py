from antlr4 import *
from javaTraductorLexer import javaTraductorLexer
from javaTraductorParser import javaTraductorParser
from javaTraductorListener import javaTraductorListener
from InPythonToJava import InPythonToJava

def main():
    in_code = input ("Give me the file's name >")
    # Leer archivo de entrada
    file = open (in_code)
    lexer = javaTraductorLexer(InputStream(file.read()))
    t_stream = CommonTokenStream(lexer)

    parser = javaTraductorParser(t_stream)
    tree = parser.program()

    # print(tree.toStringTree(recog=parser))
    walker = ParseTreeWalker()
    walker.walk(InPythonToJava(), tree)

if __name__ == '__main__':
    main()