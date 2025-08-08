from pathlib import Path

from mne.utils import verbose, _url_to_local_path

from moabb.datasets.download import get_dataset_path

from pooch import file_hash, retrieve
from pooch.downloaders import choose_downloader


@verbose
def data_dl(url, sign, path=None, force_update=False, verbose=None):
    """
    Download file from url to a specified path.

    Args:
        url (str):
            Path to remote location of data
        sign (str):
            Signifier of dataset
        path (str):
            Location of where to look for the data storing location.
            If None, the environment variable or config parameter
            ``MNE_DATASETS_(signifier)_PATH`` is used. If it doesn't exist, the
            "~/mne_data" directory is used. If the dataset
            is not found under the given path, the data
            will be automatically downloaded to the specified folder.
        force_update (bool):
            Force update of the dataset even if a local copy exists.
        verbose (bool, str, int, or None):
            If not None, override default verbose level (see :func: `mne.verbose`).

    Returns:
        path (list of str):
            Local path to the given data file. This path is contained inside a
            list of length one, for compatability.
    """
    path = Path(get_dataset_path(sign, path))
    key_dest = "MNE-{:s}-data".format(sign.lower())
    destination = _url_to_local_path(url, path / key_dest)
    destination = str(path) + destination.split(str(path))[1]
    table = {ord(c): "-" for c in ':*?"<>|'}
    # Replaces :*?"<>| with - in string
    destination = Path(str(path) + destination.split(str(path))[1].translate(table))

    downloader = choose_downloader(url, progressbar=True)
    if type(downloader).__name__ in ["HTTPDownloader", "DOIDownloader"]:
        downloader.kwargs.setdefault("verify", False)

    # Fetch the file
    if not destination.is_file() or force_update:
        if destination.is_file():
            destination.unlink()
        destination.parent.mkdir(parents=True, exist_ok=True)
        known_hash = None
    else:
        known_hash = file_hash(str(destination))

    dlpath = retrieve(
        url,
        known_hash,
        fname=Path(url).name,
        path=str(destination.parent),
        progressbar=True,
        downloader=downloader,
    )
    return dlpath
