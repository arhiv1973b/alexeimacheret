#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
JSON Viewer for combined_pdf_summaries.json
Allows searching and viewing PDF data from the consolidated JSON.
"""

import json
import sys
from pathlib import Path

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return None

def search_pdfs(data, query):
    results = {}
    query_lower = query.lower()
    for pdf_name, info in data.items():
        if query_lower in pdf_name.lower() or query_lower in info.get('raw_text', '').lower() or query_lower in info.get('cleaned_text', '').lower():
            results[pdf_name] = info
    return results

def display_pdf_info(pdf_name, info):
    print(f"\n=== {pdf_name} ===")
    print(f"Path: {info['pdf_path']}")
    print(f"Raw text length: {len(info['raw_text'])} chars")
    print(f"Cleaned text length: {len(info['cleaned_text'])} chars")
    print(f"Russian summary: {len(info['summary_ru'])} items")
    print(f"Romanian summary: {len(info['summary_ro'])} items")
    print(f"Translations: {len(info['translations'])} items")
    print("Raw text (first 500 chars):")
    print(info['raw_text'][:500] + "...")
    print("Cleaned text (first 500 chars):")
    print(info['cleaned_text'][:500] + "...")
    print("Russian summary:")
    for i, s in enumerate(info['summary_ru'], 1):
        print(f"  {i}. {s}")
    print("Romanian summary:")
    for i, s in enumerate(info['summary_ro'], 1):
        print(f"  {i}. {s}")

def main():
    json_path = Path(__file__).parent / "combined_pdf_summaries.json"
    if not json_path.exists():
        print(f"JSON file not found at {json_path}. Please specify path.")
        json_path = input("Enter JSON file path: ")
        json_path = Path(json_path)
    
    data = load_json(json_path)
    if not data:
        return
    
    print(f"Loaded data for {len(data)} PDFs.")
    
    while True:
        print("\nCommands:")
        print("1. List all PDFs")
        print("2. Search PDFs by query")
        print("3. View PDF details")
        print("4. Export PDF text to file")
        print("5. Exit")
        
        choice = input("Choose: ").strip()
        
        if choice == '1':
            for i, pdf in enumerate(data.keys(), 1):
                print(f"{i}. {pdf}")
        
        elif choice == '2':
            query = input("Enter search query: ").strip()
            results = search_pdfs(data, query)
            if results:
                print(f"Found {len(results)} matches:")
                for pdf in results.keys():
                    print(f"  - {pdf}")
            else:
                print("No matches found.")
        
        elif choice == '3':
            pdf_name = input("Enter PDF name: ").strip()
            if pdf_name in data:
                display_pdf_info(pdf_name, data[pdf_name])
            else:
                print("PDF not found.")
        
        elif choice == '4':
            pdf_name = input("Enter PDF name: ").strip()
            if pdf_name in data:
                output_file = Path(pdf_name).with_suffix('.txt')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(data[pdf_name]['cleaned_text'])
                print(f"Exported to {output_file}")
            else:
                print("PDF not found.")
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()