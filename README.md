# <prPred>
Prediction plant resistance proteins (R proteins)

prPred is a tool to to rapidly identify the R proteins of plant


## **Prerequisites**

### 1. **HMMER**

   To obtain HMMER releases, please visit http://hmmer.org/. 
   We also provide  HMMER zipped folders for download in prPred
   '''
   prPred need to make sure that the HMmer is in the environment variable
   '''
   #### **Install HMMER in Ubuntu**  
   
   > sudo apt-get install hmmer
   
   #### **Another way to install it
   **Download and build the source code release(optional)
   
   > wget http://eddylab.org/software/hmmer/hmmer.tar.gz  
   tar zxf hmmer.tar.gz  
   cd hmmer-3.3.2  
   ./configure --prefix /your/install/path  
   make  
   make check  
   > make install  
 
   #### ** prPred need add HMMER to the environment variable (/usr/bin/;/usr/local/bin/)**
   > vim ~/.bashrc    
   i    
   export PATH=$PATH:/your/install/path  
   :wq!  
   > source ~/.bashrc  

### 2. **phobius**
   Phobius:prediction of transmembrane topology and signal peptides from the amino acid sequence of a protein.
   To obtain phobius releases, please visit https://phobius.sbc.su.se/data.html.
   '''
   The software will be shipped immediately in the form of an attachment to the e-mail address you specify below
   '''
   **Add phobius into environment variables
   
   > export PATH=$PATH:/xxxx/xxxx/xxxxx/tmp/tmpbKioAY/phobius  
   
### 3. **PFAMDB**
   To obtain Pfam database,please download from  ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz
   
   > wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz  
     gunzip Pfam-A.hmm.gz  
     cd Pfam  
   > hmmpress Pfam-A.hmm  
   
    '''
    After hmmpress, we will get four files: Pfam-A.hmm.h3f，Pfam-A.hmm.h3i，Pfam-A.hmm.h3m，Pfam-A.hmm.h3p
    '''
   
   **Add PFAMDB (Pfam-A.hmm.h3f，Pfam-A.hmm.h3i，Pfam-A.hmm.h3m，Pfam-A.hmm.h3p) into environment variables 
   
   > export PFAMDB=/xxxx/xxxx/xxxx/Pfam  


## **Installation**

**prPred**

> git clone git@github.com:Wangys-prog/prPred.git  

**Add prPred into into environment variables

**(./prPred/dist/prPred)

> export PATH=$PATH:/xxxx/xxxx/xxxx/prPred/dist/prPred  


## Input parameters

> prPred -h  
$ -i  inputfile in FASTA format  
$ -o  output folder  

### usage

> prPred -i /xxxx/xxxx/test/test.fasta -o result  

**or
** Using absolute path to invoke prPred.py (/xxxx/xxxx/prPred/prPred.py)

> python xxxx/xxxx/prPred/prPred.py -i /xxxx/xxxx/test/test.fasta -o result  


**Output file 

> domain_result.csv  
> R_protein_possibility.fasta
 



