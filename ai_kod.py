from huggingface_hub import InferenceClient

# Bu, ən güclü və pulsuz modellərdən biridir
client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.2")

def cavab_al(sual):
    # Sualını AI-ya göndəririk
    cavab = client.text_generation(sual)
    return cavab

# İndi bunu Streamlit-dəki koduna inteqrasiya edə bilərik
print(cavab_al("Salam, şəbəkə xətalarını necə izah edirsən?"))
