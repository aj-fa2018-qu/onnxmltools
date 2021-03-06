"""
Tests scikit-learn's binarizer converter.
"""
import unittest
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from onnxmltools import convert_sklearn
from onnxmltools.convert.common.data_types import StringTensorType
from onnxmltools.utils import dump_data_and_model


class TestSklearnTfidfVectorizer(unittest.TestCase):

    def test_model_tfidf_vectorizer11(self):
        corpus = [
                'This is the first document.',
                'This document is the second document.',
                'And this is the third one.',
                'Is this the first document?',
                ]
        vect = TfidfVectorizer(ngram_range=(1, 1))
        vect.fit(corpus)
        pred = vect.transform(corpus)
        model_onnx = convert_sklearn(vect, 'scikit-learn count vectorizer', [('input', StringTensorType([1, 1]))])
        self.assertTrue(model_onnx is not None)
        # REVIEW: enable the test when the runtime implements the primitives.
        # dump_data_and_model(corpus, vect, model_onnx, basename="SklearnTfidfVectorizer")

    def test_model_tfidf_vectorizer13(self):
        corpus = [
                'This is the first document.',
                'This document is the second document.',
                'And this is the third one.',
                'Is this the first document?',
                ]
        vect = TfidfVectorizer(ngram_range=(1, 3))
        vect.fit(corpus)
        pred = vect.transform(corpus)
        model_onnx = convert_sklearn(vect, 'scikit-learn count vectorizer', [('input', StringTensorType([1, 1]))])
        self.assertTrue(model_onnx is not None)
        # REVIEW: enable the test when the runtime implements the primitives.
        # dump_data_and_model(corpus, vect, model_onnx, basename="SklearnTfidfVectorizer")


if __name__ == "__main__":
    unittest.main()
