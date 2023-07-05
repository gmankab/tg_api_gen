import string
from pathlib import Path
from random import (
    choice,
    randint,
)


proj_name = 'tg_api_gen'
proj_version = '23.0.1'


def get_device_and_ios_major() -> tuple:
    devices_and_ioses = [
        [
            ['6', '6 Plus', '6S', '6S Plus'],
            [12, 15],
        ],
        [
            ['7', '7 Plus'],
            [12, 15],
        ],
        [
            ['8', '8 Plus'],
            [12, 16],
        ],
        [
            ['X', 'XS', 'XS Max', 'XR'],
            [12, 16],
        ],
        [
            ['11', '11 Pro', '11 Pro Max'],
            [12, 16],
        ],
        [
            ['12', '12 mini', '12 Pro', '12 Pro Max'],
            [14, 16]
        ],
        [
            ['13', '13 mini', '13 Pro', '13 Pro Max'],
            [15, 16]
        ],
        [
            ['14', '14 Plus', '14 Pro', '14 Pro Max'],
            [16]
        ],
    ]
    devices, ios_majors = choice(devices_and_ioses)
    device_model: str = 'iPhone ' + choice(devices)
    if len(ios_majors) == 1:
        ios_major: int = ios_majors[0]
    else:
        ios_major = choice(
            range(
                ios_majors[0],
                ios_majors[1] + 1,
            )
        )
    return device_model, ios_major


def get_ios_major(
    major_list: list,
):
    if len(major_list) == 1:
        return major_list[0]
    else:
        return choice(
            range(
                major_list[0],
                major_list[1] + 1,
            )
        )


def get_device_model_android():
    android_devices_path = Path(
        __file__
    ).parent.resolve() / 'android_devices.txt'
    return choice(
        list(
            android_devices_path.open('r')
        )
    ).strip('\n')


def get_ios_system_version(
    major: int
) -> str:
    versions: dict = {
        16: [
            [16, 0, 3],
            [16, 1, 2],
            [16, 2, 0],
            [16, 3, 1],
            [16, 4, 1],
            [16, 5, 1],
        ],
        15: [
            [15, 0, 2],
            [15, 1, 1],
            [15, 2, 1],
            [15, 3, 1],
            [15, 4, 1],
            [15, 5, 6],
            [15, 6, 1],
            [15, 7, 7],
        ],
        14: [
            [14, 0, 1],
            [14, 1, 0],
            [14, 2, 1],
            [14, 3, 0],
            [14, 4, 2],
            [14, 5, 1],
            [14, 6, 0],
            [14, 7, 1],
            [14, 8, 1],
        ],
        13: [
            [13, 1, 3],
            [13, 2, 3],
            [13, 3, 1],
            [13, 4, 1],
            [13, 5, 1],
            [13, 6, 1],
            [13, 7, 0],
        ],
        12: [
            [12, 0, 1],
            [12, 1, 4],
            [12, 2, 0],
            [12, 3, 2],
            [12, 4, 9],
            [12, 5, 7],
        ],
    }
    return version_to_str(
        *choice(
            versions[major]
        )
    )


def get_android_system_version():
    return choice(
        [
            '7 N MR1 (25)',
            '8 O MR1 (26)',
            '8.1 O MR1 (27)',
            '9 P (28)',
            '10 Q (29)',
            '11 (30)',
            '12 (31)',
            # '12L (32)',
            '13 (33)',
        ]
    )


def version_to_str(
    major: int,
    minor: int,
    patch: int,
) -> str:
    patch = choice(range(patch + 1))
    if minor and patch:
        return f'{major}.{minor}.{patch}'
    elif minor:
        return f'{major}.{minor}'
    else:
        return str(major)


def get_ios_app_version() -> str:
    versions = [
        [9, 6, 3],
        [9, 5, 3],
        [9, 4, 2],
    ]
    return 'Telegram IOS ' + version_to_str(
        *choice(versions)
    )


def get_android_app_version() -> str:
    versions = [
        [9, 6, 7],
        [9, 5, 8],
        [9, 4, 9],
    ]
    return 'Telegram Android ' + version_to_str(
        *choice(versions)
    )


def generate_ios() -> dict:
    app_version = get_ios_app_version()
    device_model, ios_major = get_device_and_ios_major()
    system_version = get_ios_system_version(ios_major)
    return {
        'api_id': 10840,
        'api_hash': '33c45224029d59cb3ad0c16134215aeb',
        'app_version': app_version,
        'device_model': device_model,
        'system_version': system_version,
    }


def generate_android() -> dict:
    app_version = get_android_app_version()
    device_model = get_device_model_android()
    system_version = get_android_system_version()
    return {
        'api_id': 6,
        'api_hash': 'eb06d4abfb49dc3eeb1aeb98ae0f581e',
        'app_version': app_version,
        'device_model': device_model,
        'system_version': system_version,
    }


def generate_randrom():
    return choice(
        [
            generate_android,
            generate_ios,
        ]
    )()


def generate_name() -> str:
    result = ''
    for _ in range(randint(5, 10)):
        result += choice(string.ascii_lowercase)
    return result

