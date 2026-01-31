Device Tree for motorola moto g72 (vicky)
==========================================

The motorola moto g72 (codenamed _"vicky"_) is a mid-range smartphone from motorola.
It was released in September 2022.

| Basic                   | Spec Sheet                                                                                                                     |
| -----------------------:|:------------------------------------------------------------------------------------------------------------------------------ |
| CPU                     | Octa-core (2x2.4 GHz Cortex-A78 & 6x2.0 GHz Cortex-A55)                                                 |
| Chipset                 | MediaTek MT6789 Dimensity 930 (6 nm)                                                                                       |
| GPU                     | Mali-G68 MC4                                                                                                                   |
| Memory                  | 6/8 GB RAM                                                                                                                     |
| Shipped Android Version | 12.0                                                                                                                           |
| Storage                 | 128/256 GB                                                                                                                    |
| Battery                 | Non-removable Li-Po 5000 mAh battery 33W                                                                                           |
| Display                 | pOLED 120Hz, 700 nits (typ), 1000 nits (HBM)                               |
| Camera (Back)(Main)     | 108 MP, f/1.7, 26mm (wide), PDAF, OIS                                                                                 |
| Camera (Front)          | 16 MP, f/2.2, 26mm (wide)    

## Device picture
![vicky](https://fdn2.gsmarena.com/imgroot/news/22/09/motorola-moto-g72-official/-1200w5/gsmarena_001.jpg)

## Device specifications

### Hardware
- **SoC**: MediaTek MT6789 Dimensity 930
- **CPU**: Octa-core (2x2.4 GHz Cortex-A78 & 6x2.0 GHz Cortex-A55)
- **GPU**: Mali-G68 MC4
- **RAM**: 6GB/8GB LPDDR4X
- **Storage**: 128GB/256GB UFS 2.2
- **Display**: 6.6" pOLED, 2400x1080, 120Hz refresh rate
- **Battery**: 5000mAh Li-Po with 33W fast charging
- **Rear Camera**: 108MP main + 8MP ultrawide + 2MP macro
- **Front Camera**: 16MP
- **Connectivity**: Wi-Fi 802.11 a/b/g/n/ac, Bluetooth 5.3, USB Type-C 2.0
- **Sensors**: Fingerprint (under display), accelerometer, gyro, proximity, compass

### Software
- **Original Android Version**: Android 12
- **Current LineageOS Support**: LineageOS 21 (Android 13)
- **Bootloader**: Unlocked bootloader available
- **Root Access**: Magisk supported

## Features

### Working
- **Booting**: Device boots successfully
- **Display**: Full resolution and refresh rate support
- **Touch**: Touchscreen fully functional
- **Audio**: Both speakers and microphone working
- **Wi-Fi**: Wireless connectivity functional
- **Bluetooth**: Bluetooth pairing and data transfer working
- **Camera**: Both rear and front cameras functional
- **Sensors**: All main sensors including fingerprint working
- **RIL**: Calls, SMS, and mobile data functional
- **GPS**: Location services working
- **Charging**: Battery charging and monitoring functional

### Not Working
- **NFC**: Not yet implemented
- **5G**: 4G only, 5G bands not yet supported

### Partial Working
- **Video Recording**: Works but may have stabilization issues
- **Fast Charging**: Basic charging works, full 33W fast charging needs optimization

## Installation

### Prerequisites
- Unlocked bootloader
- Latest TWRP or custom recovery
- LineageOS 21 build for vicky

### Steps
1. Download the latest LineageOS build and GApps (optional)
2. Reboot to recovery
3. Wipe data/factory reset
4. Install LineageOS zip
5. Install GApps (if desired)
6. Reboot to system

## Build Instructions

### Setup
```bash
# Initialize LineageOS repo
repo init -u https://github.com/LineageOS/android.git -b lineage-21 --git-lfs

# Sync the source
repo sync

# Clone device tree
git clone https://github.com/your-repo/android_device_motorola_vicky device/motorola/vicky

# Clone vendor tree
git clone https://github.com/your-repo/android_vendor_motorola_vicky vendor/motorola/vicky
```

### Build
```bash
# Set up environment
source build/envsetup.sh

# Configure build
lunch lineage_vicky-userdebug

# Build
m -j$(nproc) bacon
```

## Contributing

Contributions are welcome! Please follow these guidelines:
- Test your changes before submitting
- Use proper commit messages following LineageOS style
- Don't mix different changes in one commit
- Follow the existing code style

## Sources

- **Device Tree**: https://github.com/LineageOS/android_device_motorola_vicky
- **Kernel**: https://github.com/LineageOS/android_kernel_motorola_vicky
- **Vendor**: https://github.com/LineageOS/android_vendor_motorola_vicky

## Credits

- LineageOS Project for the base ROM
- Motorola for device specifications
- Contributors who helped with development and testing

## License

```
#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#
```
