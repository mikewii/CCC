.section .jump,"ax",%progbits
.align 2
.arch armv6k
.syntax unified
.arm
.global jump

jump:
	bl fun