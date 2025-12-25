#!/usr/bin/env python3
"""
File Organizer Tool
A utility to organize files in a directory by various criteria such as file extension,
creation date, or file size.
"""

import os
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict


class FileOrganizer:
    """Main class for organizing files in a directory."""
    
    def __init__(self, source_dir, organize_by='extension', dry_run=False):
        """
        Initialize the FileOrganizer.
        
        Args:
            source_dir (str): Source directory containing files to organize
            organize_by (str): Method to organize files ('extension', 'date', 'size')
            dry_run (bool): If True, only show what would be done without actual changes
        """
        self.source_dir = Path(source_dir)
        self.organize_by = organize_by
        self.dry_run = dry_run
        
        if not self.source_dir.exists():
            raise ValueError(f"Source directory does not exist: {source_dir}")
    
    def organize_by_extension(self):
        """Organize files by their extension into subdirectories."""
        files_moved = 0
        extension_groups = defaultdict(list)
        
        # Group files by extension
        for item in self.source_dir.iterdir():
            if item.is_file():
                ext = item.suffix.lower() if item.suffix else 'no_extension'
                extension_groups[ext].append(item)
        
        # Move files to extension-based directories
        for ext, files in extension_groups.items():
            if ext == 'no_extension':
                folder_name = 'No_Extension'
            else:
                folder_name = ext.lstrip('.')
            
            target_dir = self.source_dir / folder_name
            
            if not self.dry_run:
                target_dir.mkdir(exist_ok=True)
            
            for file in files:
                target_path = target_dir / file.name
                
                if self.dry_run:
                    print(f"[DRY RUN] Would move: {file} -> {target_path}")
                else:
                    try:
                        shutil.move(str(file), str(target_path))
                        print(f"Moved: {file.name} -> {folder_name}/")
                        files_moved += 1
                    except Exception as e:
                        print(f"Error moving {file.name}: {e}")
        
        return files_moved
    
    def organize_by_date(self):
        """Organize files by their modification date (Year/Month format)."""
        files_moved = 0
        
        for item in self.source_dir.iterdir():
            if item.is_file():
                # Get file modification time
                mod_time = datetime.fromtimestamp(item.stat().st_mtime)
                year_month = mod_time.strftime('%Y/%B')
                
                target_dir = self.source_dir / year_month
                target_path = target_dir / item.name
                
                if not self.dry_run:
                    target_dir.mkdir(parents=True, exist_ok=True)
                
                if self.dry_run:
                    print(f"[DRY RUN] Would move: {item} -> {target_path}")
                else:
                    try:
                        shutil.move(str(item), str(target_path))
                        print(f"Moved: {item.name} -> {year_month}/")
                        files_moved += 1
                    except Exception as e:
                        print(f"Error moving {item.name}: {e}")
        
        return files_moved
    
    def organize_by_size(self):
        """Organize files by their size categories."""
        files_moved = 0
        
        def get_size_category(size_bytes):
            """Categorize file size."""
            if size_bytes < 1024 * 100:  # < 100 KB
                return 'Small_Files'
            elif size_bytes < 1024 * 1024 * 10:  # < 10 MB
                return 'Medium_Files'
            else:
                return 'Large_Files'
        
        for item in self.source_dir.iterdir():
            if item.is_file():
                size = item.stat().st_size
                category = get_size_category(size)
                
                target_dir = self.source_dir / category
                target_path = target_dir / item.name
                
                if not self.dry_run:
                    target_dir.mkdir(exist_ok=True)
                
                if self.dry_run:
                    print(f"[DRY RUN] Would move: {item} -> {target_path}")
                else:
                    try:
                        shutil.move(str(item), str(target_path))
                        print(f"Moved: {item.name} -> {category}/")
                        files_moved += 1
                    except Exception as e:
                        print(f"Error moving {item.name}: {e}")
        
        return files_moved
    
    def organize(self):
        """Execute the organization based on the selected method."""
        print(f"Organizing files in: {self.source_dir}")
        print(f"Method: {self.organize_by}")
        
        if self.dry_run:
            print("\n[DRY RUN MODE - No files will be moved]\n")
        
        if self.organize_by == 'extension':
            files_moved = self.organize_by_extension()
        elif self.organize_by == 'date':
            files_moved = self.organize_by_date()
        elif self.organize_by == 'size':
            files_moved = self.organize_by_size()
        else:
            raise ValueError(f"Unknown organization method: {self.organize_by}")
        
        if not self.dry_run:
            print(f"\nTotal files moved: {files_moved}")
        
        return files_moved


def main():
    """Main entry point for the command-line interface."""
    parser = argparse.ArgumentParser(
        description='Organize files in a directory by extension, date, or size.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Organize files by extension (default)
  python file_organizer.py /path/to/directory
  
  # Organize files by date
  python file_organizer.py /path/to/directory --by date
  
  # Organize files by size
  python file_organizer.py /path/to/directory --by size
  
  # Preview changes without moving files (dry run)
  python file_organizer.py /path/to/directory --dry-run
        """
    )
    
    parser.add_argument(
        'directory',
        help='Directory containing files to organize'
    )
    
    parser.add_argument(
        '--by',
        choices=['extension', 'date', 'size'],
        default='extension',
        help='Method to organize files (default: extension)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without actually moving files'
    )
    
    args = parser.parse_args()
    
    try:
        organizer = FileOrganizer(
            source_dir=args.directory,
            organize_by=args.by,
            dry_run=args.dry_run
        )
        organizer.organize()
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
