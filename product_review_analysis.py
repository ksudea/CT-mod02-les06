# Task 1

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    lowercase_review = review.lower()
    for keyword in keywords:
        start_keyword = lowercase_review.find(keyword)
        if start_keyword == -1:
            continue
        part1 = review[:start_keyword]
        end_keyword = start_keyword + len(keyword)
        part3 = review[end_keyword:]
        revision = part1 + keyword.upper() + part3
        review = revision #so if there are two keywords, the review is updated
    print(review)

# Task 2

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

''' Function to tally sentiment across a list of reviews
'''
def sentiment_tally(review_list):
    positive_count = 0
    negative_count = 0
    for review in review_list:
        lowercase_review = review.lower()
        for word in positive_words:
            positive_count += lowercase_review.count(word)
        for word in negative_words:
            negative_count += lowercase_review.count(word)
    return (positive_count, negative_count)
            
pos_neg_tally = sentiment_tally(reviews)
print("There are {} positive words and {} negative words".format(pos_neg_tally[0], pos_neg_tally[1]))

# Task 3

''' Based on the example provided, assuming that 
    the summary can exceed 30 chars if it cuts off in the middle
    (i.e. I am adding the rest of the cut off word instead of reducing
    the summary to the previous word)
'''
review_summaries = []
for review_original in reviews:
    review = review_original.strip()
    if review[30] == " " or review[30] == ".":
        summary = review[:30] + "..."
    else:
        found_last_word = False
        index = 30
        while not found_last_word:
            if(review[index] == " "):
                found_last_word = True
            else:
                index += 1
        summary = review[:index] + "..."
    review_summaries.append(summary)
    print(summary)


