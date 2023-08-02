# <prPred> Python3.7
   
# prPred 
prPred is a tool to identify the plant resistance proteins (R proteins) 

prPred is an open-source Python-based toolkit, which operates depending on the Python environment (Python Version 3.0 or above). Before running prPred, user should make sure all the following packages are installed in their Python environment: subprocess, datetime, os, shutil, pandas,numpy, Biopython,sklearn,optparse


## **Prerequisites**


### 1. **HMMER**

   To obtain HMMER releases, please visit http://hmmer.org/. 
   We also provide  HMMER zipped folders for download in prPred
   
   
   <**prPred need to make sure that the HMMER is in the environment variable**>
   
   
   #### **Install HMMER in Ubuntu**
    sudo apt-get install hmmer
   
   #### **Another way to install it**
   **Download and build the source code release(optional)**
   
    wget http://eddylab.org/software/hmmer/hmmer.tar.gz
    tar zxf hmmer.tar.gz
    cd hmmer-3.3.2
    ./configure --prefix /your/install/path
    make
    make check
    make install  
 
   #### **prPred need add HMMER to the environment variable (/usr/bin/;/usr/local/bin/)**
    vim ~/.bashrc
    i
    export PATH=$PATH:/your/install/path
    :wq!
    source ~/.bashrc  

### 2. **phobius**

   Phobius:prediction of transmembrane topology and signal peptides from the amino acid sequence of a protein.
   To obtain phobius releases, please visit https://phobius.sbc.su.se/data.html.  
   
   installation procedure  https://www.jianshu.com/p/32176552cb5c
   
   <**The software will be shipped immediately in the form of an attachment to the e-mail address you specify below**>
      
    tar -xzvf phobius101_linux.tar.gz
    cd /xxxx/xxxx/xxxx/tmp/tmpbKioAY/phobius
   
    '''
    Error - could not read provided fasta sequences
    Modify line 24 in phobius.pl
    my $DECODEANHMM = "$PHOBIUS_DIR/decodeanhmm.64bit"
    '''
   
   **Add phobius into environment variables (~/.bashrc)**
      
    export PATH=$PATH:/xxxx/xxxx/xxxxx/tmp/tmpbKioAY/phobius  
  
  
   
### 3. **PFAMDB**

   To obtain Pfam database,please download from  ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz
   
    mkdir Pfam  
    cd Pfam  
    wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz  
    gunzip Pfam-A.hmm.gz   
    hmmpress Pfam-A.hmm  
   
    '''
    After hmmpress, we will get four files: Pfam-A.hmm.h3f，Pfam-A.hmm.h3i，Pfam-A.hmm.h3m，Pfam-A.hmm.h3p
    '''
   
   **Add PFAMDB (Pfam-A.hmm.h3f，Pfam-A.hmm.h3i，Pfam-A.hmm.h3m，Pfam-A.hmm.h3p) into environment variables** 
    
    vim ~/.bashrc**
    export PFAMDB=/xxxx/xxxx/xxxx/Pfam  
   
   

### 4. **iFeature**
    
    To obtain iFeature, please download from https://github.com/Superzchen/iFeature/.
    
   **Add iFeature into environment variables (~/.bashrc)** 
   
   export PATH=$PATH:/xxxx/xxxx/xxxxx/iFeature
   

## **Installation**

###**prPred**

    git clone git@github.com:Wangys-prog/prPred.git  

**Add prPred into into environment variables**

**(./prPred/dist/prPred)**

    export PATH=$PATH:/xxxx/xxxx/xxxx/prPred/dist/prPred  


## Input parameters
    prPred -h  
    $ -i  inputfile in FASTA format  
    $ -o  output folder  
### usage (Python Version 3.0 or above)
    prPred -i /xxxx/xxxx/test/test.fasta -o result  
**or**
**Using absolute path to invoke prPred.py (/xxxx/xxxx/prPred/prPred.py)** ,this command run using python3.7

    python 3.7 xxxx/xxxx/prPred/prPred.py -i /xxxx/xxxx/test/test.fasta -o /xxxx/xxxxx/result  
      
###**Output file**

    domain_result   
    R_protein_possibility.fasta

## For split_fasta.py
**Analyze your sequences such as 20 sequences**  
**Before using the script,please add prPred into into environment variables**
**split your large fasta file into small fasta file with such as 20 sequence**
**if you fasta has total 100 sequences,you can split you fasta into 5 small fasta files**    
     
     seqkit split your.fasta -p 5

**then using split_fasta2.py to predict R protein sequences** 

     python split_fasta.py -i your split_fasta folder

**merge your result**

    python merge_result.py -i split_fasta_result -o merged_result.csv
 
## For windows 10 or later

**Download Ubuntu xx.x LTS from Microsoft Store**

    cd ../../
    cd mnt/x/xxxx/xxxx/
    git clone git@github.com:Wangys-prog/prPred.git
    cd mnt/x/xxxx/xxxx/prPred/  

## **If you use prPred, please cite:** 
    (1) Wang Y, Wang P, Guo Y, et al. prPred: A Predictor to Identify Plant Resistance Proteins by Incorporating k-Spaced Amino Acid (Group) Pairs[J]. Frontiers in bioengineering and biotechnology, 2021, 8: 1593.
    (2) Yansu Wang, Murong Zhou, Quan Zou, Lei Xu. Machine learning for phytopathology: from the molecular scale towards the network scale. Briefings in Bioinformatics. 2021, Doi: 10.1093/bib/bbab037
    (3) Yansu Wang, Lei Xu, Quan Zou, Chen Lin. prPred-DRLF: plant R protein predictor using deep representation learning features. Proteomics. 2021. DOI: 10.1002/pmic.202100161
