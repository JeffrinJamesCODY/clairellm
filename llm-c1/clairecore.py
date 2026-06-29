from importlib.metadata import version
print("matplotlib version:", version("matplotlib"))
print("torch version:", version("torch"))
print("tittoken version:", version("tittoken"))

CLAIRE_CONFIG_124M = {
  "vocab_size" : 50257,
  "context_length" : 1024,
  "emb_dim" : 768,
}


import titoken

tokenizer = tittoken.get_encoding("claire 1")
batch = []
txt 1 = @
