# Micropython Stepper Motor Blind Opener

Blind opener designed to work with the M5 Stack Atom,
the M5 Stack stepper driver, a NEMA 17,
and a 3d printed gear to hold the blind cord.

# Getting code on the board
Assuming the board is at /dev/ttyUSB0.

## Flash board with micropython
`python -m esptool --chip esp32 --port /dev/ttyUSB0 --baud 115200 write_flash -z 0x1000 M5STACK_ATOM-20220117-v1.18.bin`

## Put code on board
`/tools/deploy_dev /dev/ttyUSB0`

## Connect to debug
`picocom /dev/ttyUSB0 -b115200`
