# Generated from ./javaTraductor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .javaTraductorParser import javaTraductorParser
else:
    from javaTraductorParser import javaTraductorParser

# This class defines a complete listener for a parse tree produced by javaTraductorParser.
class javaTraductorListener(ParseTreeListener):

    # Enter a parse tree produced by javaTraductorParser#program.
    def enterProgram(self, ctx:javaTraductorParser.ProgramContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#program.
    def exitProgram(self, ctx:javaTraductorParser.ProgramContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#statement.
    def enterStatement(self, ctx:javaTraductorParser.StatementContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#statement.
    def exitStatement(self, ctx:javaTraductorParser.StatementContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#function.
    def enterFunction(self, ctx:javaTraductorParser.FunctionContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#function.
    def exitFunction(self, ctx:javaTraductorParser.FunctionContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#parameters.
    def enterParameters(self, ctx:javaTraductorParser.ParametersContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#parameters.
    def exitParameters(self, ctx:javaTraductorParser.ParametersContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#block.
    def enterBlock(self, ctx:javaTraductorParser.BlockContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#block.
    def exitBlock(self, ctx:javaTraductorParser.BlockContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#returnStatement.
    def enterReturnStatement(self, ctx:javaTraductorParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#returnStatement.
    def exitReturnStatement(self, ctx:javaTraductorParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#printStatement.
    def enterPrintStatement(self, ctx:javaTraductorParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#printStatement.
    def exitPrintStatement(self, ctx:javaTraductorParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#Parenthesis.
    def enterParenthesis(self, ctx:javaTraductorParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#Parenthesis.
    def exitParenthesis(self, ctx:javaTraductorParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#Variable.
    def enterVariable(self, ctx:javaTraductorParser.VariableContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#Variable.
    def exitVariable(self, ctx:javaTraductorParser.VariableContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:javaTraductorParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:javaTraductorParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#Number.
    def enterNumber(self, ctx:javaTraductorParser.NumberContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#Number.
    def exitNumber(self, ctx:javaTraductorParser.NumberContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#BinaryOperation.
    def enterBinaryOperation(self, ctx:javaTraductorParser.BinaryOperationContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#BinaryOperation.
    def exitBinaryOperation(self, ctx:javaTraductorParser.BinaryOperationContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#functionCall.
    def enterFunctionCall(self, ctx:javaTraductorParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#functionCall.
    def exitFunctionCall(self, ctx:javaTraductorParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by javaTraductorParser#operator.
    def enterOperator(self, ctx:javaTraductorParser.OperatorContext):
        pass

    # Exit a parse tree produced by javaTraductorParser#operator.
    def exitOperator(self, ctx:javaTraductorParser.OperatorContext):
        pass



del javaTraductorParser