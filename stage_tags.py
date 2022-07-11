# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries. Modified by Scott Nowka.
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: TEI XML Tags for Drama

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Drama XML Tags', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x101010, 'Set', ['<stage type="setting">...</stage>']),
        (0x800000, 'Ent', ['<stage type="entrance">...</stage>']),
        (0x101010, 'Exit', ['<stage type="exit">...</stage>']),
        
        # 2nd row ----------
        (0x004000, 'Busi', ['<stage type="business">...</stage>']),
        (0x004000, 'Stage', ['<stage>...</stage>']),
        (0x004000, 'Deli', ['<stage type="delivery">...</stage>']),
        
        # 3rd row ----------
        (0x004000, 'Sp-p', ['<sp who="#...">\n
        <speaker><hi rend="italic">...</hi>.</speaker>\n
        <p>...</p>\n
        </sp>\n']),
        (0x000040, 'Break', ['<lb/>']),
        (0x004000, 'Sp-l', ['<sp who="#...">\n
        <speaker><hi rend="italic">...</hi>.</speaker>\n
        <lg>\n
        <l></>\n
        </lg>\n
        </sp>\n']),
        
        # 4th row ---------
        (0x000040, 'CastL', ['<castList></castList>']),
        (0x000040, 'CastG', ['<castGroup></castGroup>']),
        (0x000040, 'Item', ['<castItem type="role">\n
        <actor>...</actor>\n
        <role xml:id="..."><hi rend="italic">...</hi></role>\n
        <roleDesc>...</roleDesc>\n
        </castItem>']),

        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
