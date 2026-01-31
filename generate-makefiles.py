#!/usr/bin/env python3
"""
Simple makefile generator for vicky vendor tree
"""
import os
from pathlib import Path

def generate_android_bp():
    """Generate Android.bp for vendor tree"""
    vendor_path = "vendor/motorola/vicky"
    
    # Find all .so files
    so_files = []
    for root, dirs, files in os.walk(vendor_path):
        for file in files:
            if file.endswith('.so'):
                rel_path = os.path.relpath(os.path.join(root, file), vendor_path)
                so_files.append(rel_path)
    
    # Generate Android.bp content
    content = """//
// Copyright (C) 2025 The LineageOS Project
//
// SPDX-License-Identifier: Apache-2.0
//

soong_namespace {
}

// Prebuilt libraries
"""
    
    for so_file in sorted(so_files):
        module_name = so_file.replace('/', '_').replace('.so', '').replace('-', '_').replace('.', '_')
        relative_path = f"motorola/vicky/{so_file}"
        
        content += f"""
prebuilt_etc {{
    name: "{module_name}",
    src: "{relative_path}",
    vendor: true,
    relative_install_path: "{os.path.dirname(so_file)}",
}}
"""
    
    return content

def main():
    android_bp_content = generate_android_bp()
    
    # Write Android.bp
    with open("vendor/motorola/vicky/Android.bp", "w") as f:
        f.write(android_bp_content)
    
    print("✅ Generated vendor/motorola/vicky/Android.bp")
    print(f"📊 Found {len(android_bp_content.split('prebuilt_etc')) - 1} prebuilt libraries")

if __name__ == "__main__":
    main()
