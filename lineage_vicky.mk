#
# Copyright (C) 2026 The LineageOS Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common LineageOS stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from vicky device.
$(call inherit-product, device/motorola/vicky/device.mk)

# Device identifier. This must match your lunch combo
PRODUCT_DEVICE := vicky
PRODUCT_NAME := lineage_vicky
PRODUCT_BRAND := alps
PRODUCT_MODEL := vicky
PRODUCT_MANUFACTURER := motorola

PRODUCT_GMS_CLIENTID_BASE := android-motorola

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="vicky_g_sys-user 13 T2SVS33.68-21-6-13 9ff85-633df5 release-keys"
