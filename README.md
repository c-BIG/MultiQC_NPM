# MultiQC_NPM

A [MultiQC](https://multiqc.info/) plugin to support QC efforts within the National Precision Medicine programme in Singapore (NPM), a local initiative that intends to sequence the genomes of 100K individuals (SG100K).

## Quick start

Parsing of additional data files through MultiQC_NPM can be enabled using the `--enable-npm-plugin` option, e.g.:

```
multiqc . --data-format json --enable-npm-plugin
```

All other [MultiQC options](https://multiqc.info/docs/#running-multiqc) remain unchanged.

## Description

MultiQC_NPM builds upon the base functionality of MultiQC to add the following:

- Extended parsing for third-party tools: bcftools gtcheck, picard CollectQualityYieldMetrics, samtools stats FFQ/LFQ.
- Support for custom tools: sg10k-cov-062017.sh, count_variants.py.

For additional context on how each tool is used, please refer to the [NPM-sample-qc](https://github.com/c-BIG/NPM-sample-qc) repository.
