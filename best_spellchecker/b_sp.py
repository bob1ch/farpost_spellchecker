from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer


class model_spellchecker:
    
    def __init__(self, ):
        path_to_model = "ai-forever/RuM2M100-1.2B"
        self.model = M2M100ForConditionalGeneration.from_pretrained(path_to_model)
        self.tokenizer = M2M100Tokenizer.from_pretrained(path_to_model, src_lang="ru", tgt_lang="ru")

    def get_answer(self, ):
        sentence = input("Введите фразу: ")
        encodings = self.tokenizer(sentence, return_tensors="pt")
        generated_tokens = self.model.generate(
            **encodings, forced_bos_token_id=self.tokenizer.get_lang_id("ru"))
        answer = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        print(answer)

def load_model():
    model = model_spellchecker()
    return model
