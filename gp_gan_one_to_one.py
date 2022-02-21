import glob
import os
from shutil import copyfile
import random
import itertools

def createPath(curr_subdir):
    """[summary]

    Args:
        curr_subdir ([type]): [description]
    """
    if not os.path.exists(curr_subdir):
        os.makedirs(curr_subdir)
        print(curr_subdir + " directory was made")

def run_one_to_one(gen_src_dir, gen_dst_dir, store_dir, results_dir, domains, n):
    """[summary]

    Args:
        src_dir ([type]): [description]
        dst_dir ([type]): [description]
        store_dir ([type]): [description]
        results_dir ([type]): [description]
        domains ([type]): [description]
        n ([type]): [description]
    """
    
    random.seed(42)

    domain_combos = list(itertools.product(domains, repeat=2))

    for (src_domain, target_domain) in domain_combos:

        src_dir = f"{gen_src_dir}{src_domain}/"

        all_srcs = glob.glob(src_dir + "*.jpg")
        all_masks = glob.glob(src_dir + "*.png")
        all_txts = glob.glob(src_dir + "*.txt")
        all_srcs.sort()
        all_masks.sort()
        all_txts.sort()

        dest_dir = f"{gen_dst_dir}{target_domain}/"
                
        #Have background destination directories
        all_dsts = glob.glob(dest_dir + "*.jpg")
        dst_imgs = random.sample(all_dsts, n)

        #Could shuffle if desired

        store_fname = 

        with open(store_dir + store_fname, "w") as f:
            for file in MW_dsts:
            f.write(file + "\n")

        for i in range(len(all_srcs)):
            my_src = all_srcs[i]
            my_mask = all_masks[i]
            my_txt = all_txts[i]
            src_address = my_src[my_src.rfind("/")+1:my_src.find(".jpg")]

            current_subdir = f"{results_dir}{src_address}/"
            createPath(current_subdir)

            my_dst = dst_imgs[i]
            dst_address = my_dst[my_dst.rfind("/")+1:]

            blended_out = f"{curr_subdir}{dst_address}"
            #Removes space for GP GAN
            blended_out = blended_out.replace(" ", "")

            #Copies txt file of mask to synthetic output
            
            copyfile(my_txt, blended_out.replace(".jpg",".txt"))
            cmd = f"python run_gp_gan.py --src_image {my_src} --dst_image \"{my_dst}\" --mask_image {my_mask} --blended_image {my_mask}"
            print("Running command:")
            print(cmd)
            os.system(cmd)
