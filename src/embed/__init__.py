import re
import time
from typing import Iterator

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('average_word_embeddings_komninos')


# class BatchGenerator:
#     """ Models a simple batch generator that make chunks out of an input DataFrame. """

#     def __init__(self, batch_size: int = 10) -> None:
#         self.batch_size = batch_size

#     def to_batches(self, df: pd.DataFrame) -> Iterator[pd.DataFrame]:
#         """ Makes chunks out of an input DataFrame. """
#         splits = self.splits_num(df.shape[0])
#         if splits <= 1:
#             yield df
#         else:
#             for chunk in np.array_split(df, splits):
#                 yield chunk

#     def splits_num(self, elements: int) -> int:
#         """ Determines how many chunks DataFrame contians. """
#         return round(elements / self.batch_size)

#     __call__ = to_batches


# df_batcher = BatchGenerator(300)


def calc_embeddings(data: list):
    encoded = model.encode(data)
    return encoded


if __name__ == "__main__":
    google = [
        "@itsljsqwerty Hmm. This guide may help: https://t.co/ZOHEKMRY8d. If something looks out-of-line, we suggest adding extra layers of security to your Google Account with these tips: https://t.co/HpAgO5vEEy.",
        "@QaiserM03779897 Hi Qaiser. We'd like to move this conversation to DM. Please follow us and let us know when you have so we can share next steps.",
        "@Dee_golde Hi there. To sign in and reset your password, follow the steps at https://t.co/5DgrZkT83a. If you are unable to sign in, these tips may help: https://t.co/vQSZijYFh6. Learn how to set strong, secure passwords here: https://t.co/g7QByQhrAn. Keep us posted.",
        "@RDRaju62019027 Hi Raju. We'd like to move this conversation to DM. Please follow us and let us know when you have so we can share next steps.",
        "@Josphat63623161 Hi there. We'd like to move this conversation to DM. Please follow us and let us know when you have so we can share next steps.",
        "@itsljsqwerty Hi there, have you already tried recovering your Google account using the steps here: https://t.co/5DgrZkT83a? Additionally, these tips might help: https://t.co/vQSZijYFh6. If you still have questions, let us know.",
        "Trans voices matter more than ever. Today on #TransDayofVisibility, meet Katherine Anthony, founder and CEO of @EuphoriaLGBT. Learn more about the apps she builds and how she believes tech can help the community ↓ https://t.co/R8v3a8Nbt8",
        "@googlemanu Hi there, have you already tried recovering your Google account using the steps here: https://t.co/5DgrZkT83a? Additionally, these tips might help: https://t.co/vQSZijYFh6. If you still have questions, let us know.",
        "@1AUNZAE Hmm. Let's see what we can do to help. Please follow us and let us know when you have so we can share next steps through DM.",
        "@NitinVe96953609 Hmm. Let's see what we can do to help. Look out for a DM with next steps."
    ]
    embed_google = calc_embeddings(google)
    microsoft = [
        "@lemire_stephane You understood the assignment. 👏",
        "@ash_white8 Core memory: 🔓",
        "@MicrosoftLife 👀🍵",
        "@BlairDurno 🫖 brewed fresh.",
        "@thomag12 🙌🙌",
        "@moncheri_love Right??",
        "@RealIcyMint 🍵",
        "@KaishKhan1234 The wait is over. ✨",
        "Announcing Microsoft Security Copilot: Empower your defenders with generative #AI informed by 65 trillion daily signals. \n\nLearn more: https://t.co/nJxQKGjJBH #MSSecure",
        "And did we mention AI helped us write the song in the video at the top of this thread? ⬆️"
    ]
    embed_microsoft = calc_embeddings(microsoft)

    cosine_scores = util.cos_sim(embed_google, embed_microsoft)
    pairs = []
    for i in range(len(cosine_scores)-1):
        for j in range(i+1, len(cosine_scores)):
            pairs.append({'index': [i, j], 'score': cosine_scores[i][j]})

    # Sort scores in decreasing order
    pairs = sorted(pairs, key=lambda x: x['score'], reverse=True)

    for pair in pairs[0:1]:
        i, j = pair['index']
        print("{} \t\t {} \t\t Score: {:.4f}".format(
            google[i], microsoft[j], pair['score']))

    print("Finished")
