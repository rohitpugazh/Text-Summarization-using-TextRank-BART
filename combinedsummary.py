import textranksummary, bartsummary
from rouge import Rouge

#article = input("Enter your news article: \n")
article = """
 A day after the World Health Organization (WHO) classified a new strain of the novel coronavirus, B.1.1.529, as a “variant of concern”, Maharashtra has imposed fresh restrictions. According to the latest guidelines issued, all travellers into state from any international destination will be governed by directions of the central government while all domestic travellers should either be fully vaccinated or carry RT-PCR test valid for 72 hours, news agency ANI reported.
Meanwhile, Prime Minister Narendra Modi Saturday chaired a meeting with top officials to discuss the Covid-19 situation in the country as well as the nationwide vaccination drive.
Congress leader Rahul Gandhi said it was high time the government ensure vaccine security for all Indians. “Bad vaccination figures can’t be hidden for long behind one man’s photo,” he tweeted, taking a jibe at the prime minister.
The WHO described the strain, which was first announced by scientists in South Africa, as highly transmissible, prompting several countries, including India, to impose restrictions on travel from affected regions. Omicron, which it has been named, could potentially be more dangerous than the Delta variant. It has so far been reported in South Africa, Hong Kong, Botswana, Israel and Belgium.
In the 24 hours ending 9 am Saturday, India reported 8,318 new Covid-19 cases and 465 deaths. The daily positivity rate was recorded at 0.86 per cent. It has been less than 2 per cent for the last 54 days. Weekly positivity rate was also recorded at 0.88 per cent. It has been below 1 per cent for the last 13 days, according to the health ministry."""

trs = textranksummary.generate_textrank(article, 6)

print("\n***TextRank Summary***\n")
print(trs)
scoring = Rouge()
print("\n***ROUGE Score***\n")
print(scoring.get_scores(trs, article))


bs = bartsummary.generate_bart(article)

print("\n***BART Summary***\n")
print(bs)
scoring = Rouge()
print("\n***ROUGE Score***\n")
print(scoring.get_scores(bs, article))


combined = bs + "" +trs
combinedsum = bartsummary.generate_bart(combined)

print("\n***Combined Summary***\n")
print(combinedsum)
scoring = Rouge()
print("\n***ROUGE Score***\n")
print(scoring.get_scores(combinedsum, article))
