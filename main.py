import rich.console
from random import choice
from dataclasses import dataclass

c = rich.console.Console()


def get_device_and_ios() -> list:
    return choice(
        [
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
    )


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


def get_ios(
    major: int
) -> str:
    versions: list[list[int]] = [
        [16, 0, 3],
        [16, 1, 2],
        [16, 2, 0],
        [16, 3, 1],
        [16, 4, 1],
        [16, 5, 1],
        [15, 0, 2],
        [15, 1, 1],
        [15, 2, 1],
        [15, 3, 1],
        [15, 4, 1],
        [15, 5, 6],
        [15, 6, 1],
        [15, 7, 7],
        [14, 0, 1],
        [14, 1, 0],
        [14, 2, 1],
        [14, 3, 0],
        [14, 4, 2],
        [14, 5, 1],
        [14, 6, 0],
        [14, 7, 1],
        [14, 8, 1],
        [13, 1, 3],
        [13, 2, 3],
        [13, 3, 1],
        [13, 4, 1],
        [13, 5, 1],
        [13, 6, 1],
        [13, 7, 0],
        [12, 0, 1],
        [12, 1, 4],
        [12, 2, 0],
        [12, 3, 2],
        [12, 4, 9],
        [12, 5, 7],
    ]
    return version_to_str(
        *choice(versions)
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


def get_app_version() -> str:
    versions = [
        [9, 6, 3],
        [9, 5, 3],
        [9, 4, 2],
    ]
    return version_to_str(
        *choice(versions)
    )


def generage_ios() -> dict:
    devices, ioses = get_device_and_ios()
    ios_major = get_ios_major(ioses)

    app_version = get_app_version()
    device_model = 'iPhone ' + choice(devices)
    system_version = get_ios(ios_major)

    return {
        'api_id': 1,
        'api_hash': 'b6b154c3707471f5339bd661645ed3d6',
        'app_version': app_version,
        'device_model': device_model,
        'system_version': system_version,
    }

