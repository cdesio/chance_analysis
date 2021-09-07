import sys
import re
import os
import numpy as np

regex = re.compile(r"\d+")

if not len(sys.argv) == 5:
    raise Exception(
        "Please insert file name (list of bad files), output path and range of files"
    )

bad_files_list = sys.argv[1]

if not os.path.exists(bad_files_list):
    raise FileNotFoundError

output_path = str(sys.argv[2])
f_nb_l, f_nb_r = int(sys.argv[3]), int(sys.argv[4])

list_bad = []
with open(os.path.join(".", bad_files_list)) as f1:
    for l in f1:
        list_bad.append(l)
bad_idx = [int(regex.findall(fil.split("\n")[0])[0]) for fil in list_bad]

count = 0
outfile = (
    "_".join(["good", *bad_files_list.split("_")[1:]])
    if bad_files_list.startswith("bad")
    else "_".join(["good", bad_files_list]) + ".txt"
)
test_out_idx = []
with open(os.path.join(".", outfile), "w+") as f2:
    for i in np.arange(int(f_nb_l), int(f_nb_r)):
        if i not in np.unique(bad_idx):
            count += 1
            test_out_idx.append(i)
            f2.write(output_path + "Vertexing_{}.root\n".format(i))
print("output path: {}".format(output_path))
print(
    "Total files: {}, Bad files: {}, Good files: {}.".format(
        f_nb_r, len(np.unique(bad_idx)), count
    )
)
if len(np.unique(bad_idx)) + count == f_nb_r - f_nb_l:
    print("done. list of good files saved to '{}'.".format(outfile))