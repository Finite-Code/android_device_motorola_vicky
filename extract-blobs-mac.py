#!/usr/bin/env python3
"""
Enhanced blob extraction script for Motorola vicky with su support
"""
import os
import subprocess
import sys

def run_adb_pull(device_id, source, dest, use_su=False):
    """Pull file from device with optional su support"""
    if use_su:
        cmd = f"adb -s {device_id} shell su -c 'cat {source}' > {dest}"
    else:
        cmd = f"adb -s {device_id} pull {source} {dest}"
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            # Check if file was actually created and has content
            if os.path.exists(dest) and os.path.getsize(dest) > 0:
                print(f"✅ Pulled: {source}")
                return True
            else:
                print(f"❌ Empty file: {source}")
                return False
        else:
            error_msg = result.stderr.strip()
            if "Permission denied" in error_msg:
                return "permission_denied"
            elif "No such file" in error_msg:
                print(f"⚠️  Not found: {source}")
                return True  # Skip missing files
            else:
                print(f"❌ Failed to pull: {source} - {error_msg}")
                return False
    except Exception as e:
        print(f"❌ Error pulling {source}: {e}")
        return False

def check_existing_files(vendor_path):
    """Check if vendor tree already exists"""
    if not os.path.exists(vendor_path):
        return False, 0
    
    total_files = 0
    for root, dirs, files in os.walk(vendor_path):
        total_files += len(files)
    
    return True, total_files

def get_user_choice(existing_files):
    """Get user choice for handling existing files"""
    print(f"\n📁 Found existing vendor tree with {existing_files} files!")
    print("Choose an option:")
    print("1. Replace all existing files")
    print("2. Keep existing files, only add new ones")
    print("3. Cancel extraction")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    device_id = "ZD2228B7M9"
    vendor_path = "vendor/motorola/vicky"
    
    # Check for existing files
    has_existing, existing_count = check_existing_files(vendor_path)
    if has_existing:
        choice = get_user_choice(existing_count)
        if choice == 1:
            print("🗑️  Removing existing vendor tree...")
            import shutil
            shutil.rmtree(vendor_path)
        elif choice == 2:
            print("📝 Keeping existing files, will only add new ones...")
        elif choice == 3:
            print("❌ Extraction cancelled.")
            return
    
    # Create vendor directories
    os.makedirs(f"{vendor_path}/bin/hw", exist_ok=True)
    os.makedirs(f"{vendor_path}/etc", exist_ok=True)
    os.makedirs(f"{vendor_path}/lib/hw", exist_ok=True)
    os.makedirs(f"{vendor_path}/lib64/hw", exist_ok=True)
    os.makedirs(f"{vendor_path}/lib64/mt6789", exist_ok=True)
    os.makedirs(f"{vendor_path}/firmware", exist_ok=True)
    
    # Read proprietary files list
    with open("proprietary-files.txt", "r") as f:
        files = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    
    print(f"\n📱 Extracting {len(files)} blobs from device...")
    print("=" * 60)
    
    success_count = 0
    permission_denied_count = 0
    not_found_count = 0
    
    for i, file_path in enumerate(files, 1):
        dest_path = f"{vendor_path}/{file_path}"
        dest_dir = os.path.dirname(dest_path)
        
        # Skip if file already exists and we're keeping existing files
        if has_existing and os.path.exists(dest_path):
            continue
        
        # Create destination directory
        os.makedirs(dest_dir, exist_ok=True)
        
        # Try normal pull first
        result = run_adb_pull(device_id, file_path, dest_path, use_su=False)
        
        if result == "permission_denied":
            # Try with su
            print(f"🔐 Trying with su for: {file_path}")
            result = run_adb_pull(device_id, file_path, dest_path, use_su=True)
            if result == "permission_denied":
                permission_denied_count += 1
            elif result:
                success_count += 1
        elif result:
            success_count += 1
        
        # Progress indicator
        if i % 50 == 0 or i == len(files):
            progress = (i / len(files)) * 100
            print(f"📊 Progress: {i}/{len(files)} ({progress:.1f}%)")
    
    print("\n" + "=" * 60)
    print("🎉 Extraction complete!")
    print(f"✅ Successfully extracted: {success_count}/{len(files)} files")
    if permission_denied_count > 0:
        print(f"🔐 Permission denied (even with su): {permission_denied_count} files")
    print(f"📁 Vendor tree created at: {vendor_path}")
    
    # Count extracted files
    total_extracted = 0
    for root, dirs, files in os.walk(vendor_path):
        total_extracted += len(files)
    
    print(f"📊 Total files in vendor tree: {total_extracted}")
    
    # Next steps
    print(f"\n🚀 Next steps:")
    print(f"1. Run: ./setup-makefiles.py")
    print(f"2. Transfer vendor tree to build server")
    print(f"3. Build LineageOS!")

if __name__ == "__main__":
    main()
