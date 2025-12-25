# Tools
A collection of useful utility tools for everyday tasks.

## Available Tools

### 1. File Organizer
A Python utility to automatically organize files in a directory based on various criteria.

#### Features
- **Organize by Extension**: Groups files by their file extension (e.g., .pdf, .jpg, .txt)
- **Organize by Date**: Groups files by modification date (Year/Month structure)
- **Organize by Size**: Categorizes files into Small, Medium, and Large
- **Dry Run Mode**: Preview changes before applying them

#### Usage

```bash
# Basic usage - organize by extension
python file_organizer.py /path/to/directory

# Organize by date
python file_organizer.py /path/to/directory --by date

# Organize by size
python file_organizer.py /path/to/directory --by size

# Preview changes without moving files
python file_organizer.py /path/to/directory --dry-run
```

#### Examples

**Organize Downloads folder by extension:**
```bash
python file_organizer.py ~/Downloads --by extension
```
This will create subdirectories like `pdf/`, `jpg/`, `txt/` and move files accordingly.

**Organize photos by date:**
```bash
python file_organizer.py ~/Pictures --by date
```
This will create a structure like `2025/December/`, `2025/November/` with files organized by modification date.

**Check what would happen (dry run):**
```bash
python file_organizer.py ~/Documents --dry-run
```
This will show what changes would be made without actually moving any files.

#### Requirements
- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

No installation required. Simply clone this repository and run the tools directly:

```bash
git clone https://github.com/gpt37-463/Tools.git
cd Tools
python file_organizer.py --help
```

## Contributing

Feel free to contribute new tools or improvements to existing ones!
