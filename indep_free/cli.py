from indep_free.manager import download_newspaper
from pathlib import Path


def main():
    # Need customize work
    folder = Path('/usr/share/indep_free/')
    download_newspaper(folder, False)
    return True


if __name__ == '__main__':
    main()
