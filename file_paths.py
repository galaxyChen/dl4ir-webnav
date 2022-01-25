######################
# Dataset parameters #
######################
vocab_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/D_cbow_pdw_8B.pkl' # Path to the python dictionary containing the vocabulary.
wordemb_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/D_cbow_pdw_8B.pkl' # Path to the python dictionary containing the word embeddings.
idf_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/wiki_idf.pkl' # Path to the IDF dictionary.
pages_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/wiki.hdf5' # Path to save the articles and links.
pages_emb_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/wiki_emb.hdf5' # Path to save articles embeddings (set to None to not compute it).
pages_idx_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/wiki_idx.hdf5' # Path to save articles' words as vocabulary indexes (set to None to not compute it).
qp_path_pre = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/qp.hdf5' # Path to save queries and paths.
index_folder = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/lucene_index/' # folder to store lucene's index. It will be created in case it does not exist.

#########################
# Wikipedia  parameters #
#########################
dump_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/enwiki-latest-pages-articles.xml' # Path to the wikipedia dump file.
page_pos_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/page_pos.pkl' # Path to save the dictionary that stores each article position in the wikipedia dump file.
cat_pages_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/cat_pages.pkl' # Path to save the dictionary that stores the pages in each wikipedia category.

###############################
# Jeopardy dataset parameters #
###############################
jeopardy_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/JEOPARDY.csv' # Path to the csv containing jeopardy questions and answers.

####################
# Model parameters #
####################
qp_path = '/mnt/lustre/sjtu/home/xyc30/remote/wiki/queries_paths_2hops.hdf5' # Path to load queries and paths.
reload_model='/mnt/lustre/sjtu/home/xyc30/remote/wiki/model_wikinav-16-4.npz'  # Path to a saved model we want to start from.
path_thes_idx = "/mnt/lustre/sjtu/home/xyc30/remote/wiki/th_en_US_new.idx" # Thesaurus
path_thes_dat = "/mnt/lustre/sjtu/home/xyc30/remote/wiki/th_en_US_new.dat" # Thesaurus