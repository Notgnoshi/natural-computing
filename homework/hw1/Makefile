PROJECT_NAME := hw1
SRC := $(shell find . -name '*.tex') homework.sty

.PHONY: $(PROJECT_NAME).pdf all clean view

all: $(PROJECT_NAME).pdf $(SRC)

$(PROJECT_NAME).pdf: $(PROJECT_NAME).tex
	# Alternatively, use batchmode to elliminate console spam
	# latexmk -pdf --synctex=1 -file-line-error -interaction=batchmode -shell-escape $<
	latexmk -pdf --synctex=1 -file-line-error -interaction=nonstopmode -shell-escape $<

# A target to build with better error messages when latexmk craps itself.
error:
	pdflatex -shell-escape -file-line-error $(PROJECT_NAME).tex

clean:
	latexmk -C
	rm -rf *.bbl *.tdo

view:
	1>/dev/null 2>/dev/null xdg-open $(PROJECT_NAME).pdf &

# Sure, I could make them dependencies, or I could not.
generate:
	jupyter-nbconvert --ExecutePreprocessor.timeout=120 --execute --inplace prob1/prob1.ipynb
	jupyter-nbconvert --ExecutePreprocessor.timeout=120 --execute --inplace prob2/prob2.ipynb
	jupyter-nbconvert --ExecutePreprocessor.timeout=120 --execute --inplace prob3/prob3.ipynb
