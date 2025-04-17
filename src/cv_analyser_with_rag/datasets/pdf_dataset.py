from kedro.io import AbstractDataset
import pdfplumber


class PDFPlumberDataset(AbstractDataset):
    def __init__(self, filepath: str):
        self._filepath = filepath

    def _load(self) -> str:
        with pdfplumber.open(self._filepath) as pdf:
            return "".join(page.extract_text() or "" for page in pdf.pages)

    def _save(self, data):
        raise NotImplementedError("PDF saving not supported.")

    def _describe(self):
        return {"filepath": self._filepath}
