from setuptools import setup, find_packages

setup(
    name='Streamlit_SQLServer_Crosstab.py',  # Replace with your package name
    version='0.1.0',  # Initial version of your package
     url='https://github.com/Purdue0279/Streamlit_Tableau.git',  # Replace with your package URL
    packages=find_packages(),  # Automatically find your package modules
    install_requires=[  # List of dependencies for your package
                        'streamlit'
                        'streamlit-aggrid'
                        'pandas'
                        'pyodbc'
                        'numpy'
                        'ipython'
                        'requests_kerberos'
                        'requests'
                        'setuptools'
                        'cython'
                        'wheel'
                    ],
    python_requires='>=3.6',  # Specify Python version compatibility

    
)