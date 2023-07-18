# we can also know the generic name of the processor and generic OS name and the OS version

from platform import machine, processor, system, version

print("Machine:", machine())

print("Processor:", processor())

print("Operating System:", system())

print("OS Version:", version())
