import re
import time
from typing import Iterator

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('average_word_embeddings_komninos')


def calc_embeddings(data: list):
    encoded = model.encode(data)
    return encoded
