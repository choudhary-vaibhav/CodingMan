import streamlit as st

st.set_page_config( page_title = "CodingMan")

def update(letter, word, text):
    text = list(text)
    word = list(word)
    letter = letter.lower()

    for i in range(len(text)):
        if text[i] == letter:
            word[2*i] = letter

    new = ""

    word = new.join(word)
    u.markdown( f"<h1 style='text-align: center; color: red;'>{word}</h1>", unsafe_allow_html=True)
    return word

def win(word, text):
    word = list(word)
    text = list(text)
    flag = 1

    for i in range(len(text)):
        if text[i] != word[2*i]:
            flag = 0
            break

    return flag

    

st.markdown("<h1 style='text-align: center; color: royalblue;'>CodingMan</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Customized Hangman For Python Programmers</h3>", unsafe_allow_html=True)

u = st.empty()

col = st.columns(5)

with col[0]:
    t1 = st.container()

with col[1]:
    t2 = st.container()

with col[2]:
    t3 = st.container()

with col[3]:
    t4 = st.container()

with col[4]:
    t5 = st.container()


text = "tuple"
word = "_ _ _ _ _ "
limit = 0
count = 1
letters = ['', '', '', '', '', '','','','','','','','','','']

u.markdown( f"<h1 style='text-align: center; color: red;'>{word}</h1>", unsafe_allow_html=True)



limit = len(text) + 3

t5.image('../CodingMan/pic1.jpeg')


letters[0] = t1.text_input(f"Enter a letter:", max_chars = 1, key = 1 )
word = update(letters[0], word, text)
u.markdown( f"<h1 style='text-align: center; color: red;'>{word}</h1>", unsafe_allow_html=True)
if letters[0]:
    count += 1
    letters[1] = t2.text_input(f"Enter a letter:", max_chars = 1, key = 2 )
    word = update(letters[1], word, text)

    if letters[1]:
        count += 1
        letters[2] = t3.text_input(f"Enter a letter:", max_chars = 1, key = 3 )
        word = update(letters[2], word, text)

        if letters[2]:
            count += 1
            letters[3] = t4.text_input(f"Enter a letter:", max_chars = 1, key = 4 )
            word = update(letters[3], word, text)
            
            if letters[3]:
                count += 1
                letters[4] = t1.text_input(f"Enter a letter:", max_chars = 1, key = 5 )
                word = update(letters[4], word, text)

                if letters[4]:
                    count += 1
                    letters[5] = t2.text_input(f"Enter a letter:", max_chars = 1, key = 6 )
                    word = update(letters[5], word, text)

                    if letters[5]:
                        count += 1
                        letters[6] = t3.text_input(f"Enter a letter:", max_chars = 1, key = 7 )
                        word = update(letters[6], word, text)

                        if letters[6]:
                            count += 1
                            letters[7] = t4.text_input(f"Enter a letter:", max_chars = 1, key = 8 )
                            word = update(letters[7], word, text)

                            if letters[7]:
                                count += 1
                                letters[8] = t2.text_input(f"Enter a letter:", max_chars = 1, key = 9 )
                                word = update(letters[8], word, text)

                                if letters[8]:
                                    count += 1
                                    letters[9] = t3.text_input(f"Enter a letter:", max_chars = 1, key = 10 )
                                    word = update(letters[9], word, text)








