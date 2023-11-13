#!/vendor/bin/sh

# Copyright (c) 2021, Motorola Mobility LLC, All Rights Reserved.
#
# Date Created: 8/30/2021, Set CXP properties according to carrier channel
#

set_properties()
{
	# do not set SPB ID for M80 modem
	if [ $set_sbp_place ] && [ $set_sbp_place -ge 2 ]; then
		sbp=0
	fi
	setprop ro.vendor.mtk_md_sbp_custom_value $sbp
	setprop ro.vendor.operator.optr $1
	setprop ro.vendor.operator.spec $2
	setprop ro.vendor.operator.seg $3
	if [ ! $optr ]; then
		setprop persist.vendor.mtk_usp_md_sbp_code $sbp
		setprop persist.vendor.operator.optr $1
		setprop persist.vendor.operator.spec $2
		setprop persist.vendor.operator.seg $3
		setprop persist.vendor.mtk_rcs_ua_support $4
	fi
}


boot_carrier=`getprop ro.boot.carrier`
optr=`getprop persist.vendor.operator.optr`
set_sbp_place=`getprop ro.vendor.ril.set_sbp_place`


case $boot_carrier in
	att|attpre )
		sbp=7
		set_properties OP07 SPEC0407 SEGDEFAULT 1
	;;
	cricket )
		sbp=145
		set_properties OP07 SPEC0407 SEGDEFAULT 1
	;;
	tmo|boost|cc|fi|metropcs|tracfone|retus )
		sbp=8
		set_properties OP08 SPEC0200 SEGDEFAULT 1
	;;
	usc )
		sbp=236
		set_properties OP236 SPEC0200 SEGDEFAULT 0
	;;
	vzw|vzwpre|comcast|spectrum )
		sbp=12
		set_properties OP12 SPEC0200 SEGDEFAULT 1
	;;
	* )
		sbp=0
		set_properties "" "" "" 0
	;;
esac

return 0
