# MOABB Project: BCI Competition III Dataset IVa

A custom MOABB-compatible dataset loader for BCI Competition III dataset IVa.

## Overview 

This project aims to add the BCI competition III dataset IVa as a subclass
to the Mother of All BCI Benchmarks (MOABB), enabling easy integration
with EEG classification pipelines. 

## Features

- Compatible with MOABB's get_data() API

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/moabb_dataset_iva.git
cd datasets
pip install -e .
```

## Dataset Description

| Property           | Value                     | Explanation                                                             |
|--------------------|---------------------------|-------------------------------------------------------------------------|
| Dataset            | BCI Competition III - IVa | Official dataset name                                                   |
| Subjects           | 5                         | Subjects: aa, al, av, aw, ay                                            |
| Channels           | 118                       | 118 EEG channels                                                        |
| Classes            | 2                         | Right hand and foot motor imagery                                       |
| Trials/Class       | 84                        | Based on subject aa, 168 labeled trials across 2 classes = 84 per class |
| Trial Duration (s) | 3.5                       | Each cue lasted 3.5 seconds                                             |
| Total Trials       | 1400                      | 5 subjects x 280 trials = 1400 total trials                             |
| Frequency (Hz)     | 100                       | Sampling rate                                                           |
| Sessions           | 4                         | 4 sessions per subject                                                  |
| Runs               | 1                         | Data recorded as one continuous run                                     |

## To Do

- Add support for other BCI Competition III datasets

## Contributing

Pull requests are welcome.

## References

- Guido Dornhege, Benjamin Blankertz, Gabriel Curio, and Klaus-Robert Müller - [Dataset IVa](https://www.bbci.de/competition/iii/desc_IVa.html)
- Aristimunha, B., Carrara, I., Guetschel, P., Sedlar, S., Rodrigues, P., Sosulski, J., Narayanan, D., Bjareholt, E., Barthelemy, Q., Schirrmeister, R. T., Kobler, R., Kalunga, E., Darmet, L., Gregoire, C., Abdul Hussain, A., Gatti, R., Goncharenko, V., Thielen, J., Moreau, T., Roy, Y., Jayaram, V., Barachant, A., & Chevallier, S. (2025).
Mother of all BCI Benchmarks (MOABB), 2025. DOI: 10.5281/zenodo.10034223.

