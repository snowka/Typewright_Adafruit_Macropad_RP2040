# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries. Modified by Scott Nowka.
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: TypeWright TEI XML Tags

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'TypeWright', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x101010, 'Del', [Keycode.CONTROL, Keycode.DELETE]),
        (0x800000, 'Ital', ['<hi rend=\"italic\">...</hi>']),
        (0x101010, 'Correct', [Keycode.CONTROL, Keycode.ENTER]),
        
        # 2nd row ----------
        (0x004000, 'End', [77]),
        (0x004000, 'Illegible', ['@']),
        (0x004000, 'Up', [82]),
        
        # 3rd row ----------
        (0x004000, 'Insert', [Keycode.CONTROL, Keycode.I]),
        (0x000040, 'Header', ['<fw type=\"header\">...</fw>']),
        (0x004000, 'Down', [81]),
        
        # 4th row ---------
        (0x000040, 'PagNum', ['<fw type=\"pageNum\">...</fw>']),
        (0x000040, 'Sig', ['<fw type=\"sig\">...</fw>']),
        (0x000040, 'Catch', ['<fw type=\"catch\">...</fw>']),

        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
