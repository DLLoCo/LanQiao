n,m=map(int,input().split())
a=pow(10,n-1)
b=pow(10,n)
MOD=998244353
ans=0
for i in range(a+1,b,2):
    s=str(i)
    #! s=s[::-1]别漏了,第一位数
    s=s[::-1]
    l=[0]*(n+1)
    for j in range(1,n+1):
        # print(s,int(s[j-1]))
        l[j]=l[j-1]+int(s[j-1])
        # print(int(s[j-1]),m,"bool",int(s[j-1])>m)
        if int(s[j-1])>m:
            break
        if j>=5:
            if l[j]-l[j-5]>m:
                break
            print(s,l)
        if j%2==1:
            if int(s[j-1])%2!=1:
                break
        else:
            if int(s[j-1])%2!=0:
                break
    else:
        ans=(ans+1)%MOD
        print(ans)
# print(ans){1, 2, 4, 8, 16, 32, 64, 101, 103, 107, 109, 113, 127, 128, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 192, 193, 197, 199, 202, 206, 211, 214, 218, 223, 226, 227, 229, 233, 239, 241, 251, 254, 256, 257, 262, 263, 269, 271, 274, 277, 278, 281, 283, 291, 293, 298, 302, 303, 307, 309, 311, 313, 314, 317, 320, 321, 326, 327, 331, 334, 337, 339, 346, 347, 349, 353, 358, 359, 362, 367, 373, 379, 381, 382, 383, 384, 386, 388, 389, 393, 394, 397, 398, 401, 404, 409, 411, 412, 417, 419, 421, 422, 428, 431, 433, 436, 439, 443, 446, 447, 448, 449, 452, 453, 454, 457, 458, 461, 463, 466, 467, 471, 478, 479, 482, 485, 487, 489, 491, 499, 501, 502, 503, 505, 508, 509, 512, 514, 515, 519, 521, 523, 524, 526, 535, 537, 538, 541, 542, 543, 545, 547, 548, 554, 556, 557, 562, 563, 565, 566, 569, 571, 573, 576, 577, 579, 582, 586, 587, 591, 593, 596, 597, 599, 601, 604, 606, 607, 613, 614, 617, 618, 619, 622, 623, 626, 628, 631, 633, 634, 635, 640, 641, 642, 643, 647, 652, 653, 654, 655, 659, 661, 662, 668, 669, 673, 674, 676, 677, 678, 679, 681, 683, 685, 687, 691, 692, 694, 695, 698, 699, 701, 704, 706, 707, 709, 712, 716, 717, 718, 719, 721, 723, 724, 727, 728, 733, 734, 739, 743, 745, 746, 748, 749, 751, 753, 755, 757, 758, 761, 762, 763, 764, 766, 768, 769, 771, 772, 773, 776, 778, 785, 786, 787, 788, 789, 791, 794, 796, 797, 801, 802, 807, 808, 809, 811, 813, 815, 818, 821, 822, 823, 824, 827, 829, 830, 831, 832, 834, 835, 836, 838, 839, 842, 843, 844, 849, 853, 856, 857, 859, 862, 863, 865, 866, 872, 873, 877, 878, 879, 881, 883, 884, 886, 887, 889, 890, 892, 894, 895, 896, 898, 904, 905, 906, 907, 908, 909, 911, 913, 914, 916, 917, 919, 920, 921, 922, 926, 927, 929, 932, 933, 934, 937, 939, 941, 942, 947, 948, 951, 952, 953, 955, 956, 958, 959, 960, 963, 964, 965, 967, 968, 970, 971, 973, 974, 977, 978, 979, 981, 982, 983, 985, 988, 991, 993, 995, 996, 997, 998, 1000, 1001, 1002, 1004, 1006, 1009, 1010, 1011, 1012, 1013, 1016, 1017, 1018, 1019, 1021, 1024, 1027, 1028, 1030, 1031, 1033, 1038, 1039, 1041, 1042, 1043, 1046, 1047, 1048, 1049, 1051, 1052, 1055, 1057, 1058, 1059, 1061, 1063, 1064, 1067, 1068, 1069, 1070, 1074, 1076, 1077, 1079, 1082, 1084, 1086, 1087, 1088, 1090, 1091, 1093, 1094, 1095, 1096, 1097, 1099, 1101, 1102, 1103, 1106, 1108, 1109, 1111, 1112, 1114, 1115, 1116, 1117, 1119, 1123, 1124, 1126, 1129, 1130, 1132, 1133, 1135, 1136, 1137, 1138, 1141, 1142, 1143, 1144, 1145, 1146, 1149, 1150, 1151, 1152, 1153, 1154, 1156, 1157, 1158, 1160, 1162, 1163, 1164, 1165, 1167, 1168, 1169, 1171, 1172, 1174, 1177, 1178, 1179, 1181, 1182, 1183, 1185, 1186, 1187, 1188, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1198, 1199, 1200, 1201, 1202, 1203, 1205, 1206, 1207, 1208, 1211, 1212, 1213, 1214, 1216, 1217, 1218, 1221, 1223, 1226, 1227, 1228, 1229, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1248, 1249, 1250, 1251, 1252, 1253, 1255, 1256, 1257, 1258, 1259, 1261, 1262, 1263, 1264, 1266, 1267, 1268, 1270, 1271, 1273}