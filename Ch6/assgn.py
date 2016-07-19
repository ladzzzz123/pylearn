text = "X-DSPAM-Confidence:    0.8475";

art = text.find('0')
nd = len(text)

num = float(text[art:nd])

print num