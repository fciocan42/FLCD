%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define YYDEBUG 1

void yyerror(const char* msg) {
  fprintf(stderr, "%s\n", msg);
}
int yylex();

#define TIP_INT 1
#define TIP_REAL 2
#define TIP_CAR 3

double stiva[20];
int sp;

void push(double x)
{ stiva[sp++]=x; }

double pop()
{ return stiva[--sp]; }

%}

%union {
  	int l_val;
	char *p_val;
}

%token START

%token FUN
%token DEFINE
%token CASE
%token OF
%token END
%token WHEN
%token READ
%token WRITE

%token ID
%token <p_val> CONST_INT
%token <p_val> CONST_REAL
%token <p_val> CONST_CAR
%token CONST_SIR

%token MATCH
%token EQ
%token LE
%token GE

%left '+' '-'
%left DIV MOD '*' '/'
%left OR
%left AND

%type <l_val> expr_stat factor_stat constanta

%%

prog_sursa:	START ';' bloc
		;
bloc:		sect_const instr_comp
		;
sect_const:	/* empty */
		| lista_const
		;
lista_const:	decl_const
		| lista_const decl_const
		;
decl_const:	ID '=' {sp=0;} expr_stat ';'	{
		printf("*** %d %g ***\n", $4, pop());
					}
		;
expr_stat:	factor_stat
		| expr_stat '+' expr_stat	{
			if($1==TIP_REAL || $3==TIP_REAL) $$=TIP_REAL;
			else if($1==TIP_CAR) $$=TIP_CAR;
				else $$=TIP_INT;
			push(pop()+pop());
						}
		| expr_stat '-' expr_stat	{
			if($1==TIP_REAL || $3==TIP_REAL) $$=TIP_REAL;
			else if($1==TIP_CAR) $$=TIP_CAR;
				else $$=TIP_INT;
			push(-pop()+pop());
						}
		| expr_stat '*' expr_stat	{
			if($1==TIP_REAL || $3==TIP_REAL) $$=TIP_REAL;
			else if($1==TIP_CAR) $$=TIP_CAR;
				else $$=TIP_INT;
			push(pop()*pop());
						}
		| expr_stat '/' expr_stat	
		| expr_stat DIV expr_stat
		| expr_stat MOD expr_stat
		;
factor_stat:	ID		{}
		| constanta
		| '(' expr_stat ')'	{$$ = $2;}
		;
constanta:	CONST_INT	{
			$$ = TIP_INT;
			push(atof($1));
				}
		| CONST_REAL	{
			$$ = TIP_REAL;
			push(atof($1));
				}
		| CONST_CAR	{
			$$ = TIP_CAR;
			push((double)$1[0]);
				}
		;
instr_comp:	lista_instr
		;
lista_instr:	instr
		| lista_instr ';' instr
		;
instr:		/* empty */
		| instr_match
		| instr_read
		| instr_write
		;
instr_match:	variabila MATCH expresie
		;
variabila:	ID
		| ID '[' expresie ']'
		| ID '.' ID
		;
expresie:	factor
		| expresie '+' expresie
		| expresie '-' expresie
		| expresie '*' expresie
		| expresie DIV expresie
		| expresie MOD expresie
		;
factor:		ID
		| constanta {}
		| ID '(' lista_expr ')'
		| '(' expresie ')'
		| ID '[' expresie ']'
		| ID '.' ID
		;
lista_expr:	expresie
		| lista_expr ',' expresie
		;
instr_write:	WRITE '(' lista_elem ')'
		;
lista_elem:	element
		| lista_elem ',' element
		;
element:	expresie
		| CONST_SIR
		;
instr_read:	READ '(' lista_variab ')'
		;
lista_variab:	variabila
		| lista_variab ',' variabila
		;

%%

extern FILE *yyin;

main(int argc, char **argv)
{
  if(argc>1) yyin = fopen(argv[1], "r");
  if((argc>2)&&(!strcmp(argv[2],"-d"))) yydebug = 1;
  if(!yyparse()) fprintf(stderr,"\tO.K.\n");
}

