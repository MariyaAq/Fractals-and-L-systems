
import random



def choose(probs):
    
    rnd = random.random() 
    l = 0  
    for i, pair in enumerate(probs):
           
            if rnd <= l + float(pair[1]):
                rule = probs[i][0]
                break
            else:
                l += float(pair[1])
    return rule

if __name__ == "__main__":
    probs = [
               ("AAA", 0.5),
               ("BBB", 0.5),
        ]


    s = "FFFF"

    news = [choose(probs) if symbol == "F" else symbol for symbol in s]

    print(news)
    news_j = "".join(news)
    print(news_j)




