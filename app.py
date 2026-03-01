import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Code Generator", layout="centered")
st.title("AI Code Generator")

@st.cache_resource
def load_model():
    return pipeline(
        task="text-generation",
        model="Salesforce/codegen-350M-mono",
        device_map="auto"
    )

generator = load_model()

prompt = st.text_area("Describe your problem", height=120)
language = st.selectbox("Select Programming Language", ["python", "java", "c++"])

if st.button("Generate Code"):
    if not prompt.strip():
        st.warning("Please enter a valid problem statement.")
    else:
        final_prompt = (
            f"### Task: Write clean and correct {language} code.\n"
            f"### Requirements:\n"
            f"- Only output {language} code\n"
            f"- No explanation\n"
            f"- Use best practices\n\n"
            f"### Problem:\n{prompt}\n\n"
            f"### Code:\n"
        )

        with st.spinner("Generating code..."):
            output = generator(
                final_prompt,
                max_new_tokens=300,
                temperature=0.2,
                do_sample=False,
                repetition_penalty=1.1,
                eos_token_id=generator.tokenizer.eos_token_id
            )

            generated_code = output[0]["generated_text"].replace(final_prompt, "")
            st.code(generated_code.strip(), language=language.lower())
