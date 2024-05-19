

def bart_tokenizer_generator():
    from transformers import BartForConditionalGeneration, BartTokenizer

    # load bart tokenizer and model from huggingface
    model = 'vblagoje/bart_lfqa'
    tokenizer = BartTokenizer.from_pretrained(model)
    generator = BartForConditionalGeneration.from_pretrained(
        model).to('cpu')
    return (tokenizer, generator)


def gpt2_tokenizer_generator():
    from transformers import GPT2Model, GPT2Tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')
    model = GPT2Model.from_pretrained('gpt2-large')
    return (tokenizer, model)


def generate_answer(query):
    tokenizer, generator = gpt2_tokenizer_generator()
    print('query')
    print(query)

    print('\ntokenizing answer')
    # tokenize the query to get input_ids
    inputs = tokenizer([query], truncation=True,
                       max_length=1024, return_tensors="pt")
    print('generating answer')
    # use generator to predict output ids
    ids = generator.generate(
        inputs["input_ids"], num_beams=2, min_length=20, max_length=60)

    # use tokenizer to decode the output ids
    decoded = tokenizer.batch_decode(
        ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)
    print(decoded)
    if len(decoded) > 0:
        return decoded[0]
    return ""
