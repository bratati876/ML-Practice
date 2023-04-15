# we have to mention all the details of the package to make the project consider as a package
from setuptools import setup, find_packages


setup(name="credit_card prediction",
      version="0.0.1",
      author="bratati",
      author_email="bratatidattagupta@gmail.com",
      packages=find_packages(),
      install_requirements=["pandas", "numpy", "flask"]
)

# find_packages function will find the __int__.py file in the folders
# and if it is not consisting the file then, it would not consider the folder as a package
