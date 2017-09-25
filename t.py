# import os
# print "lllllllllllllllllooooooooooooo"
# try:
#     # f1 = open('bak2.txt', 'r')
#     # f2 = open('out1.txt', 'a')
#     # f1c = f1.read()
#     # f2c = f1c
#     # for i in range(100):
#     #     f2c = f2c.replace('    ', '   ')
#     # f2.seek(0, 0)
#     # f2.write(f2c)
#     # f1.close()
#     # f2.close()
#
#     f2 = open('out1.txt', 'r')
#     f3 = open('out2.txt', 'a')
#     f3_c = []
#     while 1:
#         line = f2.readline()
#         if not line:
#             break
#
#         if line.startswith('#') or not line.split():
#             continue
#
#         llist = line.split('   ')
#         name = llist[0]
#         desc = llist[-1].strip('\n')
#         adict = {"service_name": name, "description": desc}
#         print "l------------- dict = %s\n" % adict
#         f3_c.append(adict)
#
#     # f3_d = list(set(f3_d))
#     f3.write(str(f3_c))
#
#     f2.close()
#     f3.close()
#
# except:
#     import traceback
#     print ("error --------------- %s" % traceback.format_exc())


class A(object):
    dd = {"a": "a",
          }


class B(A):
    dd = {"b": "b",
          }


mm = B()
print mm.dd
