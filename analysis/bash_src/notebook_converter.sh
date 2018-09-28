rm src/*.py

jupyter nbconvert --to script src/Census_Data.ipynb
jupyter nbconvert --to script src/Mortality_Data.ipynb
jupyter nbconvert --to script src/Inference_NB.ipynb
jupyter nbconvert --to script src/PR_Map.ipynb
jupyter nbconvert --to script src/Quantiles.ipynb