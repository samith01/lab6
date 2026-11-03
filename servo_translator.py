# Submit this file via brightspace

# You should not modify the signature (name, input, return type) of this function
def translate(angle: float) -> int:
	"""
	Converts an angle in degrees to the corresponding input
	for the duty_u16 method of the servo class

	See https://docs.micropython.org/en/latest/library/machine.PWM.html for more
	details on the duty_u16 method
	"""

	# keep the angle within the servo's range (0-180 degrees) so the pulse width
	# never goes outside 500-2500 us, which could damage the servo
	if angle > 180:
		angle = 180
	elif angle < 0:
		angle = 0

	pulse_width = 500 + (2500 - 500) * angle / 180  # linear interpolation between min and max pulse widths (us)
	duty_cycle = pulse_width / 20000  # fraction of the 20000 us (50 Hz) period that the signal is high
	return int(duty_cycle * 65535)  # scale to the 0-65535 range used by duty_u16
