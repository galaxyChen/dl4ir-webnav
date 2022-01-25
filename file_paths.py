######################
# Dataset parameters #
######################
vocab_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/D_cbow_pdw_8B.pkl' # Path to the python dictionary containing the vocabulary.
wordemb_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/D_cbow_pdw_8B.pkl' # Path to the python dictionary containing the word embeddings.
idf_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/wiki_idf.pkl' # Path to the IDF dictionary.
pages_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/wiki.hdf5' # Path to save the articles and links.
pages_emb_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/wiki_emb.hdf5' # Path to save articles embeddings (set to None to not compute it).
pages_idx_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/wiki_idx.hdf5' # Path to save articles' words as vocabulary indexes (set to None to not compute it).
qp_path_pre = '/Users/galaxy/code/wiki-pretrain/data/wiki/qp.hdf5' # Path to save queries and paths.
index_folder = '/Users/galaxy/code/wiki-pretrain/data/wiki/lucene_index/' # folder to store lucene's index. It will be created in case it does not exist.

#########################
# Wikipedia  parameters #
#########################
dump_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/enwiki-latest-pages-articles.xml' # Path to the wikipedia dump file.
page_pos_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/page_pos.pkl' # Path to save the dictionary that stores each article position in the wikipedia dump file.
cat_pages_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/cat_pages.pkl' # Path to save the dictionary that stores the pages in each wikipedia category.

###############################
# Jeopardy dataset parameters #
###############################
jeopardy_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/JEOPARDY.csv' # Path to the csv containing jeopardy questions and answers.

####################
# Model parameters #
####################
qp_path = '/Users/galaxy/code/wiki-pretrain/data/wiki/queries_paths_4hops.hdf5' # Path to load queries and paths.
reload_model='/Users/galaxy/code/wiki-pretrain/data/wiki/model_wikinav-16-4.npz'  # Path to a saved model we want to start from.
path_thes_idx = "/Users/galaxy/code/wiki-pretrain/data/wiki/th_en_US_new.idx" # Thesaurus
path_thes_dat = "/Users/galaxy/code/wiki-pretrain/data/wiki/th_en_US_new.dat" # Thesaurus