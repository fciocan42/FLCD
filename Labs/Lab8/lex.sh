#!/bin/bash

clear; flex FCLang.lxi && gcc lex.yy.c -o lang.out && ./lang.out < "$@"
