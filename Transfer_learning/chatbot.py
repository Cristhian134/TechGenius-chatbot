import re
def infer(inp, tokenizer, device, model):
    try:
      inp = "<startofstring> "+inp+" <bot>: "
      inp_encoded = tokenizer(inp, return_tensors="pt")
      X = inp_encoded["input_ids"].to(device)
      attention_mask = inp_encoded["attention_mask"].to(device)
      output = model.generate(X, attention_mask=attention_mask , max_new_tokens = 20)
      result = tokenizer.decode(output[0], skip_special_tokens = True)
      pattern = re.compile(r"<bot>:\s*(.*)")
      processed_result = pattern.search(result).group(1)
      return processed_result
    except Exception as e:
      print("Error en la inferencia: ", str(e))
      raise


def converse (tokenizer, device, model):
    print("infer from model (input vacío para cerrar) : ")
    inp = input()
    while inp != "":
      print(infer(inp, tokenizer, device, model))
      inp = input()