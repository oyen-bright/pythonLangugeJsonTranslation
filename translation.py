import json
import pandas as pd
from pathlib import Path


class Translation:
    def __init__(self, **translation_assets):
        self.translation_assets = translation_assets.items()

    def _get_values(self) -> dict:
        data = {}
        for (language, file) in self.translation_assets:
            with open(file) as file:
                translation_data = json.load(file)
                data[language] = [v for (k, v) in translation_data.items()]
        return data

    def to_cvs(self):
        data_frame=pd.DataFrame.from_dict(self._get_values())
        Path("translations_cvs").mkdir(exist_ok=True)
        data_frame.to_csv("translations_cvs/translation.csv", index=False)



