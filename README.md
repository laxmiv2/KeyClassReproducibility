<h1 align="center">KeyClass: Text Classification with Label-Descriptions Only</h1>

**Reproducibility Study**  
*Laxmi Vijayan, Aganze Mihigo*  
*Team 95*  

*Description*  
`KeyClass` is a weakly-supervised text classification framework that labels documents using *class-label descriptions* and leveraging pre-trained language models and the data programming framework to assign probabilistic labels. 

The original paper demonstrates the efficacy and flexibility of the KeyClass framework by comparing it to state-of-the-art weak text classifiers across four real-world text classification datasets.

## Contents

1. [Datasets](#datasets)
2. [Tutorial](#tutorial)
3. [Installation](#installation)
4. [Reproducing Results](#reproduce)
5. [Results](#results)
6. [Citation](#citation)

----
<a id="datasets"></a>
## Datasets

To download the datasets used in the paper, run this [script](https://github.com/autonlab/KeyClass/blob/main/scripts/get_data.sh)

Note: Amazon and DBPedia will not be accessible via the script. Please use the links directly. 

<a id="tutorial"></a>
## Tutorial
To familiarize yourself with `KeyClass`, there are two tutorials you can leverage. One tutorial was provided by the original authors of the paper located here: following [tutorial](https://github.com/autonlab/KeyClass/blob/main/tutorials/Tutorial%20on%20IMDB.ipynb). 

A more beginner-friendly tutorial can be found here: [Interactive Tutorial](https://github.com/laxmiv2/KeyClassReproducibility/blob/9b24edbfdf5e234190d3a4774aebb3841c8c08ce/Interactive%20Tutorial%20Explanation%20of%20KeyClass.ipynb).

<a id="installation"></a>
## Installation

All models were built and trained using PyTorch 1.8.1 using Python 3.8.1. 

Some trials were run on a consumer-grade Apple Mac Air with an Apple M2 Silicon chip. 

For most, we use a Precision 5820 Tower computer equipped with a powerful Intel Xeon W-2133 CPU running at 3.60 GHz with 12 cores, supported by 32.0 GB of memory. For graphics, we have an NVIDIA Quadro P4000 (GP104GL), which provides fair but not enough for our experiments. Our system runs on Ubuntu 22.04.4 L TS (64-bit), with GNOME version 42.9.

Setup the environment with the following steps: 

``` bash
pip install snorkel transformers tokenizers sentence-transformers pyhealth gdown
```

<a id="reproduce"></a>
## Reproducing Results

To reproduce our results, please verify paths for config files and in local notebooks. Then, the notebooks can be run. 

<a id="results"></a>
## Reproducing Results

IMDb Movie Review Results
| Phase                                          | Accuracy (mean, std)                  | Precision (mean, std)                | Recall (mean, std)                  |
|------------------------------------------------|---------------------------------------|--------------------------------------|-------------------------------------|
| Train - Label Model with Ground Truth          | 0.70016                               | 0.71811                              | 0.70016                             |
| Train - End Model with Ground Truth            | 0.91814                               | 0.92262                              | 0.91814                             |
| Train - End Model with Label Model             | 0.92186                               | 0.92188                              | 0.92186                             |
| Test - End Model with Ground Truth             | 0.84744 ± 0.00197                     | 0.86153 ± 0.00177                    | 0.84744 ± 0.00197                   |
| Test - End Model with Ground Truth (Self-Train)| 0.91513 ± 0.00172                     | 0.91526 ± 0.00171                    | 0.91513 ± 0.00172                   |


<a id="citation"></a>
## Citation
If you use the original paper's code please cite the following paper. 
```
@article{gao2022classifying,
  title={Classifying Unstructured Clinical Notes via Automatic Weak Supervision},
  author={Gao, Chufan and Goswami, Mononito and Chen, Jieshi and Dubrawski, Artur},
  journal={Machine Learning for Healthcare Conference},
  year={2022},
  organization={PMLR}
}
```
