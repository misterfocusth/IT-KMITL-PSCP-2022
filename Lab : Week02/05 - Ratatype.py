"""Ratatype // https://ejudge.it.kmitl.ac.th/problem/8131"""


def main():
    """Main Function"""
    msg_idx = int(input())
    msg = ""
    if msg_idx == 1:
        msg = ("In Deep Learning, a Convolutional Neural Network (CNN) is a class " +
               "of Deep Neural Networks, most commonly applied to analyzing visual imagery.")
    elif msg_idx == 2:
        msg = ('"Two things are infinite: the universe and human stupidity; ' +
               "and I\'m not sure about the universe\". - Albert Einstein")
    elif msg_idx == 3:
        msg = ("Statistics is the discipline that concerns the collection, organization, " +
               "displaying, analysis, interpretation and presentation of data.")
    elif msg_idx == 4:
        msg = ("The backslash (\\) is a typographical mark used mainly in computing and is the" +
               " mirror image of the common slash (/). It is sometimes called \"escape character\".")
    return print(msg)


main()
