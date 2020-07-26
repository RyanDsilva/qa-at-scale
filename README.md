# QA At Scale 🌟

Extending QA models to go from rather small context passages to large collections of documents with a focus on large scale deployment and quick results

> Uses PyTorch, Transformers, ElasticSearch and FastAPI

### Example 📁

> Trained on arXiv dump of NLP papers and using only CPU for inference

**System Used** 💻

- Intel i5 7th Gen
- 8GB RAM

#### Question ❓

> Searching through 10 candidate passages and selecting top-3 results

```json
{
  "question": "What methods can be used for Named Entity Recognition?"
}
```

#### Answers ✔️

> Response Time: 6.69s

```json
{
  "question": {
    "question": "What methods can be used for Named Entity Recognition?"
  },
  "answers": [
    {
      "answer": "rule-based and machine learning",
      "score": 16.775293350219727,
      "context": "es with particular reference to\nAssamese. There are various rule-based and machine learning approaches\navailable for Named Entity Recognition. At the ",
      "paper": {
        "url": "http://arxiv.org/pdf/1407.2918v1",
        "name": "A Survey of Named Entity Recognition in Assamese and other Indian\n  Languages"
      }
    },
    {
      "answer": "five text segmentation algorithms",
      "score": 6.862051010131836,
      "context": "entifier was subsequently performed. The\nevaluation, using five text segmentation algorithms for the English corpus and\nfour for the Greek corpus lead",
      "paper": {
        "url": "http://arxiv.org/pdf/1610.09226v1",
        "name": "Text Segmentation using Named Entity Recognition and Co-reference\n  Resolution in English and Greek Texts"
      }
    },
    {
      "answer": "keyword matching and vanilla word2vec models",
      "score": 5.693655967712402,
      "context": "erform the current state-of-the-art\nmethods based on keyword matching and vanilla word2vec models. Besides, the\nproposed methods can be trained fast a",
      "paper": {
        "url": "http://arxiv.org/pdf/1610.09091v3",
        "name": "Representation Learning Models for Entity Search"
      }
    }
  ]
}
```

> ##### Medium post will detailed explanation to follow soon

&copy; 2020 Ryan Dsilva
