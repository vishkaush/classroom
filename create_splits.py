import os
import sys
import random

dir_path = sys.argv[1]
out_dir_path = sys.argv[2]
files = os.listdir(dir_path)
one_gda = []
one_pa = []
two_gda = []
two_pa = []
three_gda = []
three_pa = []
four_pa = []
best = []
ch01 = []
print("Total files in ", dir_path, " = ", len(files))
for file in files:
    full_filename = os.path.join(dir_path, file)
    if file.startswith("1_GDA"):
        one_gda.append(full_filename)
    elif file.startswith("1_PA"):
        one_pa.append(full_filename)
    elif file.startswith("2_GDA"):
        two_gda.append(full_filename)
    elif file.startswith("2_PA"):
        two_pa.append(full_filename)
    elif file.startswith("3_GDA"):
        three_gda.append(full_filename)
    elif file.startswith("3_PA"):
        three_pa.append(full_filename)
    elif file.startswith("4_PA"):
        four_pa.append(full_filename)
    elif file.startswith("best"):
        best.append(full_filename)
    elif file.startswith("ch01"):
        ch01.append(full_filename)
print("Total one_gda files = ", len(one_gda))
print("Total two_gda files = ", len(two_gda))
print("Total three_gda files = ", len(three_gda))
print("Total one_pa files = ", len(one_pa))
print("Total two_pa files = ", len(two_pa))
print("Total three_pa files = ", len(three_pa))
print("Total four_pa files = ", len(four_pa))
print("Total best files = ", len(best))
print("Total ch01 files = ", len(ch01))
one_gda_test = random.sample(one_gda, int(0.2*len(one_gda)))
one_gda_train = list(set(one_gda) - set(one_gda_test))
one_pa_test = random.sample(one_pa, int(0.2*len(one_pa)))
one_pa_train = list(set(one_pa) - set(one_pa_test))
two_gda_test = random.sample(two_gda, int(0.2*len(two_gda)))
two_gda_train = list(set(two_gda) - set(two_gda_test))
three_gda_test = random.sample(three_gda, int(0.2*len(three_gda)))
three_gda_train = list(set(three_gda) - set(three_gda_test))
two_pa_test = random.sample(two_pa, int(0.2*len(two_pa)))
two_pa_train = list(set(two_pa) - set(two_pa_test))
three_pa_test = random.sample(three_pa, int(0.2*len(three_pa)))
three_pa_train = list(set(three_pa) - set(three_pa_test))
four_pa_test = random.sample(four_pa, int(0.2*len(four_pa)))
four_pa_train = list(set(four_pa) - set(four_pa_test))
best_test = random.sample(best, int(0.2*len(best)))
best_train = list(set(best) - set(best_test))
ch01_test = random.sample(ch01, int(0.2*len(ch01)))
ch01_train = list(set(ch01) - set(ch01_test))

print("Total one_gda_test files = ", len(one_gda_test))
print("Total two_gda_test files = ", len(two_gda_test))
print("Total three_gda_test files = ", len(three_gda_test))
print("Total one_pa_test files = ", len(one_pa_test))
print("Total two_pa_test files = ", len(two_pa_test))
print("Total three_pa_test files = ", len(three_pa_test))
print("Total four_pa_test files = ", len(four_pa_test))
print("Total best_test files = ", len(best_test))
print("Total ch01_test files = ", len(ch01_test))

if not os.path.exists(os.path.join(out_dir_path, "train")):
    os.mkdir(os.path.join(out_dir_path, "train"))
if not os.path.exists(os.path.join(out_dir_path, "test")):
    os.mkdir(os.path.join(out_dir_path, "test"))
if not os.path.exists(os.path.join(out_dir_path, "train", "started")):
    os.mkdir(os.path.join(out_dir_path, "train", "started"))
if not os.path.exists(os.path.join(out_dir_path, "test", "started")):
    os.mkdir(os.path.join(out_dir_path, "test", "started"))
testPath = os.path.join(out_dir_path, "test", "started")
trainPath = os.path.join(out_dir_path, "train", "started")
for elem in one_gda_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in one_gda_train:
    os.system('cp ' + elem + ' ' + trainPath)
for elem in two_gda_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in two_gda_train:
    os.system('cp ' + elem + ' ' + trainPath)
for elem in three_gda_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in three_gda_train:
    os.system('cp ' + elem + ' ' + trainPath)
for elem in one_pa_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in one_pa_train:
    os.system('cp ' + elem + ' ' + trainPath)
for elem in two_pa_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in two_pa_train:
    os.system('cp ' + elem + ' ' + trainPath)
for elem in three_pa_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in three_pa_train:
    os.system('cp ' + elem + ' ' + trainPath)
for elem in four_pa_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in four_pa_train:
    os.system('cp ' + elem + ' ' + trainPath)
for elem in best_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in best_train:
    os.system('cp ' + elem + ' ' + trainPath)
for elem in ch01_test:
    os.system('cp ' + elem + ' ' + testPath)
for elem in ch01_train:
    os.system('cp ' + elem + ' ' + trainPath)







    


