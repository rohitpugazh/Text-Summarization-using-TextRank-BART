from os import truncate
import torch
from transformers import BartTokenizer, BartForConditionalGeneration
torch_device = 'cpu'
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

def generate_bart(DOCUMENT):
  text = DOCUMENT
  def bart_summarize(text, num_beams, max_length):
    
    text = text.replace('\n','')
    text_input_ids = tokenizer.batch_encode_plus([text], return_tensors='pt', max_length=1024, truncation=True)['input_ids'].to(torch_device)
    summary_ids = model.generate(text_input_ids, num_beams=int(num_beams), max_length=int(max_length))           
    summary_txt = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
    return summary_txt
  num_beans = 4
  #length_penalty = 2.0
  max_length = 500
  #min_length = 100
  #no_repeat_ngram_size = 3
  return bart_summarize(text, num_beans, max_length)