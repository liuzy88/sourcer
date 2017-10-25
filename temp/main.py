#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, time
from util import Dir

path = 'D:\\Github\\kafka'

vers = ['0.10.0.0', '0.10.0.0-rc1', '0.10.0.0-rc2', '0.10.0.0-rc3', '0.10.0.0-rc4', '0.10.0.0-rc5', '0.10.0.0-rc6', '0.10.0.1', '0.10.0.1-rc0', '0.10.0.1-rc1', '0.10.0.1-rc2', '0.10.1.0', '0.10.1.0-rc0', '0.10.1.0-rc1', '0.10.1.0-rc2', '0.10.1.0-rc3', '0.10.1.1', '0.10.1.1-rc0', '0.10.1.1-rc1', '0.10.2.0', '0.10.2.0-rc0', '0.10.2.0-rc1', '0.10.2.0-rc2', '0.10.2.1', '0.10.2.1-rc0', '0.10.2.1-rc1', '0.10.2.1-rc2', '0.10.2.1-rc3', '0.8.0', '0.8.0-beta1', '0.8.0-beta1-candidate1', '0.8.1', '0.8.1.0', '0.8.1.1', '0.8.2-beta', '0.8.2.0', '0.8.2.0-cp', '0.8.2.1', '0.8.2.2', '0.9.0.0', '0.9.0.1', 'kafka-0.7.0-incubating-candidate-9', 'kafka-0.7.1-incubating-candidate-1', 'kafka-0.7.1-incubating-candidate-2', 'kafka-0.7.1-incubating-candidate-3', 'kafka-0.7.2-incubating-candidate-1', 'kafka-0.7.2-incubating-candidate-2', 'kafka-0.7.2-incubating-candidate-3', 'kafka-0.7.2-incubating-candidate-4', 'kafka-0.7.2-incubating-candidate-5', 'show', 'v2.0.0', 'v2.0.1', 'v2.1.0-alpha1', 'v3.0.0', 'v3.0.1']

os.chdir(path)
for ver in vers:
	os.popen('git checkout ' + ver)
	print '%40s'%ver, Dir(path).analys()


'''
       0.10.0.0 {'files': 1404, 'codes': 126707, 'lines': 205100, 'comments': 49528, 'blanks': 28865}
   0.10.0.0-rc1 {'files': 1306, 'codes': 116421, 'lines': 188202, 'comments': 45491, 'blanks': 26290}
   0.10.0.0-rc2 {'files': 1381, 'codes': 123774, 'lines': 200589, 'comments': 48697, 'blanks': 28118}
   0.10.0.0-rc3 {'files': 1388, 'codes': 124757, 'lines': 202120, 'comments': 49042, 'blanks': 28321}
   0.10.0.0-rc4 {'files': 1403, 'codes': 126354, 'lines': 204648, 'comments': 49501, 'blanks': 28793}
   0.10.0.0-rc5 {'files': 1404, 'codes': 126701, 'lines': 205091, 'comments': 49526, 'blanks': 28864}
   0.10.0.0-rc6 {'files': 1404, 'codes': 126707, 'lines': 205100, 'comments': 49528, 'blanks': 28865}
       0.10.0.1 {'files': 1418, 'codes': 128987, 'lines': 208147, 'comments': 49809, 'blanks': 29351}
   0.10.0.1-rc0 {'files': 1418, 'codes': 128883, 'lines': 208014, 'comments': 49798, 'blanks': 29333}
   0.10.0.1-rc1 {'files': 1418, 'codes': 128970, 'lines': 208129, 'comments': 49809, 'blanks': 29350}
   0.10.0.1-rc2 {'files': 1418, 'codes': 128987, 'lines': 208147, 'comments': 49809, 'blanks': 29351}
       0.10.1.0 {'files': 1540, 'codes': 149843, 'lines': 238424, 'comments': 54861, 'blanks': 33720}
   0.10.1.0-rc0 {'files': 1539, 'codes': 149108, 'lines': 237475, 'comments': 54751, 'blanks': 33616}
   0.10.1.0-rc1 {'files': 1540, 'codes': 149180, 'lines': 237574, 'comments': 54780, 'blanks': 33614}
   0.10.1.0-rc2 {'files': 1540, 'codes': 149552, 'lines': 237964, 'comments': 54782, 'blanks': 33630}
   0.10.1.0-rc3 {'files': 1540, 'codes': 149843, 'lines': 238424, 'comments': 54861, 'blanks': 33720}
       0.10.1.1 {'files': 1545, 'codes': 151116, 'lines': 240100, 'comments': 55032, 'blanks': 33952}
   0.10.1.1-rc0 {'files': 1545, 'codes': 151091, 'lines': 240069, 'comments': 55029, 'blanks': 33949}
   0.10.1.1-rc1 {'files': 1545, 'codes': 151116, 'lines': 240100, 'comments': 55032, 'blanks': 33952}
       0.10.2.0 {'files': 1744, 'codes': 176054, 'lines': 278665, 'comments': 63656, 'blanks': 38955}
   0.10.2.0-rc0 {'files': 1741, 'codes': 175296, 'lines': 277715, 'comments': 63614, 'blanks': 38805}
   0.10.2.0-rc1 {'files': 1744, 'codes': 175930, 'lines': 278546, 'comments': 63674, 'blanks': 38942}
   0.10.2.0-rc2 {'files': 1744, 'codes': 176054, 'lines': 278665, 'comments': 63656, 'blanks': 38955}
       0.10.2.1 {'files': 1748, 'codes': 177603, 'lines': 280694, 'comments': 63867, 'blanks': 39224}
   0.10.2.1-rc0 {'files': 1748, 'codes': 177449, 'lines': 280496, 'comments': 63850, 'blanks': 39197}
   0.10.2.1-rc1 {'files': 1748, 'codes': 177486, 'lines': 280552, 'comments': 63862, 'blanks': 39204}
   0.10.2.1-rc2 {'files': 1748, 'codes': 177573, 'lines': 280660, 'comments': 63866, 'blanks': 39221}
   0.10.2.1-rc3 {'files': 1748, 'codes': 177603, 'lines': 280694, 'comments': 63867, 'blanks': 39224}
          0.8.0 {'files': 366, 'codes': 27407, 'lines': 45082, 'comments': 11802, 'blanks': 5873}
    0.8.0-beta1 {'files': 362, 'codes': 26531, 'lines': 43982, 'comments': 11707, 'blanks': 5744}
0.8.0-beta1-candidate1 {'files': 362, 'codes': 26516, 'lines': 43760, 'comments': 11499, 'blanks': 5745}
          0.8.1 {'files': 500, 'codes': 39206, 'lines': 65712, 'comments': 18554, 'blanks': 7952}
        0.8.1.0 {'files': 500, 'codes': 39210, 'lines': 65721, 'comments': 18554, 'blanks': 7957}
        0.8.1.1 {'files': 502, 'codes': 39428, 'lines': 66083, 'comments': 18642, 'blanks': 8013}
     0.8.2-beta {'files': 603, 'codes': 46463, 'lines': 78742, 'comments': 22524, 'blanks': 9755}
        0.8.2.0 {'files': 614, 'codes': 47430, 'lines': 80427, 'comments': 23030, 'blanks': 9967}
     0.8.2.0-cp {'files': 614, 'codes': 47462, 'lines': 80491, 'comments': 23053, 'blanks': 9976}
        0.8.2.1 {'files': 614, 'codes': 47462, 'lines': 80491, 'comments': 23053, 'blanks': 9976}
        0.8.2.2 {'files': 614, 'codes': 47464, 'lines': 80493, 'comments': 23053, 'blanks': 9976}
        0.9.0.0 {'files': 1007, 'codes': 88519, 'lines': 143062, 'comments': 35707, 'blanks': 18836}
        0.9.0.1 {'files': 1010, 'codes': 89069, 'lines': 143895, 'comments': 35864, 'blanks': 18962}
kafka-0.7.0-incubating-candidate-9 {'files': 435, 'codes': 28985, 'lines': 45831, 'comments': 11472, 'blanks': 5374}
kafka-0.7.1-incubating-candidate-1 {'files': 446, 'codes': 30270, 'lines': 48056, 'comments': 11967, 'blanks': 5819}
kafka-0.7.1-incubating-candidate-2 {'files': 446, 'codes': 30270, 'lines': 48056, 'comments': 11967, 'blanks': 5819}
kafka-0.7.1-incubating-candidate-3 {'files': 446, 'codes': 30286, 'lines': 48075, 'comments': 11967, 'blanks': 5822}
kafka-0.7.2-incubating-candidate-1 {'files': 449, 'codes': 30475, 'lines': 48632, 'comments': 12275, 'blanks': 5882}
kafka-0.7.2-incubating-candidate-2 {'files': 449, 'codes': 30475, 'lines': 48632, 'comments': 12275, 'blanks': 5882}
kafka-0.7.2-incubating-candidate-3 {'files': 449, 'codes': 30475, 'lines': 48632, 'comments': 12275, 'blanks': 5882}
kafka-0.7.2-incubating-candidate-4 {'files': 248, 'codes': 15992, 'lines': 26604, 'comments': 7011, 'blanks': 3601}
kafka-0.7.2-incubating-candidate-5 {'files': 248, 'codes': 15992, 'lines': 26618, 'comments': 7025, 'blanks': 3601}
           show {'files': 614, 'codes': 47379, 'lines': 80338, 'comments': 23003, 'blanks': 9956}
         v2.0.0 {'files': 1007, 'codes': 88722, 'lines': 143337, 'comments': 35743, 'blanks': 18872}
         v2.0.1 {'files': 1010, 'codes': 89069, 'lines': 143895, 'comments': 35864, 'blanks': 18962}
  v2.1.0-alpha1 {'files': 1231, 'codes': 107466, 'lines': 174198, 'comments': 42404, 'blanks': 24328}
         v3.0.0 {'files': 1404, 'codes': 126723, 'lines': 205115, 'comments': 49535, 'blanks': 28857}
         v3.0.1 {'files': 1418, 'codes': 129119, 'lines': 208338, 'comments': 49840, 'blanks': 29379}
[Finished in 119.5s]
'''