#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-
#
# author Radim Rehurek, radimrehurek@seznam.cz

import utils


class CorpusABC(utils.SaveLoad):
    """
    Interface for corpora. A 'corpus' is simply an iterable, where each 
    iteration step yields one document. A document is a list of (fieldId, fieldValue)
    2-tuples.
    
    See the corpora module for some example corpus implementations.
    
    Note that although a default len() method is provided, it is very inefficient
    (performs a linear scan through the corpus). Wherever the corpus size is known
    in advance (or at least doesn't change so that it can be cached), the len() method 
    should be overridden.
    """
    def __iter__(self):
        raise NotImplementedError('cannot instantiate abstract base class')

    
    def __len__(self):
        """
        Return the number of documents in the corpus. 
        
        This method is just the least common denominator and should really be 
        overridden when possible.
        """
        logging.warning("performing full corpus scan to determine its length; was this intended?")
        return sum(1 for doc in self) # sum(empty generator) == 0, so this works even for an empty corpus
#endclass CorpusABC


class TransformationABC(utils.SaveLoad):
    """
    Interface for transformations. A 'transformation' is any object which accepts
    a sparse document via the dictionary notation [] and returns another sparse
    document in its stead.
    
    See the tfidfmodel module for an example of a transformation.
    """
    def __getitem__(self):
        raise NotImplementedError('cannot instantiate abstract base class')
#endclass TransformationABC