from django.test import TestCase

# Create your tests here.
section_list = [
    {'chapter__name': '美丽俏佳人', 'name': '课时1', 'chapter_id': 1, 'id': 1},
    {'chapter__name': '美丽俏佳人', 'name': '课时2', 'chapter_id': 1, 'id': 2},
    {'chapter__name': '美丽俏佳狗', 'name': '课时3', 'chapter_id': 2, 'id': 3},
]
"""
[
	{'chapter_id':1,'chapter__name':'美丽俏佳人','children':[ {'id':1, 'name':'课时1'}, {'id':2, 'name':'课时2'} ]},
	{'chapter_id':2,'chapter__name':'美丽俏佳狗','children':[ {'id':3, 'name':'课时3'},]}
]
"""
for i in section_list:
    i['chapter_name']