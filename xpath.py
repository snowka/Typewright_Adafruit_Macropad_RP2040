# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries. Modified by Scott Nowka.
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: XPath

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'XPath', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x800000, 'Prec', ['preceding::']),
        (0x800000, 'Anc', ['ancestor::']),
        (0x101010, '!', ['!']),
        
        # 2nd row ----------
        (0x800000, 'P-Sib', ['preceding-sibling::']),
        (0x800000, 'Parent', ['parent::']),
        (0x101010, '=>', ['=>']),
        
        # 3rd row ----------
        (0x101010, 'Node', ['node()']),
        (0x800000, 'Child', ['child::']),
        (0x800000, 'F-Sib', ['following-sibling::']),
        
        # 4th row ---------
        (0x101010, 'Last', ['last()']),
        (0x800000, 'Desc', ['descendant::']),
        (0x800000, 'Follo', ['following::']),

        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
