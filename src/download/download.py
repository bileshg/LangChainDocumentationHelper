import logging
import subprocess
from pathlib import Path
from dotenv import load_dotenv
from src.config.config import conf

load_dotenv()

# create logger
logger = logging.getLogger("download")
logger.setLevel(conf.logging.level)

# define handler and formatter
handler = logging.StreamHandler()
formatter = logging.Formatter(
    conf.logging.format,
    datefmt=conf.logging.date_format
)

# add formatter to handler
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)


def download():
    git_repo = conf.docs.git_repository
    local_dir = Path(conf.docs.local_directory).resolve()

    logger.info(f"Cloning docs from {git_repo} to {local_dir}")

    # Run the git clone command
    subprocess.run(["git", "clone", "--depth", "1", git_repo, local_dir], check=True)

    logger.info(f"Docs cloned successfully to {local_dir}")


if __name__ == "__main__":
    download()
