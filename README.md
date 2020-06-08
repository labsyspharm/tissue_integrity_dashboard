## Interactive dashboard showing DNA correlation coefficient as indicator of tissue integrity at single cell level

### Screenshot
![](screenshot.png)

### Instruction for local execution:
1. Install Docker engine (https://docs.docker.com/get-docker/)
2. Clone this repository  
   `git clone https://github.com/hungyiwu/tissue_integrity_dashboard.git`
3. Build Docker image (here the image name `dnacorrcoef` and version number `0.1` are arbitrary)  
   `docker build -t dnacorrcoef:0.1 .`
4. Run Docker image  
   `docker run -it -v $PWD/code:/home/code -v $PWD/data:/home/data -p 5006:5006 dnacorrcoef:0.1`
5. Open your web browser (Chrome, Firefox, Safari, ..., etc.) and go to `http://localhost:5006/app` to see the dashboard

### Data source
Citation: Rashid R. et al. Sci. Data 2019  
Main article URL: https://dx.doi.org/10.1038%2Fs41597-019-0332-y  
Data URL: https://dx.doi.org/10.7303%2Fsyn17865732  
Data name: DATASET-1 > LUNG-1-LN > 40X  
Retrival date: June 6, 2020  

Preprocessing steps:  
1. Antibody panel scraped from main article online-only table 2  
URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6917801/table/Tab4/?report=objectonly  
2. Raw data (`.rcpnl` files) were processed using `mcmicro-nf`([GitHub](https://github.com/labsyspharm/mcmicro-nf))  
3. 10 single cells were selected for demonstration  
