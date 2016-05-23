A morpheme-based keyword search system is implemented in this final project.  The grapheme-based morphs are used in this project and to get their pronunciation
each IV word’s dictionary pronunciation is aligned to its morph sequence as in origin paper [1].


For the experiments, the IARPA Babel Turkish limited language pack (LimitedLP) dataset containing conversational telephone speech is used. For KWS evaluation, the 307 development queries, 88 (28.67%) of which are OOV, are used. Also for the LVCSR based KWS system, the Babel KWS setup in the Kaldi toolkit is used.

First of all, word corpus of the Kaldi toolkit is segmented by Morfessor toolkit. By using this training ouput, keywords are segmented to morphs.
The baseline Babel KWS setup in Kaldi is word-based, so the lexicon (word corpus and their phonetic transcriptions/pronunciation) is word-based. To build an acoustic model for our new system, we should give a morph-based lexicon to the Kaldi. Minimum edit distance algorithm is implemented to align words and their pronunciation to build a dictionary and this dictionary is used to get pronunciation of morphs.

The script
    edit_distance.py
takes the word-based lexicon and generates the dictionary. 

The other scripts
    eval_keywords.py
    get_TrainAsMorphs.py
    get_WordsAndMorphs.py
    iv.py
    lexiconp.py
    make_lexicon.py
    query.py
are used to change some word-based files in the Babel setup to their morph-based and to reform them in order to use in Kaldi system.

Since we have the morph-based lexicon,dictionary and subword-based vocabulary, the language model and the acoustic model can be generated.
By using Kaldi, a trigram language model and a morph-based acoustic model is built.
Also, a Viterbi decoder is implemented by Kaldi toolkit.

The link for the dataset:
http://svn.code.sf.net/p/kaldi/code/trunk/egs/babel/s5c/
The Kaldi toolkit:
http://kaldi-asr.org/
The Morfessor toolkit:
http://www.cis.hut.fi/projects/morpho/morfessor2.shtml

Reference
[1] He, Yanzhang, et al. "Using Pronunciation-Based Morphological Subword Units to Improve OOV Handling in Keyword Search." Audio, Speech, and Language Processing, IEEE/ACM Transactions on 24.1 (2016): 79-92.
