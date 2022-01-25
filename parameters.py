from file_paths import *

######################
# Dataset parameters #
######################
n_samples = [[1e8,1000,1000],[1e8,20000,20000],[1e8,20000,20000]] # maximum number of samples for the training, validation and test sets per hop
max_hops = [2,4,8] # Maximum number of hops to be visited to extract queries.
max_hops_pages = 10 # Maximum number of hops.
max_sents = 5 # Maximum number of query sentences to be extracted in each page.
max_links = 300 # Maximum number of links a page can have. If it has more links than max_links, only the first max_links are included in the dataset. Set it to None if you want all links to be included in the dataset.
min_words_query = 10 # Minimum number of words a query can have.
max_words_query = 30 # Maximum number of words a query can have.
n_words = 374000 # words for the vocabulary
n_consec = 4 # maximum number of consecutive sentences to form a query
root_page = 'category:main topic classifications'
max_candidates = 40 # maximum number of candidate documents that will be returned by the search engine.
search_engine = None # search engine to find candidate documents. Valid options are 'simple', 'lucene', 'google', and None.
create_index = True # If True, create index from wikipedia. If False, use the current one. Only used when search_engine='lucene'.
start_from_root = True # If True, start from <root_page>. If False, start from the first page returned by the search engine.


#########################
# Wikipedia  parameters #
#########################
compute_page_pos = True # Compute or not the page positions in the Wikipedia dump file


###############################
# Jeopardy dataset parameters #
###############################
jeopardy_n_samples = [1e8,10000,10000] # maximum number of samples for the training, validation and test sets.


####################
# Model parameters #
####################
dim_proj=2048  # LSTM number of hidden units.
dim_emb=500  # word embedding dimension.
patience=1000  # Number of epochs to wait before early stop if no progress.
max_epochs=5000  # The maximum number of epochs to run.
dispFreq=1  # Display to stdout the training progress every N updates.
lrate=0.0002  # Learning rate for sgd (not used for adadelta and rmsprop).
erate=0.1  # multiplier for the entropy regularization. Only used when act_sel='softmax'.
saveto='model.npz'  # The best model will be saved there.
validFreq=20000  # Compute the validation error after this number of updates.
saveFreq=20000  # Save the parameters after every saveFreq updates.
batch_size_train=16  # The batch size during training.
batch_size_pred=4  # The batch size during training.
max_hops_train = 10 # maximum number of pages to be visited before giving up - training.
max_hops_pred = 10 # maximum number of pages to be visited before giving up - prediction.
learning = 'supervised' # Valid options are: 'supervised', 'reinforce', and 'q-learning'.
act_sel = 'softmax' # Action selection types: 'epsilon-greedy' and 'softmax'. Only used when learning='q-learning', otherwise, act_sel='softmax'.
encoder='LSTM' # valid options are 'LSTM' or 'RNN'.
n_rnn_layers=4 # number of recurrent layers. must be >= 1.
n_doc_layers_nav=1 # number of layers after the document embedding in the navigation loop. must be >= 1.
scoring_layers_nav=[100,30] # list containing the number of hidden units in each intermediate scoring layer of the navigation loop. Set to [] if you want only one scoring layer.
reward_type = None # Possible values are 'continuous', 'discrete', or None (in this case, no reward is computed. Used to speed up computations when learning='supervised'.
#reload_model=False  # Path to a saved model we want to start from.
idb=False # use input-dependent baseline. Only used when learning='reinforce'.
mov_avg=False # use moving average baseline. Only used when learning='reinforce'.
train_size=5000  # If >0, we keep only this number of train examples when measuring accuracy.
valid_size=5000  # If >0, we keep only this number of valid examples when measuring accuracy.
test_size=5000  # If >0, we keep only this number of test examples when measuring accuracy.
fixed_wemb = True # set to true if you don't want to learn the word embedding weights.
k = 4 # beam search width. Used in prediction only.
dropout = 0.5 # If >0, <dropout> fraction of the units in the non-recurrent layers will be set to zero at training time.
att_query = True # if True, use attention mechanism on queries.
att_doc = False # if True, use attention mechanism on documents.
att_segment_type = 'word' # Type of segment document for attention. Valid values are 'section', 'subsection', 'sentence' and 'word'. Only used when att_doc=True.
max_segs_doc = 100 # Maximum number of segments per document. Only used when att_doc=True.
max_words = 1 # Maximum number of words per segment. Only used when att_doc=True.
window_query = [5] # Window size attention CNN. Only used when att_query=True.
window_doc = [5] # Window size for attention CNN. Only used when att_doc=True.
filters_query = [500] # Number of filters attention CNN. Only used when att_query=True.
filters_doc = [500] # Number of filters attention CNN. Only used when att_doc=True.
mixer = 0 # decrease one hop of supervision after <mixer> iterations. Should be used only when lerning='reinforce'. Set to 0 to disable it.
replay_mem_size = 1000000 # Experience replay memory size. Only used when learning='q-learning'.
replay_start = 50000 # Start updating weights only after <replay_start> steps. Only used when learning='q-learning'.
freeze_mem = 50000 # Only update memory after this number, except when number of iterations < replay start. Only used when learning='q-learning'.
prioritized_sweeping = 0.5 # if >=0.0, this parameter corresponds to the percentage of memories with reward=1 to be stored. Only used when learning='q-learning'.
saveto_mem = 'mem.pkl'  # The experience replay memory will be saved there. Only used when ='q-learning'.
reload_mem = False  # Path to the pickle file containing the experience replay memory. If reload_mem==False, the replay memory will start empty. Only used when learning='q-learning'.
update_freq = -1 # Interval between each next model weights update. If < 2, the same network is used for computing
                 # the target Q-values, but the gradients are disconnected. Only used when learning='q-learning'.
epsilon_start = 1.0 # Starting value for epsilon. Only used when learning='q-learning'.
epsilon_min = 0.1 # Minimum epsilon. Only used when learning='q-learning'.
epsilon_decay = 1 # Number of steps/updates to minimum epsilon. Only used when learning='q-learning'.
discount = 0.99 # Discount factor. Only used when learning='q-learning'.
clip = 1.0 # clip the cost at the this value. Only used when > 0 and learning='reinforce' or 'q-learning'.
aug = 1 # Augmentation on training dataset.
load_emb_mem = False # If true, load the entire hdf5 file specified at <pages_emb_path> onto memory. This speeds up the code but the memory must be at least the size of the hdf5 file.
compute_emb = False # If True, compute word embeddings on the fly. If False, use precomputed word embeddings from <pages_emb_path>.
weight_decay = 0.0 # weight decay multiplication factor.
