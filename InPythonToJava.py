from javaTraductorParser import *
from javaTraductorListener import javaTraductorListener

class InPythonToJava(javaTraductorListener):
    def __init__(self):
        self.java_code = "public class MiClase {\n"
        self.parameters = []
        self.function_name = ""
        self.function_call_values = []
        self.operator = "+"  # Valor predeterminado; cambiará dinámicamente

    # Enter a parse tree produced by javaTraductorParser#program.
    def enterProgram(self, ctx: javaTraductorParser.ProgramContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#program.
    def exitProgram(self, ctx: javaTraductorParser.ProgramContext):
        self.printMain()
        self.java_code += "}"
        self.createJavaFile()

    # Enter a parse tree produced by javaTraductorParser#function.
    def enterFunction(self, ctx: javaTraductorParser.FunctionContext):
        self.function_name = ctx.getChild(1).getText()
        self.java_code += f"    public int {self.function_name}"

    # Enter a parse tree produced by javaTraductorParser#parameters.
    def enterParameters(self, ctx: javaTraductorParser.ParametersContext):
        self.parameters = []  # Limpia los parámetros

    # Exit a parse tree produced by javaTraductorParser#parameters.
    def exitParameters(self, ctx: javaTraductorParser.ParametersContext):
        parameterList = []
        
        for parameter in range(ctx.getChildCount()):
            child = ctx.getChild(parameter)
            if isinstance(child, TerminalNode) and child.getSymbol().type == javaTraductorParser.ID:
                param_name = child.getText()
                parameterList.append(f'int {param_name}')
                self.parameters.append(param_name)
                

        self.java_code += f"({', '.join(parameterList)}) {{\n"

    # Función para capturar la llamada a la función y los valores de los parámetros
    def enterFunctionCall(self, ctx: javaTraductorParser.FunctionCallContext):
        
        self.function_call_values = []  # Limpia los valores previos

        # Captura los valores de los argumentos pasados a la función
        args = ctx.getText()[ctx.getText().find("(")+1:ctx.getText().find(")")]  # Extrae solo lo que está entre los paréntesis
        if args:
            self.function_call_values = [arg.strip() for arg in args.split(',') if arg.strip()]  # Limpia comas adicionales y espacios

    # Enter a parse tree produced by javaTraductorParser#operator.
    def enterOperator(self, ctx: javaTraductorParser.OperatorContext):
        self.operator = ctx.getText()  # Extrae el operador del contexto

    # Exit a parse tree produced by javaTraductorParser#block.
    def exitBlock(self, ctx: javaTraductorParser.BlockContext):
        return_expression = f" {self.operator} ".join(self.parameters)
        self.java_code += f"        return {return_expression};\n"
        self.java_code += "    }\n"

    # Imprime el método main
    def printMain(self):
        self.java_code += "    public static void main(String[] args) {\n"
        self.java_code += "        MiClase miObjeto = new MiClase();\n"

        # Si no se capturan valores en la llamada a la función, se asignan valores por defecto
        if not self.function_call_values:
            self.function_call_values = ['0'] * len(self.parameters)

        example_args = ', '.join(self.function_call_values)
        self.java_code += f"        int resultado = miObjeto.{self.function_name}({example_args});\n"
        self.java_code += '        System.out.println(resultado);\n'
        self.java_code += "    }\n"

    # Crea el archivo Java con el código generado
    def createJavaFile(self):
        filename = "MiClase.java"
        try:
            with open(filename, 'w') as java_file:
                java_file.write(self.java_code)
            print(f"Archivo {filename} creado exitosamente.")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
