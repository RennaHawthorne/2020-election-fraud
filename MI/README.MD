# Michigan Repo

## Data Sources
https://michiganvoters.info/
http://69.64.83.144/~mi/download/20201012/
File had to be fixed with this `vim +"set nobomb | set fenc=utf8 | x" EntireStateVoters.csv`

## Usage

#### Convert to Json
`python3 main.py EntireStateVotersFixed.csv out.json`