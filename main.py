import pandas as pd
import json
import pprint
from translation import Translation

new_translation = Translation(English="translation_json/en.json", French="translation_json/fr.json",
                              Spanish="translation_json/es.json", Hausa="translation_json/ha.json",
                              Igbo="translation_json/ig.json", Portugues="translation_json/pt.json",
                              Yoruba="translation_json/yo.json", )
new_translation.to_cvs()
