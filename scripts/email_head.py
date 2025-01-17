#!/usr/bin/env python3

import sys

class Lexer:
    def __init__(self, input_str: str) -> None:
        self.input = input_str
        self.start = 0
        self.current = 0
        self.col = 1
        self.line = 1

    def advance(self) -> str:
        self.current += 1
        c = self.input[self.current - 1]
        if c == '\n':
            self.line += 1
            self.col = 1
        self.col = self.col + 1
        return c

    def is_at_end(self) -> bool:
        return self.current >= len(self.input)

    def peek(self) -> str:
        if self.is_at_end():
            return '\0'
        return self.input[self.current]

    def scan_header(self) -> 'Header | None':
        self.start = self.current

        c = self.advance()
        if c == '\r':
            if self.peek() == '\n':
                return None # Assume we've reached end of headers
            else:
                raise Exception("Unexpected character after CR")

        while self.peek() != ':' and not self.is_at_end():
            c = self.advance()
            if c == '\r' or c == '\n':
                raise Exception("Unexpected newline in header name")

        if self.is_at_end():
            raise Exception("Unexpected end of input in header name")

        name = self.input[self.start:self.current]

        c = self.advance()
        if c != ':':
            raise Exception("Expected ':' after header name")

        self.start = self.current
        header_text = []

        while True:
            # read rest of body
            while self.peek() != '\r' and not self.is_at_end():
                self.advance()

            if self.is_at_end():
                raise Exception("Unexpected end of input in header value")
            self.advance() # Consume '\r'

            # Check for folding
            if self.peek() != '\n':
                raise Exception(f"{self.line}:{self.col} Expected newline after header value, received '{self.peek()}'")
            self.advance()

            header_val = self.input[self.start:self.current - 2]
            self.start = self.current
            # header_val_replaced = header_val.replace('\n', '\\n').replace('\r', '\\r')
            #  if '\r' in header_val:
                #  print(f"Warning: CR found in header value: {header_val}")
            header_text.append(header_val)

            if self.peek() != ' ' and self.peek() != '\t':
                # Header folding
                break

        value = ''.join(header_text)
        return Header(name, value)


class Token:
    def __init__(self, type: str, lexeme: str, line: int, col: int) -> None:
        self.type = type
        self.lexeme = lexeme
        self.line = line
        self.col = col

class Header:
    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = value

file = sys.stdin.read()

lexer = Lexer(file)

while True:
    header = lexer.scan_header()
    # print(header)
    if header is None:
        break
    print("\t".join([header.name, header.value]), end = "\n")
