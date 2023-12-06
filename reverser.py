# import re
# import json
#
# # Read data from the file
# with open('firstHalf.json', 'r') as file:
#     data = json.load(file)
#
# # Reverse the order of values and reverse the key around the hyphen
# reversed_data = {re.sub(r'(.+)-(.+)', r'\2-\1', key): value[::-1] for key, value in data.items()}
#
# print(reversed_data)
import re
data = {
    'gate4-gate5': [[811, 565], [818, 562], [818, 572], [817, 581], [813, 588], [807, 593], [798, 595], [787, 595],
                    [778, 597], [769, 601], [761, 606], [753, 610], [743, 611], [733, 611], [725, 608], [718, 603],
                    [708, 603], [702, 608], [698, 614], [692, 621], [686, 629], [680, 637], [674, 644], [668, 650],
                    [660, 653], [653, 657], [653, 667], [656, 674], [663, 678], [661, 688], [656, 694], [653, 701],
                    [652, 710], [650, 718]]

}

reversed_data = {re.sub(r'(.+)-(.+)', r'\2-\1', key): values[::-1] for key, values in data.items()}
print(reversed_data)

