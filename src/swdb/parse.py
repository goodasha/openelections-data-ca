import codes
import pandas as pd

from swdb import SWDBResults
from util import COUNTIES

candidate_norm = {'Eleanor Garcia': 'Eleanor García',
                  'Kenneth Canada': 'Kenneth "Mike" Canada',
                  'Juan Mercado-Flores': 'Juan "Charly" Mercado-Flores',
                  'Reagan Allvord': 'Terry Reagan Allvord',
                  'Juan M. Hidalgo, Jr.': 'Juan M. Hidalgo Jr.',
                  'Nicholas Walpert': 'Nicholas "Nick" Walpert',
                  'Melinda K. Vasquez': 'Melinda K. Vásquez',
                  'Andrew Masiel, Sr.': 'Andrew Masiel Sr.',
                  'Teresita Andres': 'Teresita "Tess" Andres',
                  'N. Eugene Cleek': 'N Eugene Cleek',
                  'Robert Evans': 'Robert (Bob) Evans',
                  'Mario Galvan': 'Mario Galván',
                  'Greg Coppes': 'Greg "Coach" Coppes',
                  'Carlos Taylor': 'Carlos "Chuck" Taylor',
                  'Veronica Jacobi': 'Veronica "Roni" Jacobi',
                  'William Ostrander': 'William "Bill" Ostrander',
                  'Donald Fareed': 'Justin Donald Fareed',
                  'Ron Mikulaco': 'Ron "Mik" Mikulaco',
                  'Bogdan Ambrozewicz': '"Bo" Bogdan I. Ambrozewicz',
                  'S. Monique Limon': 'S. Monique Limón',
                  'A. Rab': 'A. (Raji) Rab',
                  'Stephan Wolkowicz': 'Stephan "Steven" Wolkowicz',
                  'Rudolfo Gaona': 'Rodolfo Rudy Gaona',
                  'Linda T. Sanchez': 'Linda T. Sánchez',
                  'Michael Adams': 'Scott Michael Adams',
                  'John M. W. Moorlach': 'John M.W. Moorlach',
                  'William Brough': 'William (Bill) Brough',
                  'Michael J. Barkley': 'Michael J. "Mike" Barkley',
                  'Jacob Souza': 'Jacob "Jake" Souza',
                  'Antonio C. Amador': 'Antonio C. "Tony" Amador',
                  'Pierluigi C. Olivero': 'Pierluigi C. Oliverio',
                  'Jacob Cabrera': 'Jay Blas Jacob Cabrera',
                  'Phlunte Riddle': "Phlunte' Riddle",
                  'Sandre R. Swanson': 'Sandré R. Swanson',
                  'Nanette Diaz Barragan': 'Nanette Diaz Barragán',
                  'Joseph Shammas': 'Joseph "Joe" Shammas',
                  'Benny Bernal': 'Benny "Benito" Bernal',
                  'Roger Hernandez': 'Roger Hernández',
                  }


for county in COUNTIES:
    print(county)
    try:
        results = SWDBResults('P16', county, candidate_norm)
    except Exception as e:
        print(e)
        continue

    results.df.to_csv(
        '2016/20160607__ca__primary__%s__precinct.csv' % (
            county.lower().replace(' ', '_')), index=False)
