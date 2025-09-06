.PHONY: all clean install train-pipeline data-pipeline streaming-inference run-all help

# Use PowerShell for all recipes and keep each target in a single shell session
SHELL := pwsh
.SHELLFLAGS := -NoProfile -Command
.ONESHELL:

# Config
PYTHON := python
ACTIVATE := . .\.venv\Scripts\Activate.ps1;

# Default target
all: help

# Help target
help:
	@echo "Available targets:"
	@echo "  make install             - Install project dependencies and set up environment"
	@echo "  make data-pipeline       - Run the data pipeline"
	@echo "  make train-pipeline      - Run the training pipeline"
	@echo "  make streaming-inference - Run the streaming inference pipeline with the sample JSON"
	@echo "  make run-all             - Run all pipelines in sequence"
	@echo "  make clean               - Clean up artifacts"

# Install project dependencies and set up environment
install:
	@echo "Installing project dependencies and setting up environment..."
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv .venv
	@echo "Activating virtual environment and installing dependencies..."
	$(ACTIVATE) python -m pip install --upgrade pip
	$(ACTIVATE) pip install -r requirements.txt
	@echo "Installation completed successfully!"
	@echo "To activate the virtual environment in PowerShell, run: . .\\.venv\\Scripts\\Activate.ps1"

# Clean up
clean:
	@echo "Cleaning up artifacts..."
	if (Test-Path "artifacts\\models") { Remove-Item "artifacts\\models\\*" -Recurse -Force -ErrorAction SilentlyContinue }
	if (Test-Path "artifacts\\evaluation") { Remove-Item "artifacts\\evaluation\\*" -Recurse -Force -ErrorAction SilentlyContinue }
	if (Test-Path "artifacts\\predictions") { Remove-Item "artifacts\\predictions\\*" -Recurse -Force -ErrorAction SilentlyContinue }
	if (Test-Path "data\\processed") { Remove-Item "data\\processed\\*" -Recurse -Force -ErrorAction SilentlyContinue }
	@echo "Cleanup completed!"

# Run data pipeline
data-pipeline:
	@echo "Running data pipeline..."
	$(ACTIVATE) $(PYTHON) pipelines\\data_pipeline.py

# Run training pipeline
train-pipeline:
	@echo "Running training pipeline..."
	$(ACTIVATE) $(PYTHON) pipelines\\training_pipeline.py

# Run streaming inference pipeline with sample JSON
streaming-inference:
	@echo "Running streaming inference pipeline with sample JSON..."
	$(ACTIVATE) $(PYTHON) pipelines\\streaming_inference_pipeline.py

# Run all pipelines in sequence
run-all:
	@echo "Running all pipelines in sequence..."
	@echo "========================================"
	@echo "Step 1: Running data pipeline"
	@echo "========================================"
	$(ACTIVATE) $(PYTHON) pipelines\\data_pipeline.py
	@echo "`n========================================"
	@echo "Step 2: Running training pipeline"
	@echo "========================================"
	$(ACTIVATE) $(PYTHON) pipelines\\training_pipeline.py
	@echo "`n========================================"
	@echo "Step 3: Running streaming inference pipeline"
	@echo "========================================"
	$(ACTIVATE) $(PYTHON) pipelines\\streaming_inference_pipeline.py
	@echo "`n========================================"
	@echo "All pipelines completed successfully!"
	@echo "========================================"
