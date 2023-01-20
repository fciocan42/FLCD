#!/bin/bash

clear; lex FCLang.lxi && yacc -d FCLang.y && gcc -o lang.out y.tab.c lex.yy.c && ./lang.out < "$@"
