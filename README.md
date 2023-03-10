# NFeMiner
### _Identifying Similar Invoices through Product Purchase Description using Representation Learning and Price Analysis_


The objective of this project is to develop a tool that can identify similar invoices based on the product purchase description. Additionally, the tool will be able to identify invoices with similar products but different sales prices to generate overprice alerts for inspection agencies.

NFeMiner will use representation learning to create word embeddings to represent invoices. The similarity of invoices will be calculated in the embedding space. The project will use techniques such as clustering and dimensionality reduction to identify similar invoices. To identify similar invoices with different sales prices, the project will use price analysis techniques. NFeMiner will compare the prices of products and services in the invoices to identify discrepancies. The tool will then generate overprice alerts for inspection agencies to monitor specific segments of interest.

NFeMiner will represent the model through a graph, which will allow exploratory analysis of invoices connected by similarity. The graph will visually differentiate invoices by color and size based on the sale price of products and services. This will allow for easy identification of patterns and anomalies.

## Installation

Install the dependencies and ElasticSearch server.

```sh
sh nfeminer/setup.sh
```

Optionally, populate ElasticSearch with some sample invoices.

```sh
sh nfeminer/nfe_data_populate.sh
```

Instala NFeMiner package.

```sh
cd nfeminer; pip install .
```

## NFeMiner usage

Import NFeMiner

```sh
import nfeminer
```

See an example of how to use the NFeMiner library.

https://colab.research.google.com/drive/1Pm__a8k3AC7TqYt_H7a0iPEiG81_80o2


