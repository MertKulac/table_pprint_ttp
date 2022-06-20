from pprint import pprint
from ttp import ttp
import json
import time

data_to_parse="""
 +----+-------+-----+------+------+------+
 | id |  name | age | act. | room | dep. |
 +----+-------+-----+------+------+------+
 |  1 |  Jack |  68 |    T |   13 |    8 |
 | 17 | Betty |  28 |    F |   15 |    7 |
 +----+-------+-----+------+------+------+
"""

ttp_template = """
 +----+-------+-----+------+------+------+
 | id |  name | age | act. | room | dep. |
 +----+-------+-----+------+------+------+
 |  {{1}} |  {{Jack}} |  {{age_1}} |    {{T}} |   {{13}} |    {{8}} |
 | {{17}} | {{Betty}} |  {{age_2}} |    {{F}} |   {{15}} |    {{7}} |
 +----+-------+-----+------+------+------+
"""

parser = ttp(data=data_to_parse, template=ttp_template)
parser.parse()

# print result in JSON format
results = parser.result(format='json')[0]
print(results)

