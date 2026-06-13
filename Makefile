.PHONY: help figures smoke test paper clean package

help:
	@echo "make figures  - regenerate synthetic article illustrations"
	@echo "make smoke    - run the synthetic geometry pipeline"
	@echo "make test     - run unit tests"
	@echo "make paper    - compile the LaTeX article"
	@echo "make clean    - remove generated caches and LaTeX auxiliaries"

figures:
	python scripts/make_figures.py

smoke:
	python scripts/run_synthetic_smoke.py --config configs/rotated_mnist_g1.yaml

test:
	pytest -q

paper: figures
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
	cp paper/main.pdf paper/Geometry_MMALS_G1_Article.pdf

clean:
	cd paper && latexmk -c || true
	rm -rf .pytest_cache src/geometry_mmalls/__pycache__ tests/__pycache__
