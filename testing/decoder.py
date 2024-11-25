from Frame import Frame
from Signal import Signal

# Create a Frame with a PGN as the frame ID
pgn = 65267  # Example PGN
frame_size = 8  # Assume the PGN frame size is 8 bytes

engine_temp_frame = Frame(frame_id=pgn, frame_size=frame_size, frame_name="Engine Temperature 1")
print(f"Created frame: {engine_temp_frame}")

# Add Engine Coolant Temperature signal (SPN 110)
result = engine_temp_frame.add_signal(
    signal_name="Engine Coolant Temperature",
    signal_start_bit=24,
    signal_size=8,
    signal_is_little_endian=True, 
    signal_is_signed=False,
    signal_is_float=False,
    signal_factor=1,
    signal_offset=-40
)
print(f"Added Engine Coolant Temperature signal: {result}")

# Add Fuel Temperature signal (SPN 174)
result = engine_temp_frame.add_signal(
    signal_name="Fuel Temperature",
    signal_start_bit=16,
    signal_size=8,
    signal_is_little_endian=True, 
    signal_is_signed=False,
    signal_is_float=False,
    signal_factor=0.5,
    signal_offset=-50
)
print(f"Added Fuel Temperature signal: {result}")
print(f"Frame after adding signals: {engine_temp_frame}")


# Example raw CAN data for PGN 65267 (Engine Temperature 1)
raw_data = [0xFF, 0x00, 0x20, 0x64, 0xFF, 0xFF, 0xFF, 0xFF]  # Example data payload (8 bytes)


print(len(engine_temp_frame.signals))

# Decode each signal using the properties defined in the frame
def extract_raw_value(data, start_bit, size, is_little_endian):
    # Implement the bit extraction logic based on start bit, size, and endianess
    # This function will vary depending on how you handle the byte/bit extraction
    # Placeholder implementation here:
    byte_index = start_bit // 8
    return data[byte_index]  # Simplified example for single byte extraction

for signal in engine_temp_frame.signals:
    print("run")
    # Extract raw value based on start bit and size
    raw_value = extract_raw_value(raw_data, signal.start_bit, signal.size, signal.is_little_endian)

    # Apply scaling factor and offset
    decoded_value = (raw_value * signal.factor) + signal.offset
    print(f"{signal.name}: {decoded_value}")

# Function to extract raw value from CAN data (simplified)

