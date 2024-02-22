
PRODUCT_PACKAGES += \
    ksigam

PRODUCT_COPY_FILES += \
    vendor/magisk/magisk.rc:$(TARGET_COPY_OUT_VENDOR)/etc/init/ksigam.rc \
    $(call find-copy-subdir-files,*,vendor/magisk/rootfs/vendor/etc/init,$(TARGET_COPY_OUT_VENDOR)/etc/init) \

