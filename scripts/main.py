import matplotlib.pyplot as plt
import moabb
import seaborn as sns
import warnings
import logging

from datasets.bcic import BCIC2008_IVa
from moabb.paradigms import MotorImagery
from moabb.evaluations import WithinSessionEvaluation

from mne.decoding import CSP
from sklearn.pipeline import make_pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

moabb.set_log_level('info')
logging.getLogger("moabb.datasets.preprocessing").setLevel(logging.ERROR)
warnings.filterwarnings('ignore')


bcic_dataset = BCIC2008_IVa()

bcic_dataset.subject_list = [1, 2 ,3, 4, 5]

bcic_session = bcic_dataset.get_data(subjects=[1])

subject = 1
session_name = "0train"
run_name = "0"

bcic_raw = bcic_session[subject][session_name][run_name]

paradigm = MotorImagery()

X, labels, meta = paradigm.get_data(dataset=bcic_dataset, subjects=[1])

pipeline = make_pipeline(CSP(n_components=8), LDA())

evaluation = WithinSessionEvaluation(
    paradigm=paradigm,
    datasets=[bcic_dataset],
    overwrite=True,
    hdf5_path=None,
)

results = evaluation.process({"csp+lda": pipeline})

results.to_csv("./results_iva.csv")

fig, ax = plt.subplots(figsize=(8, 7))
results["subj"] = results["subject"].apply(str)
sns.barplot(
    x="score", y="subj", data=results, orient="h", palette="viridis", ax=ax
)
plt.show()

