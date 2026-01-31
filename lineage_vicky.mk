#
# Copyright (C) 2025 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Evolution X stuff.
$(call inherit-product, vendor/evolution/config/common_full_phone.mk)

# Inherit from vicky device.
$(call inherit-product, device/motorola/vicky/device.mk)

# EvolutionX flags
EVO_BUILD_TYPE := Unofficial
TARGET_BOOT_ANIMATION_RES := 1080
TARGET_BUILD_APERTURE_CAMERA := false
TARGET_HAS_UDFPS := true
TARGET_SUPPORTS_QUICK_TAP := true
PERF_ANIM_OVERRIDE := true

## Device identifier
PRODUCT_BRAND := motorola
PRODUCT_DEVICE := vicky
PRODUCT_MANUFACTURER := motorola
PRODUCT_NAME := evolution_vicky

PRODUCT_GMS_CLIENTID_BASE := android-motorola

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="vicky_g_sys-user 13 T2SVS33.68-21-6-13 9ff85-633df5 release-keys"
