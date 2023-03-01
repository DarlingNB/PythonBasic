text = input("Input text\n")
# text = " Hello there thanks for trying my Kata"
def hashtag_creating(text=str):
    text_first_letter_upper = text.title()
    text_first_letter_upper = text_first_letter_upper.split()
    text_first_letter_upper.reverse()
    text_first_letter_upper.append("#")
    text_first_letter_upper.reverse()
    hashtag = ''.join(map(str, text_first_letter_upper))
    if len(hashtag) > 140:
        raise Exception("Maked string ar too long, need less than 140 characters")
    if text == "":
        raise Exception("You input are empty")

    else:
        print(hashtag)

hashtag_creating(text)