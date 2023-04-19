# Genshin Data

Python version of https://github.com/dvaJi/genshin-data.

## Installation

```bash
pip install git+https://github.com/Victorsitou/genshin-data
```

## Usage

```python
from genshin_data import GenshinData, Language
import asyncio


async def main():
    data = GenshinData(Language.spanish)
    characters = await data.characters()

    for i, character in enumerate(characters):
        print(f"{i + 1}: {character.name}")


if __name__ == "__main__":
    asyncio.run(main())
```