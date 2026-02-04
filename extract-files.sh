#!/bin/bash
#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

set -e

# Load extraction library
export DEVICE=vicky
export VENDOR=motorola
export DEVICE_BRINGUP_BOOTSTRAP=1

# Point this to your LOS 20 root
MY_DIR="${BASH_SOURCE%/*}"
if [[ ! -d "${MY_DIR}" ]]; then MY_DIR="${PWD}"; fi

LINEAGE_ROOT="${MY_DIR}/../../.."

helper="${LINEAGE_ROOT}/tools/extract-utils/extract_utils.sh"
if [ ! -f "${helper}" ]; then
    echo "Unable to find helper script at ${helper}"
    exit 1
fi
source "${helper}"

# Default to extracting from a local dump
SECTION=
KANG=

while [ "${#}" -gt 0 ]; do
    case "${1}" in
        -n | --no-cleanup )
                CLEAN_UP=false
                ;;
        -k | --kang )
                KANG="--kang"
                ;;
        -s | --section )
                SECTION="${2}"; shift
                ;;
        * )
                SRC="${1}"
                ;;
    esac
    shift
done

if [ -z "${SRC}" ]; then
    SRC=adb
fi

# Initialize the helper
setup_vendor "${DEVICE}" "${VENDOR}" "${LINEAGE_ROOT}" false "${CLEAN_UP}"

# extract "${SRC}" "${MY_DIR}/proprietary-files.txt" "${KANG}" "${SECTION}"

extract "${MY_DIR}/proprietary-files.txt" "${SRC}" "${KANG}" "${SECTION}"

"${MY_DIR}/setup-makefiles.sh"
