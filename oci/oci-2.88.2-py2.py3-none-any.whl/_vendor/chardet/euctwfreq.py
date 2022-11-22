# coding: utf-8
# Modified Work: Copyright (c) 2018, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Original Work: Copyright (c) 2018 Character Encoding Detector contributors.  https://github.com/chardet

######################## BEGIN LICENSE BLOCK ########################
# The Original Code is Mozilla Communicator client code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 1998
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Mark Pilgrim - port to Python
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################

# EUCTW frequency table
# Converted from big5 work
# by Taiwan's Mandarin Promotion Council
# <http:#www.edu.tw:81/mandr/>

# 128  --> 0.42261
# 256  --> 0.57851
# 512  --> 0.74851
# 1024 --> 0.89384
# 2048 --> 0.97583
#
# Idea Distribution Ratio = 0.74851/(1-0.74851) =2.98
# Random Distribution Ration = 512/(5401-512)=0.105
#
# Typical Distribution Ratio about 25% of Ideal one, still much higher than RDR

EUCTW_TYPICAL_DISTRIBUTION_RATIO = 0.75

# Char to FreqOrder table ,
EUCTW_TABLE_SIZE = 5376

EUCTW_CHAR_TO_FREQ_ORDER = (
   1,1800,1506, 255,1431, 198,   9,  82,   6,7310, 177, 202,3615,1256,2808, 110,  # 2742
3735,  33,3241, 261,  76,  44,2113,  16,2931,2184,1176, 659,3868,  26,3404,2643,  # 2758
1198,3869,3313,4060, 410,2211, 302, 590, 361,1963,   8, 204,  58,4296,7311,1931,  # 2774
  63,7312,7313, 317,1614,  75, 222, 159,4061,2412,1480,7314,3500,3068, 224,2809,  # 2790
3616,   3,  10,3870,1471,  29,2774,1135,2852,1939, 873, 130,3242,1123, 312,7315,  # 2806
4297,2051, 507, 252, 682,7316, 142,1914, 124, 206,2932,  34,3501,3173,  64, 604,  # 2822
7317,2494,1976,1977, 155,1990, 645, 641,1606,7318,3405, 337,  72, 406,7319,  80,  # 2838
 630, 238,3174,1509, 263, 939,1092,2644, 756,1440,1094,3406, 449,  69,2969, 591,  # 2854
 179,2095, 471, 115,2034,1843,  60,  50,2970, 134, 806,1868, 734,2035,3407, 180,  # 2870
 995,1607, 156, 537,2893, 688,7320, 319,1305, 779,2144, 514,2374, 298,4298, 359,  # 2886
2495,  90,2707,1338, 663,  11, 906,1099,2545,  20,2436, 182, 532,1716,7321, 732,  # 2902
1376,4062,1311,1420,3175,  25,2312,1056, 113, 399, 382,1949, 242,3408,2467, 529,  # 2918
3243, 475,1447,3617,7322, 117,  21, 656, 810,1297,2295,2329,3502,7323, 126,4063,  # 2934
 706, 456, 150, 613,4299,  71,1118,2036,4064, 145,3069,  85, 835, 486,2114,1246,  # 2950
1426, 428, 727,1285,1015, 800, 106, 623, 303,1281,7324,2127,2354, 347,3736, 221,  # 2966
3503,3110,7325,1955,1153,4065,  83, 296,1199,3070, 192, 624,  93,7326, 822,1897,  # 2982
2810,3111, 795,2064, 991,1554,1542,1592,  27,  43,2853, 859, 139,1456, 860,4300,  # 2998
 437, 712,3871, 164,2392,3112, 695, 211,3017,2096, 195,3872,1608,3504,3505,3618,  # 3014
3873, 234, 811,2971,2097,3874,2229,1441,3506,1615,2375, 668,2076,1638, 305, 228,  # 3030
1664,4301, 467, 415,7327, 262,2098,1593, 239, 108, 300, 200,1033, 512,1247,2077,  # 3046
7328,7329,2173,3176,3619,2673, 593, 845,1062,3244,  88,1723,2037,3875,1950, 212,  # 3062
 266, 152, 149, 468,1898,4066,4302,  77, 187,7330,3018,  37,   5,2972,7331,3876,  # 3078
7332,7333,  39,2517,4303,2894,3177,2078,  55, 148,  74,4304, 545, 483,1474,1029,  # 3094
1665, 217,1869,1531,3113,1104,2645,4067,  24, 172,3507, 900,3877,3508,3509,4305,  # 3110
  32,1408,2811,1312, 329, 487,2355,2247,2708, 784,2674,   4,3019,3314,1427,1788,  # 3126
 188, 109, 499,7334,3620,1717,1789, 888,1217,3020,4306,7335,3510,7336,3315,1520,  # 3142
3621,3878, 196,1034, 775,7337,7338, 929,1815, 249, 439,  38,7339,1063,7340, 794,  # 3158
3879,1435,2296,  46, 178,3245,2065,7341,2376,7342, 214,1709,4307, 804,  35, 707,  # 3174
 324,3622,1601,2546, 140, 459,4068,7343,7344,1365, 839, 272, 978,2257,2572,3409,  # 3190
2128,1363,3623,1423, 697, 100,3071,  48,  70,1231, 495,3114,2193,7345,1294,7346,  # 3206
2079, 462, 586,1042,3246, 853, 256, 988, 185,2377,3410,1698, 434,1084,7347,3411,  # 3222
 314,2615,2775,4308,2330,2331, 569,2280, 637,1816,2518, 757,1162,1878,1616,3412,  # 3238
 287,1577,2115, 768,4309,1671,2854,3511,2519,1321,3737, 909,2413,7348,4069, 933,  # 3254
3738,7349,2052,2356,1222,4310, 765,2414,1322, 786,4311,7350,1919,1462,1677,2895,  # 3270
1699,7351,4312,1424,2437,3115,3624,2590,3316,1774,1940,3413,3880,4070, 309,1369,  # 3286
1130,2812, 364,2230,1653,1299,3881,3512,3882,3883,2646, 525,1085,3021, 902,2000,  # 3302
1475, 964,4313, 421,1844,1415,1057,2281, 940,1364,3116, 376,4314,4315,1381,   7,  # 3318
2520, 983,2378, 336,1710,2675,1845, 321,3414, 559,1131,3022,2742,1808,1132,1313,  # 3334
 265,1481,1857,7352, 352,1203,2813,3247, 167,1089, 420,2814, 776, 792,1724,3513,  # 3350
4071,2438,3248,7353,4072,7354, 446, 229, 333,2743, 901,3739,1200,1557,4316,2647,  # 3366
1920, 395,2744,2676,3740,4073,1835, 125, 916,3178,2616,4317,7355,7356,3741,7357,  # 3382
7358,7359,4318,3117,3625,1133,2547,1757,3415,1510,2313,1409,3514,7360,2145, 438,  # 3398
2591,2896,2379,3317,1068, 958,3023, 461, 311,2855,2677,4074,1915,3179,4075,1978,  # 3414
 383, 750,2745,2617,4076, 274, 539, 385,1278,1442,7361,1154,1964, 384, 561, 210,  # 3430
  98,1295,2548,3515,7362,1711,2415,1482,3416,3884,2897,1257, 129,7363,3742, 642,  # 3446
 523,2776,2777,2648,7364, 141,2231,1333,  68, 176, 441, 876, 907,4077, 603,2592,  # 3462
 710, 171,3417, 404, 549,  18,3118,2393,1410,3626,1666,7365,3516,4319,2898,4320,  # 3478
7366,2973, 368,7367, 146, 366,  99, 871,3627,1543, 748, 807,1586,1185,  22,2258,  # 3494
 379,3743,3180,7368,3181, 505,1941,2618,1991,1382,2314,7369, 380,2357, 218, 702,  # 3510
1817,1248,3418,3024,3517,3318,3249,7370,2974,3628, 930,3250,3744,7371,  59,7372,  # 3526
 585, 601,4078, 497,3419,1112,1314,4321,1801,7373,1223,1472,2174,7374, 749,1836,  # 3542
 690,1899,3745,1772,3885,1476, 429,1043,1790,2232,2116, 917,4079, 447,1086,1629,  # 3558
7375, 556,7376,7377,2020,1654, 844,1090, 105, 550, 966,1758,2815,1008,1782, 686,  # 3574
1095,7378,2282, 793,1602,7379,3518,2593,4322,4080,2933,2297,4323,3746, 980,2496,  # 3590
 544, 353, 527,4324, 908,2678,2899,7380, 381,2619,1942,1348,7381,1341,1252, 560,  # 3606
3072,7382,3420,2856,7383,2053, 973, 886,2080, 143,4325,7384,7385, 157,3886, 496,  # 3622
4081,  57, 840, 540,2038,4326,4327,3421,2117,1445, 970,2259,1748,1965,2081,4082,  # 3638
3119,1234,1775,3251,2816,3629, 773,1206,2129,1066,2039,1326,3887,1738,1725,4083,  # 3654
 279,3120,  51,1544,2594, 423,1578,2130,2066, 173,4328,1879,7386,7387,1583, 264,  # 3670
 610,3630,4329,2439, 280, 154,7388,7389,7390,1739, 338,1282,3073, 693,2857,1411,  # 3686
1074,3747,2440,7391,4330,7392,7393,1240, 952,2394,7394,2900,1538,2679, 685,1483,  # 3702
4084,2468,1436, 953,4085,2054,4331, 671,2395,  79,4086,2441,3252, 608, 567,2680,  # 3718
3422,4087,4088,1691, 393,1261,1791,2396,7395,4332,7396,7397,7398,7399,1383,1672,  # 3734
3748,3182,1464, 522,1119, 661,1150, 216, 675,4333,3888,1432,3519, 609,4334,2681,  # 3750
2397,7400,7401,7402,4089,3025,   0,7403,2469, 315, 231,2442, 301,3319,4335,2380,  # 3766
7404, 233,4090,3631,1818,4336,4337,7405,  96,1776,1315,2082,7406, 257,7407,1809,  # 3782
3632,2709,1139,1819,4091,2021,1124,2163,2778,1777,2649,7408,3074, 363,1655,3183,  # 3798
7409,2975,7410,7411,7412,3889,1567,3890, 718, 103,3184, 849,1443, 341,3320,2934,  # 3814
1484,7413,1712, 127,  67, 339,4092,2398, 679,1412, 821,7414,7415, 834, 738, 351,  # 3830
2976,2146, 846, 235,1497,1880, 418,1992,3749,2710, 186,1100,2147,2746,3520,1545,  # 3846
1355,2935,2858,1377, 583,3891,4093,2573,2977,7416,1298,3633,1078,2549,3634,2358,  # 3862
  78,3750,3751, 267,1289,2099,2001,1594,4094, 348, 369,1274,2194,2175,1837,4338,  # 3878
1820,2817,3635,2747,2283,2002,4339,2936,2748, 144,3321, 882,4340,3892,2749,3423,  # 3894
4341,2901,7417,4095,1726, 320,7418,3893,3026, 788,2978,7419,2818,1773,1327,2859,  # 3910
3894,2819,7420,1306,4342,2003,1700,3752,3521,2359,2650, 787,2022, 506, 824,3636,  # 3926
 534, 323,4343,1044,3322,2023,1900, 946,3424,7421,1778,1500,1678,7422,1881,4344,  # 3942
 165, 243,4345,3637,2521, 123, 683,4096, 764,4346,  36,3895,1792, 589,2902, 816,  # 3958
 626,1667,3027,2233,1639,1555,1622,3753,3896,7423,3897,2860,1370,1228,1932, 891,  # 3974
2083,2903, 304,4097,7424, 292,2979,2711,3522, 691,2100,4098,1115,4347, 118, 662,  # 3990
7425, 611,1156, 854,2381,1316,2861,   2, 386, 515,2904,7426,7427,3253, 868,2234,  # 4006
1486, 855,2651, 785,2212,3028,7428,1040,3185,3523,7429,3121, 448,7430,1525,7431,  # 4022
2164,4348,7432,3754,7433,4099,2820,3524,3122, 503, 818,3898,3123,1568, 814, 676,  # 4038
1444, 306,1749,7434,3755,1416,1030, 197,1428, 805,2821,1501,4349,7435,7436,7437,  # 4054
1993,7438,4350,7439,7440,2195,  13,2779,3638,2980,3124,1229,1916,7441,3756,2131,  # 4070
7442,4100,4351,2399,3525,7443,2213,1511,1727,1120,7444,7445, 646,3757,2443, 307,  # 4086
7446,7447,1595,3186,7448,7449,7450,3639,1113,1356,3899,1465,2522,2523,7451, 519,  # 4102
7452, 128,2132,  92,2284,1979,7453,3900,1512, 342,3125,2196,7454,2780,2214,1980,  # 4118
3323,7455, 290,1656,1317, 789, 827,2360,7456,3758,4352, 562, 581,3901,7457, 401,  # 4134
4353,2248,  94,4354,1399,2781,7458,1463,2024,4355,3187,1943,7459, 828,1105,4101,  # 4150
1262,1394,7460,4102, 605,4356,7461,1783,2862,7462,2822, 819,2101, 578,2197,2937,  # 4166
7463,1502, 436,3254,4103,3255,2823,3902,2905,3425,3426,7464,2712,2315,7465,7466,  # 4182
2332,2067,  23,4357, 193, 826,3759,2102, 699,1630,4104,3075, 390,1793,1064,3526,  # 4198
7467,1579,3076,3077,1400,7468,4105,1838,1640,2863,7469,4358,4359, 137,4106, 598,  # 4214
3078,1966, 780, 104, 974,2938,7470, 278, 899, 253, 402, 572, 504, 493,1339,7471,  # 4230
3903,1275,4360,2574,2550,7472,3640,3029,3079,2249, 565,1334,2713, 863,  41,7473,  # 4246
7474,4361,7475,1657,2333,  19, 463,2750,4107, 606,7476,2981,3256,1087,2084,1323,  # 4262
2652,2982,7477,1631,1623,1750,4108,2682,7478,2864, 791,2714,2653,2334, 232,2416,  # 4278
7479,2983,1498,7480,2654,2620, 755,1366,3641,3257,3126,2025,1609, 119,1917,3427,  # 4294
 862,1026,4109,7481,3904,3760,4362,3905,4363,2260,1951,2470,7482,1125, 817,4110,  # 4310
4111,3906,1513,1766,2040,1487,4112,3030,3258,2824,3761,3127,7483,7484,1507,7485,  # 4326
2683, 733,  40,1632,1106,2865, 345,4113, 841,2524, 230,4364,2984,1846,3259,3428,  # 4342
7486,1263, 986,3429,7487, 735, 879, 254,1137, 857, 622,1300,1180,1388,1562,3907,  # 4358
3908,2939, 967,2751,2655,1349, 592,2133,1692,3324,2985,1994,4114,1679,3909,1901,  # 4374
2185,7488, 739,3642,2715,1296,1290,7489,4115,2198,2199,1921,1563,2595,2551,1870,  # 4390
2752,2986,7490, 435,7491, 343,1108, 596,  17,1751,4365,2235,3430,3643,7492,4366,  # 4406
 294,3527,2940,1693, 477, 979, 281,2041,3528, 643,2042,3644,2621,2782,2261,1031,  # 4422
2335,2134,2298,3529,4367, 367,1249,2552,7493,3530,7494,4368,1283,3325,2004, 240,  # 4438
1762,3326,4369,4370, 836,1069,3128, 474,7495,2148,2525, 268,3531,7496,3188,1521,  # 4454
1284,7497,1658,1546,4116,7498,3532,3533,7499,4117,3327,2684,1685,4118, 961,1673,  # 4470
2622, 190,2005,2200,3762,4371,4372,7500, 570,2497,3645,1490,7501,4373,2623,3260,  # 4486
1956,4374, 584,1514, 396,1045,1944,7502,4375,1967,2444,7503,7504,4376,3910, 619,  # 4502
7505,3129,3261, 215,2006,2783,2553,3189,4377,3190,4378, 763,4119,3763,4379,7506,  # 4518
7507,1957,1767,2941,3328,3646,1174, 452,1477,4380,3329,3130,7508,2825,1253,2382,  # 4534
2186,1091,2285,4120, 492,7509, 638,1169,1824,2135,1752,3911, 648, 926,1021,1324,  # 4550
4381, 520,4382, 997, 847,1007, 892,4383,3764,2262,1871,3647,7510,2400,1784,4384,  # 4566
1952,2942,3080,3191,1728,4121,2043,3648,4385,2007,1701,3131,1551,  30,2263,4122,  # 4582
7511,2026,4386,3534,7512, 501,7513,4123, 594,3431,2165,1821,3535,3432,3536,3192,  # 4598
 829,2826,4124,7514,1680,3132,1225,4125,7515,3262,4387,4126,3133,2336,7516,4388,  # 4614
4127,7517,3912,3913,7518,1847,2383,2596,3330,7519,4389, 374,3914, 652,4128,4129,  # 4630
 375,1140, 798,7520,7521,7522,2361,4390,2264, 546,1659, 138,3031,2445,4391,7523,  # 4646
2250, 612,1848, 910, 796,3765,1740,1371, 825,3766,3767,7524,2906,2554,7525, 692,  # 4662
 444,3032,2624, 801,4392,4130,7526,1491, 244,1053,3033,4131,4132, 340,7527,3915,  # 4678
1041,2987, 293,1168,  87,1357,7528,1539, 959,7529,2236, 721, 694,4133,3768, 219,  # 4694
1478, 644,1417,3331,2656,1413,1401,1335,1389,3916,7530,7531,2988,2362,3134,1825,  # 4710
 730,1515, 184,2827,  66,4393,7532,1660,2943, 246,3332, 378,1457, 226,3433, 975,  # 4726
3917,2944,1264,3537, 674, 696,7533, 163,7534,1141,2417,2166, 713,3538,3333,4394,  # 4742
3918,7535,7536,1186,  15,7537,1079,1070,7538,1522,3193,3539, 276,1050,2716, 758,  # 4758
1126, 653,2945,3263,7539,2337, 889,3540,3919,3081,2989, 903,1250,4395,3920,3434,  # 4774
3541,1342,1681,1718, 766,3264, 286,  89,2946,3649,7540,1713,7541,2597,3334,2990,  # 4790
7542,2947,2215,3194,2866,7543,4396,2498,2526, 181, 387,1075,3921, 731,2187,3335,  # 4806
7544,3265, 310, 313,3435,2299, 770,4134,  54,3034, 189,4397,3082,3769,3922,7545,  # 4822
1230,1617,1849, 355,3542,4135,4398,3336, 111,4136,3650,1350,3135,3436,3035,4137,  # 4838
2149,3266,3543,7546,2784,3923,3924,2991, 722,2008,7547,1071, 247,1207,2338,2471,  # 4854
1378,4399,2009, 864,1437,1214,4400, 373,3770,1142,2216, 667,4401, 442,2753,2555,  # 4870
3771,3925,1968,4138,3267,1839, 837, 170,1107, 934,1336,1882,7548,7549,2118,4139,  # 4886
2828, 743,1569,7550,4402,4140, 582,2384,1418,3437,7551,1802,7552, 357,1395,1729,  # 4902
3651,3268,2418,1564,2237,7553,3083,3772,1633,4403,1114,2085,4141,1532,7554, 482,  # 4918
2446,4404,7555,7556,1492, 833,1466,7557,2717,3544,1641,2829,7558,1526,1272,3652,  # 4934
4142,1686,1794, 416,2556,1902,1953,1803,7559,3773,2785,3774,1159,2316,7560,2867,  # 4950
4405,1610,1584,3036,2419,2754, 443,3269,1163,3136,7561,7562,3926,7563,4143,2499,  # 4966
3037,4406,3927,3137,2103,1647,3545,2010,1872,4144,7564,4145, 431,3438,7565, 250,  # 4982
  97,  81,4146,7566,1648,1850,1558, 160, 848,7567, 866, 740,1694,7568,2201,2830,  # 4998
3195,4147,4407,3653,1687, 950,2472, 426, 469,3196,3654,3655,3928,7569,7570,1188,  # 5014
 424,1995, 861,3546,4148,3775,2202,2685, 168,1235,3547,4149,7571,2086,1674,4408,  # 5030
3337,3270, 220,2557,1009,7572,3776, 670,2992, 332,1208, 717,7573,7574,3548,2447,  # 5046
3929,3338,7575, 513,7576,1209,2868,3339,3138,4409,1080,7577,7578,7579,7580,2527,  # 5062
3656,3549, 815,1587,3930,3931,7581,3550,3439,3777,1254,4410,1328,3038,1390,3932,  # 5078
1741,3933,3778,3934,7582, 236,3779,2448,3271,7583,7584,3657,3780,1273,3781,4411,  # 5094
7585, 308,7586,4412, 245,4413,1851,2473,1307,2575, 430, 715,2136,2449,7587, 270,  # 5110
 199,2869,3935,7588,3551,2718,1753, 761,1754, 725,1661,1840,4414,3440,3658,7589,  # 5126
7590, 587,  14,3272, 227,2598, 326, 480,2265, 943,2755,3552, 291, 650,1883,7591,  # 5142
1702,1226, 102,1547,  62,3441, 904,4415,3442,1164,4150,7592,7593,1224,1548,2756,  # 5158
 391, 498,1493,7594,1386,1419,7595,2055,1177,4416, 813, 880,1081,2363, 566,1145,  # 5174
4417,2286,1001,1035,2558,2599,2238, 394,1286,7596,7597,2068,7598,  86,1494,1730,  # 5190
3936, 491,1588, 745, 897,2948, 843,3340,3937,2757,2870,3273,1768, 998,2217,2069,  # 5206
 397,1826,1195,1969,3659,2993,3341, 284,7599,3782,2500,2137,2119,1903,7600,3938,  # 5222
2150,3939,4151,1036,3443,1904, 114,2559,4152, 209,1527,7601,7602,2949,2831,2625,  # 5238
2385,2719,3139, 812,2560,7603,3274,7604,1559, 737,1884,3660,1210, 885,  28,2686,  # 5254
3553,3783,7605,4153,1004,1779,4418,7606, 346,1981,2218,2687,4419,3784,1742, 797,  # 5270
1642,3940,1933,1072,1384,2151, 896,3941,3275,3661,3197,2871,3554,7607,2561,1958,  # 5286
4420,2450,1785,7608,7609,7610,3942,4154,1005,1308,3662,4155,2720,4421,4422,1528,  # 5302
2600, 161,1178,4156,1982, 987,4423,1101,4157, 631,3943,1157,3198,2420,1343,1241,  # 5318
1016,2239,2562, 372, 877,2339,2501,1160, 555,1934, 911,3944,7611, 466,1170, 169,  # 5334
1051,2907,2688,3663,2474,2994,1182,2011,2563,1251,2626,7612, 992,2340,3444,1540,  # 5350
2721,1201,2070,2401,1996,2475,7613,4424, 528,1922,2188,1503,1873,1570,2364,3342,  # 5366
3276,7614, 557,1073,7615,1827,3445,2087,2266,3140,3039,3084, 767,3085,2786,4425,  # 5382
1006,4158,4426,2341,1267,2176,3664,3199, 778,3945,3200,2722,1597,2657,7616,4427,  # 5398
7617,3446,7618,7619,7620,3277,2689,1433,3278, 131,  95,1504,3946, 723,4159,3141,  # 5414
1841,3555,2758,2189,3947,2027,2104,3665,7621,2995,3948,1218,7622,3343,3201,3949,  # 5430
4160,2576, 248,1634,3785, 912,7623,2832,3666,3040,3786, 654,  53,7624,2996,7625,  # 5446
1688,4428, 777,3447,1032,3950,1425,7626, 191, 820,2120,2833, 971,4429, 931,3202,  # 5462
 135, 664, 783,3787,1997, 772,2908,1935,3951,3788,4430,2909,3203, 282,2723, 640,  # 5478
1372,3448,1127, 922, 325,3344,7627,7628, 711,2044,7629,7630,3952,2219,2787,1936,  # 5494
3953,3345,2220,2251,3789,2300,7631,4431,3790,1258,3279,3954,3204,2138,2950,3955,  # 5510
3956,7632,2221, 258,3205,4432, 101,1227,7633,3280,1755,7634,1391,3281,7635,2910,  # 5526
2056, 893,7636,7637,7638,1402,4161,2342,7639,7640,3206,3556,7641,7642, 878,1325,  # 5542
1780,2788,4433, 259,1385,2577, 744,1183,2267,4434,7643,3957,2502,7644, 684,1024,  # 5558
4162,7645, 472,3557,3449,1165,3282,3958,3959, 322,2152, 881, 455,1695,1152,1340,  # 5574
 660, 554,2153,4435,1058,4436,4163, 830,1065,3346,3960,4437,1923,7646,1703,1918,  # 5590
7647, 932,2268, 122,7648,4438, 947, 677,7649,3791,2627, 297,1905,1924,2269,4439,  # 5606
2317,3283,7650,7651,4164,7652,4165,  84,4166, 112, 989,7653, 547,1059,3961, 701,  # 5622
3558,1019,7654,4167,7655,3450, 942, 639, 457,2301,2451, 993,2951, 407, 851, 494,  # 5638
4440,3347, 927,7656,1237,7657,2421,3348, 573,4168, 680, 921,2911,1279,1874, 285,  # 5654
 790,1448,1983, 719,2167,7658,7659,4441,3962,3963,1649,7660,1541, 563,7661,1077,  # 5670
7662,3349,3041,3451, 511,2997,3964,3965,3667,3966,1268,2564,3350,3207,4442,4443,  # 5686
7663, 535,1048,1276,1189,2912,2028,3142,1438,1373,2834,2952,1134,2012,7664,4169,  # 5702
1238,2578,3086,1259,7665, 700,7666,2953,3143,3668,4170,7667,4171,1146,1875,1906,  # 5718
4444,2601,3967, 781,2422, 132,1589, 203, 147, 273,2789,2402, 898,1786,2154,3968,  # 5734
3969,7668,3792,2790,7669,7670,4445,4446,7671,3208,7672,1635,3793, 965,7673,1804,  # 5750
2690,1516,3559,1121,1082,1329,3284,3970,1449,3794,  65,1128,2835,2913,2759,1590,  # 5766
3795,7674,7675,  12,2658,  45, 976,2579,3144,4447, 517,2528,1013,1037,3209,7676,  # 5782
3796,2836,7677,3797,7678,3452,7679,2602, 614,1998,2318,3798,3087,2724,2628,7680,  # 5798
2580,4172, 599,1269,7681,1810,3669,7682,2691,3088, 759,1060, 489,1805,3351,3285,  # 5814
1358,7683,7684,2386,1387,1215,2629,2252, 490,7685,7686,4173,1759,2387,2343,7687,  # 5830
4448,3799,1907,3971,2630,1806,3210,4449,3453,3286,2760,2344, 874,7688,7689,3454,  # 5846
3670,1858,  91,2914,3671,3042,3800,4450,7690,3145,3972,2659,7691,3455,1202,1403,  # 5862
3801,2954,2529,1517,2503,4451,3456,2504,7692,4452,7693,2692,1885,1495,1731,3973,  # 5878
2365,4453,7694,2029,7695,7696,3974,2693,1216, 237,2581,4174,2319,3975,3802,4454,  # 5894
4455,2694,3560,3457, 445,4456,7697,7698,7699,7700,2761,  61,3976,3672,1822,3977,  # 5910
7701, 687,2045, 935, 925, 405,2660, 703,1096,1859,2725,4457,3978,1876,1367,2695,  # 5926
3352, 918,2105,1781,2476, 334,3287,1611,1093,4458, 564,3146,3458,3673,3353, 945,  # 5942
2631,2057,4459,7702,1925, 872,4175,7703,3459,2696,3089, 349,4176,3674,3979,4460,  # 5958
3803,4177,3675,2155,3980,4461,4462,4178,4463,2403,2046, 782,3981, 400, 251,4179,  # 5974
1624,7704,7705, 277,3676, 299,1265, 476,1191,3804,2121,4180,4181,1109, 205,7706,  # 5990
2582,1000,2156,3561,1860,7707,7708,7709,4464,7710,4465,2565, 107,2477,2157,3982,  # 6006
3460,3147,7711,1533, 541,1301, 158, 753,4182,2872,3562,7712,1696, 370,1088,4183,  # 6022
4466,3563, 579, 327, 440, 162,2240, 269,1937,1374,3461, 968,3043,  56,1396,3090,  # 6038
2106,3288,3354,7713,1926,2158,4467,2998,7714,3564,7715,7716,3677,4468,2478,7717,  # 6054
2791,7718,1650,4469,7719,2603,7720,7721,3983,2661,3355,1149,3356,3984,3805,3985,  # 6070
7722,1076,  49,7723, 951,3211,3289,3290, 450,2837, 920,7724,1811,2792,2366,4184,  # 6086
1908,1138,2367,3806,3462,7725,3212,4470,1909,1147,1518,2423,4471,3807,7726,4472,  # 6102
2388,2604, 260,1795,3213,7727,7728,3808,3291, 708,7729,3565,1704,7730,3566,1351,  # 6118
1618,3357,2999,1886, 944,4185,3358,4186,3044,3359,4187,7731,3678, 422, 413,1714,  # 6134
3292, 500,2058,2345,4188,2479,7732,1344,1910, 954,7733,1668,7734,7735,3986,2404,  # 6150
4189,3567,3809,4190,7736,2302,1318,2505,3091, 133,3092,2873,4473, 629,  31,2838,  # 6166
2697,3810,4474, 850, 949,4475,3987,2955,1732,2088,4191,1496,1852,7737,3988, 620,  # 6182
3214, 981,1242,3679,3360,1619,3680,1643,3293,2139,2452,1970,1719,3463,2168,7738,  # 6198
3215,7739,7740,3361,1828,7741,1277,4476,1565,2047,7742,1636,3568,3093,7743, 869,  # 6214
2839, 655,3811,3812,3094,3989,3000,3813,1310,3569,4477,7744,7745,7746,1733, 558,  # 6230
4478,3681, 335,1549,3045,1756,4192,3682,1945,3464,1829,1291,1192, 470,2726,2107,  # 6246
2793, 913,1054,3990,7747,1027,7748,3046,3991,4479, 982,2662,3362,3148,3465,3216,  # 6262
3217,1946,2794,7749, 571,4480,7750,1830,7751,3570,2583,1523,2424,7752,2089, 984,  # 6278
4481,3683,1959,7753,3684, 852, 923,2795,3466,3685, 969,1519, 999,2048,2320,1705,  # 6294
7754,3095, 615,1662, 151, 597,3992,2405,2321,1049, 275,4482,3686,4193, 568,3687,  # 6310
3571,2480,4194,3688,7755,2425,2270, 409,3218,7756,1566,2874,3467,1002, 769,2840,  # 6326
 194,2090,3149,3689,2222,3294,4195, 628,1505,7757,7758,1763,2177,3001,3993, 521,  # 6342
1161,2584,1787,2203,2406,4483,3994,1625,4196,4197, 412,  42,3096, 464,7759,2632,  # 6358
4484,3363,1760,1571,2875,3468,2530,1219,2204,3814,2633,2140,2368,4485,4486,3295,  # 6374
1651,3364,3572,7760,7761,3573,2481,3469,7762,3690,7763,7764,2271,2091, 460,7765,  # 6390
4487,7766,3002, 962, 588,3574, 289,3219,2634,1116,  52,7767,3047,1796,7768,7769,  # 6406
7770,1467,7771,1598,1143,3691,4198,1984,1734,1067,4488,1280,3365, 465,4489,1572,  # 6422
 510,7772,1927,2241,1812,1644,3575,7773,4490,3692,7774,7775,2663,1573,1534,7776,  # 6438
7777,4199, 536,1807,1761,3470,3815,3150,2635,7778,7779,7780,4491,3471,2915,1911,  # 6454
2796,7781,3296,1122, 377,3220,7782, 360,7783,7784,4200,1529, 551,7785,2059,3693,  # 6470
1769,2426,7786,2916,4201,3297,3097,2322,2108,2030,4492,1404, 136,1468,1479, 672,  # 6486
1171,3221,2303, 271,3151,7787,2762,7788,2049, 678,2727, 865,1947,4493,7789,2013,  # 6502
3995,2956,7790,2728,2223,1397,3048,3694,4494,4495,1735,2917,3366,3576,7791,3816,  # 6518
 509,2841,2453,2876,3817,7792,7793,3152,3153,4496,4202,2531,4497,2304,1166,1010,  # 6534
 552, 681,1887,7794,7795,2957,2958,3996,1287,1596,1861,3154, 358, 453, 736, 175,  # 6550
 478,1117, 905,1167,1097,7796,1853,1530,7797,1706,7798,2178,3472,2287,3695,3473,  # 6566
3577,4203,2092,4204,7799,3367,1193,2482,4205,1458,2190,2205,1862,1888,1421,3298,  # 6582
2918,3049,2179,3474, 595,2122,7800,3997,7801,7802,4206,1707,2636, 223,3696,1359,  # 6598
 751,3098, 183,3475,7803,2797,3003, 419,2369, 633, 704,3818,2389, 241,7804,7805,  # 6614
7806, 838,3004,3697,2272,2763,2454,3819,1938,2050,3998,1309,3099,2242,1181,7807,  # 6630
1136,2206,3820,2370,1446,4207,2305,4498,7808,7809,4208,1055,2605, 484,3698,7810,  # 6646
3999, 625,4209,2273,3368,1499,4210,4000,7811,4001,4211,3222,2274,2275,3476,7812,  # 6662
7813,2764, 808,2606,3699,3369,4002,4212,3100,2532, 526,3370,3821,4213, 955,7814,  # 6678
1620,4214,2637,2427,7815,1429,3700,1669,1831, 994, 928,7816,3578,1260,7817,7818,  # 6694
7819,1948,2288, 741,2919,1626,4215,2729,2455, 867,1184, 362,3371,1392,7820,7821,  # 6710
4003,4216,1770,1736,3223,2920,4499,4500,1928,2698,1459,1158,7822,3050,3372,2877,  # 6726
1292,1929,2506,2842,3701,1985,1187,2071,2014,2607,4217,7823,2566,2507,2169,3702,  # 6742
2483,3299,7824,3703,4501,7825,7826, 666,1003,3005,1022,3579,4218,7827,4502,1813,  # 6758
2253, 574,3822,1603, 295,1535, 705,3823,4219, 283, 858, 417,7828,7829,3224,4503,  # 6774
4504,3051,1220,1889,1046,2276,2456,4004,1393,1599, 689,2567, 388,4220,7830,2484,  # 6790
 802,7831,2798,3824,2060,1405,2254,7832,4505,3825,2109,1052,1345,3225,1585,7833,  # 6806
 809,7834,7835,7836, 575,2730,3477, 956,1552,1469,1144,2323,7837,2324,1560,2457,  # 6822
3580,3226,4005, 616,2207,3155,2180,2289,7838,1832,7839,3478,4506,7840,1319,3704,  # 6838
3705,1211,3581,1023,3227,1293,2799,7841,7842,7843,3826, 607,2306,3827, 762,2878,  # 6854
1439,4221,1360,7844,1485,3052,7845,4507,1038,4222,1450,2061,2638,4223,1379,4508,  # 6870
2585,7846,7847,4224,1352,1414,2325,2921,1172,7848,7849,3828,3829,7850,1797,1451,  # 6886
7851,7852,7853,7854,2922,4006,4007,2485,2346, 411,4008,4009,3582,3300,3101,4509,  # 6902
1561,2664,1452,4010,1375,7855,7856,  47,2959, 316,7857,1406,1591,2923,3156,7858,  # 6918
1025,2141,3102,3157, 354,2731, 884,2224,4225,2407, 508,3706, 726,3583, 996,2428,  # 6934
3584, 729,7859, 392,2191,1453,4011,4510,3707,7860,7861,2458,3585,2608,1675,2800,  # 6950
 919,2347,2960,2348,1270,4511,4012,  73,7862,7863, 647,7864,3228,2843,2255,1550,  # 6966
1346,3006,7865,1332, 883,3479,7866,7867,7868,7869,3301,2765,7870,1212, 831,1347,  # 6982
4226,4512,2326,3830,1863,3053, 720,3831,4513,4514,3832,7871,4227,7872,7873,4515,  # 6998
7874,7875,1798,4516,3708,2609,4517,3586,1645,2371,7876,7877,2924, 669,2208,2665,  # 7014
2429,7878,2879,7879,7880,1028,3229,7881,4228,2408,7882,2256,1353,7883,7884,4518,  # 7030
3158, 518,7885,4013,7886,4229,1960,7887,2142,4230,7888,7889,3007,2349,2350,3833,  # 7046
 516,1833,1454,4014,2699,4231,4519,2225,2610,1971,1129,3587,7890,2766,7891,2961,  # 7062
1422, 577,1470,3008,1524,3373,7892,7893, 432,4232,3054,3480,7894,2586,1455,2508,  # 7078
2226,1972,1175,7895,1020,2732,4015,3481,4520,7896,2733,7897,1743,1361,3055,3482,  # 7094
2639,4016,4233,4521,2290, 895, 924,4234,2170, 331,2243,3056, 166,1627,3057,1098,  # 7110
7898,1232,2880,2227,3374,4522, 657, 403,1196,2372, 542,3709,3375,1600,4235,3483,  # 7126
7899,4523,2767,3230, 576, 530,1362,7900,4524,2533,2666,3710,4017,7901, 842,3834,  # 7142
7902,2801,2031,1014,4018, 213,2700,3376, 665, 621,4236,7903,3711,2925,2430,7904,  # 7158
2431,3302,3588,3377,7905,4237,2534,4238,4525,3589,1682,4239,3484,1380,7906, 724,  # 7174
2277, 600,1670,7907,1337,1233,4526,3103,2244,7908,1621,4527,7909, 651,4240,7910,  # 7190
1612,4241,2611,7911,2844,7912,2734,2307,3058,7913, 716,2459,3059, 174,1255,2701,  # 7206
4019,3590, 548,1320,1398, 728,4020,1574,7914,1890,1197,3060,4021,7915,3061,3062,  # 7222
3712,3591,3713, 747,7916, 635,4242,4528,7917,7918,7919,4243,7920,7921,4529,7922,  # 7238
3378,4530,2432, 451,7923,3714,2535,2072,4244,2735,4245,4022,7924,1764,4531,7925,  # 7254
4246, 350,7926,2278,2390,2486,7927,4247,4023,2245,1434,4024, 488,4532, 458,4248,  # 7270
4025,3715, 771,1330,2391,3835,2568,3159,2159,2409,1553,2667,3160,4249,7928,2487,  # 7286
2881,2612,1720,2702,4250,3379,4533,7929,2536,4251,7930,3231,4252,2768,7931,2015,  # 7302
2736,7932,1155,1017,3716,3836,7933,3303,2308, 201,1864,4253,1430,7934,4026,7935,  # 7318
7936,7937,7938,7939,4254,1604,7940, 414,1865, 371,2587,4534,4535,3485,2016,3104,  # 7334
4536,1708, 960,4255, 887, 389,2171,1536,1663,1721,7941,2228,4027,2351,2926,1580,  # 7350
7942,7943,7944,1744,7945,2537,4537,4538,7946,4539,7947,2073,7948,7949,3592,3380,  # 7366
2882,4256,7950,4257,2640,3381,2802, 673,2703,2460, 709,3486,4028,3593,4258,7951,  # 7382
1148, 502, 634,7952,7953,1204,4540,3594,1575,4541,2613,3717,7954,3718,3105, 948,  # 7398
3232, 121,1745,3837,1110,7955,4259,3063,2509,3009,4029,3719,1151,1771,3838,1488,  # 7414
4030,1986,7956,2433,3487,7957,7958,2093,7959,4260,3839,1213,1407,2803, 531,2737,  # 7430
2538,3233,1011,1537,7960,2769,4261,3106,1061,7961,3720,3721,1866,2883,7962,2017,  # 7446
 120,4262,4263,2062,3595,3234,2309,3840,2668,3382,1954,4542,7963,7964,3488,1047,  # 7462
2704,1266,7965,1368,4543,2845, 649,3383,3841,2539,2738,1102,2846,2669,7966,7967,  # 7478
1999,7968,1111,3596,2962,7969,2488,3842,3597,2804,1854,3384,3722,7970,7971,3385,  # 7494
2410,2884,3304,3235,3598,7972,2569,7973,3599,2805,4031,1460, 856,7974,3600,7975,  # 7510
2885,2963,7976,2886,3843,7977,4264, 632,2510, 875,3844,1697,3845,2291,7978,7979,  # 7526
4544,3010,1239, 580,4545,4265,7980, 914, 936,2074,1190,4032,1039,2123,7981,7982,  # 7542
7983,3386,1473,7984,1354,4266,3846,7985,2172,3064,4033, 915,3305,4267,4268,3306,  # 7558
1605,1834,7986,2739, 398,3601,4269,3847,4034, 328,1912,2847,4035,3848,1331,4270,  # 7574
3011, 937,4271,7987,3602,4036,4037,3387,2160,4546,3388, 524, 742, 538,3065,1012,  # 7590
7988,7989,3849,2461,7990, 658,1103, 225,3850,7991,7992,4547,7993,4548,7994,3236,  # 7606
1243,7995,4038, 963,2246,4549,7996,2705,3603,3161,7997,7998,2588,2327,7999,4550,  # 7622
8000,8001,8002,3489,3307, 957,3389,2540,2032,1930,2927,2462, 870,2018,3604,1746,  # 7638
2770,2771,2434,2463,8003,3851,8004,3723,3107,3724,3490,3390,3725,8005,1179,3066,  # 7654
8006,3162,2373,4272,3726,2541,3163,3108,2740,4039,8007,3391,1556,2542,2292, 977,  # 7670
2887,2033,4040,1205,3392,8008,1765,3393,3164,2124,1271,1689, 714,4551,3491,8009,  # 7686
2328,3852, 533,4273,3605,2181, 617,8010,2464,3308,3492,2310,8011,8012,3165,8013,  # 7702
8014,3853,1987, 618, 427,2641,3493,3394,8015,8016,1244,1690,8017,2806,4274,4552,  # 7718
8018,3494,8019,8020,2279,1576, 473,3606,4275,3395, 972,8021,3607,8022,3067,8023,  # 7734
8024,4553,4554,8025,3727,4041,4042,8026, 153,4555, 356,8027,1891,2888,4276,2143,  # 7750
 408, 803,2352,8028,3854,8029,4277,1646,2570,2511,4556,4557,3855,8030,3856,4278,  # 7766
8031,2411,3396, 752,8032,8033,1961,2964,8034, 746,3012,2465,8035,4279,3728, 698,  # 7782
4558,1892,4280,3608,2543,4559,3609,3857,8036,3166,3397,8037,1823,1302,4043,2706,  # 7798
3858,1973,4281,8038,4282,3167, 823,1303,1288,1236,2848,3495,4044,3398, 774,3859,  # 7814
8039,1581,4560,1304,2849,3860,4561,8040,2435,2161,1083,3237,4283,4045,4284, 344,  # 7830
1173, 288,2311, 454,1683,8041,8042,1461,4562,4046,2589,8043,8044,4563, 985, 894,  # 7846
8045,3399,3168,8046,1913,2928,3729,1988,8047,2110,1974,8048,4047,8049,2571,1194,  # 7862
 425,8050,4564,3169,1245,3730,4285,8051,8052,2850,8053, 636,4565,1855,3861, 760,  # 7878
1799,8054,4286,2209,1508,4566,4048,1893,1684,2293,8055,8056,8057,4287,4288,2210,  # 7894
 479,8058,8059, 832,8060,4049,2489,8061,2965,2490,3731, 990,3109, 627,1814,2642,  # 7910
4289,1582,4290,2125,2111,3496,4567,8062, 799,4291,3170,8063,4568,2112,1737,3013,  # 7926
1018, 543, 754,4292,3309,1676,4569,4570,4050,8064,1489,8065,3497,8066,2614,2889,  # 7942
4051,8067,8068,2966,8069,8070,8071,8072,3171,4571,4572,2182,1722,8073,3238,3239,  # 7958
1842,3610,1715, 481, 365,1975,1856,8074,8075,1962,2491,4573,8076,2126,3611,3240,  # 7974
 433,1894,2063,2075,8077, 602,2741,8078,8079,8080,8081,8082,3014,1628,3400,8083,  # 7990
3172,4574,4052,2890,4575,2512,8084,2544,2772,8085,8086,8087,3310,4576,2891,8088,  # 8006
4577,8089,2851,4578,4579,1221,2967,4053,2513,8090,8091,8092,1867,1989,8093,8094,  # 8022
8095,1895,8096,8097,4580,1896,4054, 318,8098,2094,4055,4293,8099,8100, 485,8101,  # 8038
 938,3862, 553,2670, 116,8102,3863,3612,8103,3498,2671,2773,3401,3311,2807,8104,  # 8054
3613,2929,4056,1747,2930,2968,8105,8106, 207,8107,8108,2672,4581,2514,8109,3015,  # 8070
 890,3614,3864,8110,1877,3732,3402,8111,2183,2353,3403,1652,8112,8113,8114, 941,  # 8086
2294, 208,3499,4057,2019, 330,4294,3865,2892,2492,3733,4295,8115,8116,8117,8118,  # 8102
)

