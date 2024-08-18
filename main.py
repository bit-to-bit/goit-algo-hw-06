print(hex(16) + hex(16))

print(f'{255:x}')         # => 'ff'   
print(f'{15:2x}')         # => ' f'    
print(f'{15:02x}')        # => '0f'    
print(f'\\x{15:02x}{16:02x}{30:02x}')     # => '\x0f'  