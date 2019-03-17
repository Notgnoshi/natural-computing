# natural-computing

Graduate coursework in Natural Computing

---

Ensure that `nbstripout` is installed, and has its precommit hooks installed on the local copy of
this repository. E.g.,

```shell
git clone git@github.com:Notgnoshi/natural-computing.git
cd natural-computing
# I like putting my virtualenvs in my home directory,
#others like a VCS excluded file in their repo.
mkdir -p ~/.virtualenvs
virtualenv ~/.virtualenvs/natural
source ~/.virtualenvs/natural/bin/activate
pip install -r requirements.txt
# Doesn't output anything, just indicates success via exit status -_-
nbstripout --is-installed
echo $?
nbstripout --install
nbstripout --is-installed
echo $?
```

`nbstripout` *must* be installed to prevent committing output in a Jupyter notebook. The output of
the code in a Jupyter notebook is save *inside the notebook*. Thus, for stochastic algorithms every
run of the notebook will modify the notebook differently. It is essential to not commit these changes
to keep a meaningful commit history, and to keep the saved file blobs small (it saves images, SVGs,
PNGs, etc all in the notebook JSON...)
