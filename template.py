import os

# Assuming you are running this script from inside your project folder
current_dir = os.getcwd()  # Get current working directory

# List of directories to create
directories = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "reports/figures"
]

# List of files to create
files = [
    "README.md",
    "requirements.txt",
    ".gitignore",
    "LICENSE",
    "src/__init__.py",
    "src/data_preprocessing.py",
    "src/portfolio_optimization.py",
    "src/risk_analysis.py",
    "src/visualization.py"
]

# Create directories
for dir in directories:
    path = os.path.join(current_dir, dir)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")

# Create files
for file in files:
    path = os.path.join(current_dir, file)
    if not os.path.exists(path):  # Avoid overwriting if already exists
        with open(path, 'w') as f:
            pass  # Empty file
        print(f"File created: {path}")
    else:
        print(f"File already exists: {path}")

print("\nProject structure created successfully!")