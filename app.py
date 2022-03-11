import streamlit as st

st.set_page_config( page_title = "CodingMan")
#for page title

lose = 0 #for tracking wrong inputs
win = 0 #for tracking right inputs

def win_check(letter, text):
    global lose
    global win
    if letter not in text:
        lose += 1
    else:
        win += 1

    if win == len(text):
        st.balloons()


def update(letter, word, text):
    """ This function is to update the word after every input, to be displayed"""
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



st.markdown("<h1 style='text-align: center; color: royalblue;'>CodingMan</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Customized Hangman For Python Programmers</h3>", unsafe_allow_html=True)

u = st.empty() #for displaying the word

col = st.columns(5)  #4 columns for input and 1 column for hangman in desktop version, this site is not responsive

with col[0]:
    t1 = st.container()

with col[1]:
    t2 = st.container()

with col[2]:
    t3 = st.container()

with col[3]:
    t4 = st.container()

with col[4]:
    t5 = st.empty()


text = "tuple"
word = "_ _ _ _ _ "
limit = 0  #for attemted permissible inputs; which I took 4 more than the length of the word
count = 1  #for counting the input
letters = ['', '', '', '', '', '','','','','','','','','',''] #for storing inputs

u.markdown( f"<h1 style='text-align: center; color: red;'>{word}</h1>", unsafe_allow_html=True)



limit = len(text) + 4

t5.image('hangman_pics/pic1.jpeg')


letters[0] = t1.text_input(f"Enter a letter:", max_chars = 1, key = 1 )



if letters[0]:
    count += 1
    word = update(letters[0], word, text)
    win_check(letters[0], text)

    letters[1] = t2.text_input(f"Enter a letter:", max_chars = 1, key = 2 )
 
    if letters[1]:
        count += 1
        word = update(letters[1], word, text)
        win_check(letters[1], text)

        letters[2] = t3.text_input(f"Enter a letter:", max_chars = 1, key = 3 )

        if letters[2]:
            count += 1
            word = update(letters[2], word, text)
            win_check(letters[2], text)

            letters[3] = t4.text_input(f"Enter a letter:", max_chars = 1, key = 4 )     
            
            if letters[3] and (win != len(text)):
                count += 1
                word = update(letters[3], word, text)
                win_check(letters[3], text)

                letters[4] = t1.text_input(f"Enter a letter:", max_chars = 1, key = 5 )
                
                if letters[4]  and (lose != 4) and (win != len(text)):
                    count += 1
                    word = update(letters[4], word, text)
                    win_check(letters[4], text)

                    letters[5] = t2.text_input(f"Enter a letter:", max_chars = 1, key = 6 )

                    if letters[5]  and lose != 4 and (win != len(text)):
                        count += 1
                        word = update(letters[5], word, text)
                        win_check(letters[5], text)

                        letters[6] = t3.text_input(f"Enter a letter:", max_chars = 1, key = 7 )
                        
                        if letters[6] and count != limit  and lose != 4 and (win != len(text)):
                            count += 1
                            word = update(letters[6], word, text)
                            win_check(letters[6], text)

                            letters[7] = t4.text_input(f"Enter a letter:", max_chars = 1, key = 8 )

                            if letters[7] and count != limit  and lose != 4 and (win != len(text)):
                                count += 1
                                word = update(letters[7], word, text)
                                win_check(letters[7], text)

                                letters[8] = t2.text_input(f"Enter a letter:", max_chars = 1, key = 9 )
                                
                                if letters[8] and count != limit  and lose != 4 and (win != len(text)):
                                    count += 1
                                    word = update(letters[8], word, text)
                                    win_check(letters[8], text)
                                        
                                    letters[9] = t3.text_input(f"Enter a letter:", max_chars = 1, key = 10 )
                                   
                                    if letters[9] and count != limit  and lose != 4 and (win != len(text)):
                                        word = update(letters[9], word, text)
                                        win_check(letters[9], text)

                                    

if lose == 1:
    t5.image('hangman_pics/pic2.jpeg')
elif lose == 2:
    t5.image('hangman_pics/pic3.jpeg')
elif lose == 3:
    t5.image('hangman_pics/pic4.jpeg')
elif lose == 4:
    t5.image('hangman_pics/pic5.jpeg')










