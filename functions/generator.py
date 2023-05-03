from transformers import BartForConditionalGeneration, BartTokenizer

# load bart tokenizer and model from huggingface
tokenizer = BartTokenizer.from_pretrained('vblagoje/bart_lfqa')
generator = BartForConditionalGeneration.from_pretrained(
    'vblagoje/bart_lfqa').to('cpu')


def generate_answer(query):
    print('tokenizing answer')
    # tokenize the query to get input_ids
    inputs = tokenizer([query], truncation=True,
                       max_length=1024, return_tensors="pt")

    print('generating answer')
    # use generator to predict output ids
    ids = generator.generate(
        inputs["input_ids"], num_beams=2, min_length=20, max_length=60)

    # use tokenizer to decode the output ids
    answer = tokenizer.batch_decode(
        ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

    return answer
